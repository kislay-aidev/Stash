"""
Sift — General helpers.

Small utility functions that do not belong to a more specific module.
"""

from typing import Iterable


def first_matching(prefix: str, candidates: Iterable[str]) -> str | None:
    """Return the first candidate that starts with *prefix*, or None."""
    for candidate in candidates:
        if candidate.startswith(prefix):
            return candidate
    return None
