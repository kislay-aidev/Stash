"""
Stash — Centralized logging module.

Replaces scattered print/write statements with a single logger that
creates a timestamped log file and writes every operation with a timestamp.
"""

import os
from datetime import datetime
from pathlib import Path


class StashLogger:
    """Centralized logger for file organization operations."""

    def __init__(self, log_dir: str, project_folder: Path) -> None:
        """Initialize logger and create the log file.

        Args:
            log_dir: Directory where log files are stored.
            project_folder: Root project folder used for relative path
                calculations elsewhere in the application.
        """
        self.project_folder = project_folder
        os.makedirs(log_dir, exist_ok=True)

        log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")
        self.log_file = os.path.join(log_dir, log_filename)

    def log(self, message: str) -> None:
        """Write a timestamped log entry to the current log file.

        Args:
            message: The log message to record.
        """
        if not message:
            return
        with open(self.log_file, "a", encoding="utf-8") as log:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"[{timestamp}] {message}\n")
