"""
Sift — File mover with safe duplicate handling.

Moves files to their target destinations and delegates duplicate naming
to DuplicateResolver. Every operation is logged via SiftLogger and tracked
via StatsTracker.
"""

import os
import shutil

from ..utils.filename_utils import split_filename
from ..utils.logger import SiftLogger
from ..utils.path_utils import get_relative_dir, source_folder_name
from ..utils.stats import StatsTracker
from .duplicate_handler import DuplicateResolver


class FileMover:
    """Handles safe file moves with duplicate detection and logging."""

    def __init__(
        self,
        project_folder: str,
        logger: SiftLogger,
        stats: StatsTracker,
    ) -> None:
        self.project_folder = project_folder
        self.logger = logger
        self.stats = stats
        self.resolver = DuplicateResolver()

    def safe_move(
        self,
        source_path: str,
        destination_path: str,
        is_unknown: bool = False,
    ) -> None:
        """Move *source_path* to *destination_path*, handling duplicates.

        Args:
            source_path: Absolute path of the file to move.
            destination_path: Absolute path of the intended destination.
            is_unknown: True when the extension is not in the mapping.
        """
        log_message = ""

        source_name = os.path.basename(source_path)
        source_folder = source_folder_name(source_path)
        destination_folder = get_relative_dir(destination_path, self.project_folder)
        base, ext = split_filename(destination_path)

        try:
            if os.path.exists(destination_path):
                # Duplicate: generate the next available name like file(1).ext
                unique_name = self.resolver.find_unique_name(destination_path)
                shutil.move(source_path, unique_name)

                self.stats.increment_duplicate()
                self.stats.increment_moved()
                self.stats.increment_processed()

                print(f"Moved duplicate as: {unique_name}")
                log_message = (
                    f"[DUPLICATE] "
                    f"{source_name} -> {os.path.basename(unique_name)} | "
                    f"{source_folder} -> "
                    f"{destination_folder}"
                )
            else:
                shutil.move(source_path, destination_path)

                self.stats.increment_moved()
                self.stats.increment_processed()

                if is_unknown:
                    self.stats.increment_unknown()
                    log_message = (
                        f"[UNKNOWN] {source_name} | "
                        f"{source_folder} -> "
                        f"{destination_folder}"
                    )
                else:
                    print(f"Moved: {destination_path}")
                    log_message = (
                        f"[MOVED] {source_name} | "
                        f"{source_folder} -> "
                        f"{destination_folder}"
                    )

        except Exception as exc:
            self.stats.increment_processed()
            log_message = (
                f"[ERROR] {source_name}"
                f"from {source_folder}"
                f"to {destination_folder} | {str(exc)}"
            )
            print(log_message)

        self.logger.log(log_message)
