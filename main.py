"""
Stash — Intelligent File Organizer.

Entry point that resolves the target folder (CLI argument → interactive prompt
→ settings.py fallback), validates it, initializes the support infrastructure,
and runs the organizer.

Usage:
    python main.py "C:\path\to\folder\to\organize"
    python main.py          (interactive prompt)
    python -m main "C:\path\to\folder\to\organize"
"""

import sys
import time
from pathlib import Path

from config.settings import LOG_DIR, PROJECT_FOLDER
from core.folder_manager import ensure_system_dirs, get_stats_file
from core.organizer import Organizer
from core.validator import PathValidator
from utils.logger import StashLogger
from utils.stats import StatsTracker

STASH_ROOT = Path(__file__).resolve().parent


def _resolve_target_folder() -> str:
    """Resolve the target folder from CLI arg, interactive prompt, or fallback."""
    raw: str | None = None

    # 1. CLI argument
    if len(sys.argv) > 1:
        raw = sys.argv[1].strip()

    # 2. Interactive prompt
    if not raw:
        try:
            raw = input("Enter the full path of the folder to organize: ").strip()
        except (EOFError, KeyboardInterrupt):
            raw = ""

    # 3. Last-resort default from settings
    if not raw and PROJECT_FOLDER is not None:
        raw = str(PROJECT_FOLDER)

    if not raw:
        print(
            "No folder specified.\n"
            "Usage: python main.py \"C:\\path\\to\\folder\"",
            file=sys.stderr,
        )
        sys.exit(1)

    path = PathValidator.validate_project_folder(raw)

    # Safety guard: refuse to organise the Stash project itself.
    if path == STASH_ROOT:
        print(
            f"Error: refusing to organise the Stash project folder ({path}).\n"
            "Please specify a different folder.",
            file=sys.stderr,
        )
        sys.exit(1)

    return str(path)


def main() -> None:
    """Run Stash on the resolved target folder."""
    project_folder = _resolve_target_folder()
    start_time = time.time()

    # Prepare system directories first so the logger and stats have a home.
    ensure_system_dirs(project_folder)

    log_dir = Path(project_folder) / LOG_DIR
    logger = StashLogger(str(log_dir), Path(project_folder))
    stats = StatsTracker()

    organizer = Organizer(project_folder, logger, stats)
    organizer.run()

    end_time = time.time()
    stats.finalize(start_time, end_time)
    stats.save(get_stats_file(project_folder))

    print("Stats written to Statistics.json")


if __name__ == "__main__":
    main()
