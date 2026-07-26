"""
Stash — General helpers.

Small utility functions that do not belong to a more specific module.
"""

from typing import Iterable, Optional


def first_matching(prefix: str, candidates: Iterable[str]) -> Optional[str]:
    """Return the first candidate that starts with *prefix*, or None."""
    for candidate in candidates:
        if candidate.startswith(prefix):
            return candidate
    return None
