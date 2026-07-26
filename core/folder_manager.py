"""
Stash — Folder management utilities.

Handles creation of system directories and path resolution for logs
and statistics files.
"""

import os
from datetime import datetime

from config.settings import LOG_DIR, STATS_DIR


def ensure_system_dirs(project_folder: str) -> None:
    """Create .system/logs and .system/stats directories."""
    os.makedirs(os.path.join(project_folder, LOG_DIR), exist_ok=True)
    os.makedirs(os.path.join(project_folder, STATS_DIR), exist_ok=True)


def get_log_file(project_folder: str) -> str:
    """Return path to a timestamped log file inside .system/logs."""
    return os.path.join(
        project_folder,
        LOG_DIR,
        datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log"),
    )


def get_stats_file(project_folder: str) -> str:
    """Return path to Statistics.json inside .system/stats."""
    return os.path.join(project_folder, STATS_DIR, "Statistics.json")
