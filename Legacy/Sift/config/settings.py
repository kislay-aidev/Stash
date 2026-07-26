"""
Sift — Application settings and configuration.

All user-configurable values live here. Nothing configurable should remain
hardcoded in other modules.
"""

from pathlib import Path
from typing import List

# -----------------------------------------------------------------------------
# Core Paths
# -----------------------------------------------------------------------------

# Project folder — the directory Sift will organize.
PROJECT_FOLDER: Path = Path(r"C:\Users\kisla\Desktop\FileOrgProject")

# Folder for files whose extension is not mapped anywhere else.
UNKNOWN_FOLDER: str = "Others/Unknown"

# -----------------------------------------------------------------------------
# Traversal Protection
# -----------------------------------------------------------------------------

# Directory names that must never be scanned, preventing recursive
# re-processing of already-organized files and project internals.
SKIP_FOLDERS: List[str] = [
    "Documents",
    "Images",
    "Videos",
    "Music",
    "Archives",
    "Project",
    "WebPages",
    "Others",
    "GIFs",
    ".system",
    "Sift",  # Application package itself
]

# -----------------------------------------------------------------------------
# System Directories
# -----------------------------------------------------------------------------

SYSTEM_DIR: str = ".system"
LOG_DIR: str = ".system/logs"
STATS_DIR: str = ".system/stats"
STATS_FILE: str = ".system/stats/Statistics.json"
