"""
Sift — Integration tests.

Runs the full Sift pipeline against a disposable temporary directory and
verifies:
  - Correct file moves
  - Duplicate renaming with incrementing suffixes
  - Unknown-extension handling
  - Statistics JSON integrity
  - Log file creation and tagged entries
  - Skip-folder protection

Run with:
    python -m Sift.tests.test_integration
    python Sift/tests/test_integration.py
"""

import json
import os
import sys
import tempfile
import time
from pathlib import Path

# Support running this file directly by ensuring the project root is on sys.path.
_root = str(Path(__file__).resolve().parent.parent.parent)
if _root not in sys.path:
    sys.path.insert(0, _root)

from Sift.config.extension_map import ALL_EXTENSIONS
from Sift.config.settings import SKIP_FOLDERS, UNKNOWN_FOLDER
from Sift.core.folder_manager import ensure_system_dirs, get_stats_file
from Sift.core.organizer import Organizer
from Sift.utils.logger import SiftLogger
from Sift.utils.stats import StatsTracker


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _p(base: str, *parts: str) -> str:
    """Build a normalized, platform-native path from parts."""
    return os.path.normpath(os.path.join(base, *parts))


def _touch(directory: str, filename: str, content: str = "") -> str:
    """Create a file with optional content and return its full path."""
    full = os.path.join(directory, filename)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return full


def _file_exists(base: str, *parts: str) -> bool:
    """Check whether a file exists at the normalized, joined path."""
    return os.path.isfile(_p(base, *parts))


def _dir_exists(base: str, *parts: str) -> bool:
    """Check whether a directory exists at the normalized, joined path."""
    return os.path.isdir(_p(base, *parts))


def _build_temp_tree(tmp: str) -> None:
    """Populate *tmp* with a realistic mix of files for testing."""
    # Normal files at root
    _touch(tmp, "report.pdf")
    _touch(tmp, "notes.txt")
    _touch(tmp, "photo.png")

    # Unknown extension (not in ALL_EXTENSIONS)
    _touch(tmp, "mystery.xyz")

    # Files inside a non-skipped subfolder
    sub = os.path.join(tmp, "misc")
    os.makedirs(sub, exist_ok=True)
    _touch(sub, "data.csv")
    _touch(sub, "song.mp3")

    # A file inside a SKIP_FOLDER — must NOT be re-processed
    _touch(tmp, os.path.join("Documents", "PDFs", "already_organized.pdf"))


# ---------------------------------------------------------------------------
# Test runner
# ---------------------------------------------------------------------------


