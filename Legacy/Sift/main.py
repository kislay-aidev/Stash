"""
Sift — Intelligent File Organizer.

Entry point that validates the project folder, initializes the support
infrastructure, and runs the organizer.

Usage:
    python -m Sift.main
    python Sift/main.py
"""

import sys
import time
from pathlib import Path

# Make the parent of the Sift package importable for direct script execution.
_parent = str(Path(__file__).resolve().parent.parent)
if _parent not in sys.path:
    sys.path.insert(0, _parent)

from Sift.config.settings import LOG_DIR, PROJECT_FOLDER
from Sift.core.folder_manager import ensure_system_dirs, get_stats_file
from Sift.core.organizer import Organizer
from Sift.core.validator import PathValidator
from Sift.utils.logger import SiftLogger
from Sift.utils.stats import StatsTracker


def main() -> None:
    """Run Sift on the configured project folder."""
    project_folder = str(PathValidator.validate_project_folder(PROJECT_FOLDER))
    start_time = time.time()

    # Prepare system directories first so the logger and stats have a home.
    ensure_system_dirs(project_folder)

    log_dir = Path(project_folder) / LOG_DIR
    logger = SiftLogger(str(log_dir), Path(project_folder))
    stats = StatsTracker()

    organizer = Organizer(project_folder, logger, stats)
    organizer.run()

    end_time = time.time()
    stats.finalize(start_time, end_time)
    stats.save(get_stats_file(project_folder))

    print("Stats written to Statistics.json")


if __name__ == "__main__":
    main()
