"""
Stash — Application settings and configuration.

All user-configurable values live here. Nothing configurable should remain
hardcoded in other modules.
"""

from pathlib import Path
from typing import List

# -----------------------------------------------------------------------------
# Core Paths
# -----------------------------------------------------------------------------

# Project folder — the directory Stash will organize.
# This is a last-resort fallback when neither a CLI argument nor interactive
# input is provided. Set it to None to require a value at runtime.
PROJECT_FOLDER: Path | None = None

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
    "Legacy",  # Archived historical versions
    "config",  # Application package subdirectories
    "core",
    "utils",
    "tests",
]

# Root-level files that must never be scanned (application entry points and config).
ROOT_SKIP_FILES: List[str] = [
    "main.py",
    "__init__.py",
    "README.md",
    "requirements.txt",
]

# -----------------------------------------------------------------------------
# System Directories
# -----------------------------------------------------------------------------

SYSTEM_DIR: str = ".system"
LOG_DIR: str = ".system/logs"
STATS_DIR: str = ".system/stats"
STATS_FILE: str = ".system/stats/Statistics.json"
