"""
Stash — Path utilities.

Small helpers for deriving relative paths and folder names used in
logging and validation.
"""

import os


def get_relative_dir(path: str, project_folder: str) -> str:
    """Return the directory portion of *path* relative to *project_folder*."""
    return os.path.dirname(os.path.relpath(path, project_folder))


def source_folder_name(source_path: str) -> str:
    """Return the immediate parent folder name of *source_path*."""
    return os.path.basename(os.path.dirname(source_path))


def is_within_project(path: str, project_folder: str) -> bool:
    """Return True if *path* is located inside *project_folder*."""
    try:
        rel = os.path.relpath(os.path.abspath(path), os.path.abspath(project_folder))
    except ValueError:
        return False
    return not (rel.startswith("..") or rel == os.path.pardir)
