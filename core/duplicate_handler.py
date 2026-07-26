"""
Stash — Duplicate filename resolution.

Responsible for generating the next available duplicate name for a file
that already exists at its destination, e.g.:

    file.pdf -> file(1).pdf -> file(2).pdf -> ...

This logic exists in exactly one place in the codebase.
"""

import os


class DuplicateResolver:
    """Resolves filename conflicts using an incrementing numeric suffix."""

    def find_unique_name(self, destination_path: str) -> str:
        """Return the next available duplicate path for *destination_path*.

        The search loops without an arbitrary cap until a free filename is
        found, preserving the historical behavior of the project.

        Args:
            destination_path: The absolute path that already exists.

        Returns:
            A new absolute path where the duplicate can be moved.
        """
        base, ext = os.path.splitext(destination_path)
        nums = 1
        while True:
            candidate = f"{base}({nums}){ext}"
            if not os.path.exists(candidate):
                return candidate
            nums += 1
