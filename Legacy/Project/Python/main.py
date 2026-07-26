"""
Stash — Intelligent File Organizer.

Entry point that validates the project folder, initializes the support
infrastructure, and runs the organizer.

Usage:
    python -m main
    python main.py
"""

import time
from pathlib import Path

from config.settings import LOG_DIR, PROJECT_FOLDER
from core.folder_manager import ensure_system_dirs, get_stats_file
from core.organizer import Organizer
from core.validator import PathValidator
from utils.logger import StashLogger
from utils.stats import StatsTracker


def main() -> None:
    """Run Stash on the configured project folder."""
    project_folder = str(PathValidator.validate_project_folder(PROJECT_FOLDER))
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
