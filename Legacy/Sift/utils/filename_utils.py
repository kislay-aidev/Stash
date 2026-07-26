"""
Sift — Filename utilities.

Helpers for splitting and constructing filenames.
"""

import os
from typing import Tuple


def split_filename(path: str) -> Tuple[str, str]:
    """Split *path* into (base, extension) the same way os.path.splitext does."""
    return os.path.splitext(path)
