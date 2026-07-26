"""
Stash — Directory scanner.

Walks the project folder tree, skipping organizer-managed directories,
and yields file information for the organizer to process.
"""

import os
from typing import Generator, List, Tuple


class DirectoryScanner:
    """Scans a project folder and yields unprocessed files."""

    def __init__(self, project_folder: str, skip_folders: List[str]) -> None:
        self.project_folder = project_folder
        self.skip_folders = skip_folders

    def scan(self) -> Generator[Tuple[str, str, str], None, None]:
        """Yield (source_path, filename, extension) for every file found.

        Directories listed in *skip_folders* are pruned from the walk
        in-place so already-organized or protected folders are never
        revisited.
        """
        for current_path, foldernames, filenames in os.walk(self.project_folder):
            # Prune protected folders in-place so os.walk skips them entirely.
            foldernames[:] = [f for f in foldernames if f not in self.skip_folders]

            for filename in filenames:
                extension = os.path.splitext(filename)[1].lower()
                source_path = os.path.join(current_path, filename)
                yield source_path, filename, extension
