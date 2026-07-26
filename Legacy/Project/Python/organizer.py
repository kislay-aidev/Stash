"""
Stash — Organizer.

Orchestrates the full file-organization flow:
scan -> resolve destination -> create target folder -> move -> update stats.
"""

import os
from typing import Tuple

from config.extension_map import ALL_EXTENSIONS
from config.settings import SKIP_FOLDERS, UNKNOWN_FOLDER
from utils.logger import StashLogger
from utils.stats import StatsTracker
from core.mover import FileMover
from core.scanner import DirectoryScanner


class Organizer:
    """Top-level organizer that runs the complete Stash workflow."""

    def __init__(
        self,
        project_folder: str,
        logger: StashLogger,
        stats: StatsTracker,
    ) -> None:
        self.project_folder = project_folder
        self.logger = logger
        self.stats = stats

    def run(self) -> None:
        """Execute the full organization pipeline."""
        scanner = DirectoryScanner(self.project_folder, SKIP_FOLDERS)
        mover = FileMover(self.project_folder, self.logger, self.stats)

        for source_path, filename, extension in scanner.scan():
            if extension in ALL_EXTENSIONS:
                target_subfolder = ALL_EXTENSIONS[extension]
                is_unknown = False
            else:
                target_subfolder = UNKNOWN_FOLDER
                is_unknown = True

            # Track category counts for every scanned file, moved or not.
            category = ALL_EXTENSIONS.get(extension, UNKNOWN_FOLDER)
            self.stats.add_category_count(category)

            target_folder = os.path.join(self.project_folder, target_subfolder)
            os.makedirs(target_folder, exist_ok=True)
            destination_path = os.path.join(target_folder, filename)

            if source_path != destination_path and os.path.exists(source_path):
                mover.safe_move(source_path, destination_path, is_unknown)