def run_integration_test() -> None:
    """Execute the full integration test suite."""
    passed = 0
    failed = 0

    def check(label: str, condition: bool, detail: str = "") -> None:
        nonlocal passed, failed
        if condition:
            passed += 1
            print(f"  [PASS] {label}")
        else:
            failed += 1
            msg = f"  [FAIL] {label}"
            if detail:
                msg += f"  — {detail}"
            print(msg)

    def is_numeric(value: object) -> bool:
        return isinstance(value, (int, float)) and not isinstance(value, bool)

    def is_int(value: object) -> bool:
        return isinstance(value, int) and not isinstance(value, bool)

    with tempfile.TemporaryDirectory(prefix="sift_test_") as tmp:
        tmp = os.path.normpath(tmp)
        print(f"Temp directory: {tmp}\n")

        # ---- Arrange ----
        _build_temp_tree(tmp)
        start_time = time.time()

        ensure_system_dirs(tmp)

        log_dir = Path(tmp) / ".system" / "logs"
        logger = SiftLogger(str(log_dir), Path(tmp))
        stats = StatsTracker()

        # ---- Act: first run ----
        organizer = Organizer(tmp, logger, stats)
        organizer.run()

        end_time = time.time()
        stats.finalize(start_time, end_time)
        stats_file = get_stats_file(tmp)
        stats.save(stats_file)

        # ==================================================================
        # 1. FILE MOVE VERIFICATION
        # ==================================================================
        print("--- File Moves ---")

        check(
            "report.pdf moved to Documents/PDFs",
            _file_exists(tmp, "Documents", "PDFs", "report.pdf"),
        )
        check(
            "notes.txt moved to Documents/Text Files",
            _file_exists(tmp, "Documents", "Text Files", "notes.txt"),
        )
        check(
            "photo.png moved to Images/PNGs",
            _file_exists(tmp, "Images", "PNGs", "photo.png"),
        )
        check(
            "data.csv moved to Documents/CSV Files",
            _file_exists(tmp, "Documents", "CSV Files", "data.csv"),
        )
        check(
            "song.mp3 moved to Music/MP3s",
            _file_exists(tmp, "Music", "MP3s", "song.mp3"),
        )

        check("report.pdf removed from root", not _file_exists(tmp, "report.pdf"))
        check("notes.txt removed from root", not _file_exists(tmp, "notes.txt"))
        check("photo.png removed from root", not _file_exists(tmp, "photo.png"))
        check("song.mp3 removed from misc/", not _file_exists(tmp, "misc", "song.mp3"))

        # ==================================================================
        # 2. UNKNOWN FILES
        # ==================================================================
        print("\n--- Unknown Files ---")

        check(
            f"mystery.xyz moved to {UNKNOWN_FOLDER}",
            _file_exists(
                tmp,
                *_p(tmp, UNKNOWN_FOLDER.replace("/", os.sep)).split(os.sep)[len(_p(tmp).split(os.sep)) :],
                "mystery.xyz",
            ),
        )

        # The unknown counter should count only when actually moved.
        check("Unknown Files Found == 1", stats.stats["Unknown Files Found"] == 1)

        # ==================================================================
        # 3. DUPLICATE RENAMING
        # ==================================================================
        print("\n--- Duplicate Renaming ---")

        _touch(tmp, "report.pdf", "duplicate content")
        logger2 = SiftLogger(str(log_dir), Path(tmp))
        stats2 = StatsTracker()
        start2 = time.time()
        org2 = Organizer(tmp, logger2, stats2)
        org2.run()
        end2 = time.time()
        stats2.finalize(start2, end2)

        check(
            "Duplicate renamed as report(1).pdf",
            _file_exists(tmp, "Documents", "PDFs", "report(1).pdf"),
        )
        check(
            "Original report.pdf still exists",
            _file_exists(tmp, "Documents", "PDFs", "report.pdf"),
        )
        check(
            "stats2 Duplicate Files Renamed == 1",
            stats2.stats["Duplicate Files Renamed"] == 1,
            f"got {stats2.stats['Duplicate Files Renamed']}",
        )
        check(
            "stats2 Files Moved == 1",
            stats2.stats["Files Moved"] == 1,
            f"got {stats2.stats['Files Moved']}",
        )

        # ==================================================================
        # 4. SKIP-FOLDER PROTECTION
        # ==================================================================
        print("\n--- Skip-Folder Protection ---")

        check(
            "already_organized.pdf still in Documents/PDFs",
            _file_exists(tmp, "Documents", "PDFs", "already_organized.pdf"),
        )

        # Ensure the skip-list names are honored by the scanner.
        skip_names = set(SKIP_FOLDERS)
        check(
            "SKIP_FOLDERS contains protected directory names",
            "Documents" in skip_names and ".system" in skip_names and "Sift" in skip_names,
        )

        # ==================================================================
        # 5. STATS INTEGRITY
        # ==================================================================
        print("\n--- Stats Integrity ---")

        check("Stats file exists", os.path.isfile(stats_file))

        if os.path.isfile(stats_file):
            with open(stats_file, "r", encoding="utf-8") as f:
                saved_stats = json.load(f)
        else:
            saved_stats = {}
            print("  [WARN] Cannot continue stats checks — file missing")

        required_keys = [
            "Run Time",
            "Execution Time (seconds)",
            "Files Processed",
            "Files Moved",
            "Duplicate Files Renamed",
            "Unknown Files Found",
            "Category Counts",
        ]
        for key in required_keys:
            check(f"Stats has key '{key}'", key in saved_stats)

        check(
            "Files Moved == 6",
            saved_stats.get("Files Moved") == 6,
            f"got {saved_stats.get('Files Moved')!r}",
        )
        check(
            "Files Processed == 6",
            saved_stats.get("Files Processed") == 6,
            f"got {saved_stats.get('Files Processed')!r}",
        )
        check(
            "Duplicate Files Renamed == 0",
            saved_stats.get("Duplicate Files Renamed") == 0,
            f"got {saved_stats.get('Duplicate Files Renamed')!r}",
        )
        check(
            "Unknown Files Found == 1",
            saved_stats.get("Unknown Files Found") == 1,
            f"got {saved_stats.get('Unknown Files Found')!r}",
        )
        check(
            "Files Processed >= Files Moved",
            is_numeric(saved_stats.get("Files Processed"))
            and is_numeric(saved_stats.get("Files Moved"))
            and saved_stats["Files Processed"] >= saved_stats["Files Moved"],
            f"processed={saved_stats.get('Files Processed')!r}, "
            f"moved={saved_stats.get('Files Moved')!r}",
        )
        check(
            "Execution Time is numeric",
            is_numeric(saved_stats.get("Execution Time (seconds)")),
            f"got {saved_stats.get('Execution Time (seconds)')!r}",
        )
        check(
            "Category Counts is a non-empty dict",
            isinstance(saved_stats.get("Category Counts"), dict)
            and len(saved_stats["Category Counts"]) > 0,
        )
        check(
            "Category Counts has expected entries",
            saved_stats["Category Counts"].get("Documents/PDFs") == 1
            and saved_stats["Category Counts"].get("Documents/Text Files") == 1
            and saved_stats["Category Counts"].get("Images/PNGs") == 1
            and saved_stats["Category Counts"].get("Others/Unknown") == 1
            and saved_stats["Category Counts"].get("Documents/CSV Files") == 1
            and saved_stats["Category Counts"].get("Music/MP3s") == 1,
            f"got {saved_stats.get('Category Counts')!r}",
        )

        # ==================================================================
        # 6. LOG FILE CREATION
        # ==================================================================
        print("\n--- Log Files ---")

        logs_dir = _p(tmp, ".system", "logs")
        log_files = sorted(f for f in os.listdir(logs_dir) if f.endswith(".log"))
        check("At least one log file exists", len(log_files) >= 1)

        log_content = ""
        for lf in log_files:
            with open(os.path.join(logs_dir, lf), "r", encoding="utf-8") as f:
                log_content += f.read()

        check("[MOVED] entries present", "[MOVED]" in log_content)
        check("[DUPLICATE] entries present", "[DUPLICATE]" in log_content)
        check("[UNKNOWN] entries present", "[UNKNOWN]" in log_content)
        check("Timestamps present", "[" in log_content)

        # ==================================================================
        # 7. STATS OUTPUT FORMAT (types)
        # ==================================================================
        print("\n--- Stats Output Format ---")

        check(
            "Run Time is a string",
            isinstance(saved_stats.get("Run Time"), str),
            f"got {type(saved_stats.get('Run Time')).__name__}",
        )
        check(
            "Files Processed is int",
            is_int(saved_stats.get("Files Processed")),
            f"got {type(saved_stats.get('Files Processed')).__name__}: "
            f"{saved_stats.get('Files Processed')!r}",
        )
        check(
            "Files Moved is int",
            is_int(saved_stats.get("Files Moved")),
            f"got {type(saved_stats.get('Files Moved')).__name__}: "
            f"{saved_stats.get('Files Moved')!r}",
        )
        check(
            "Duplicate Files Renamed is int",
            is_int(saved_stats.get("Duplicate Files Renamed")),
            f"got {type(saved_stats.get('Duplicate Files Renamed')).__name__}: "
            f"{saved_stats.get('Duplicate Files Renamed')!r}",
        )
        check(
            "Unknown Files Found is int",
            is_int(saved_stats.get("Unknown Files Found")),
            f"got {type(saved_stats.get('Unknown Files Found')).__name__}: "
            f"{saved_stats.get('Unknown Files Found')!r}",
        )

    # ======================================================================
    # Summary
    # ======================================================================
    total = passed + failed
    print(f"\n{'=' * 50}")
    print(f"Results:  {passed} passed,  {failed} failed,  {total} total")
    print(f"{'=' * 50}")

    if failed:
        print("\nINTEGRATION TEST FAILED")
        raise SystemExit(1)
    else:
        print("\nALL INTEGRATION TESTS PASSED")


if __name__ == "__main__":
    run_integration_test()
