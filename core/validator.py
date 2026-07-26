"""
Stash — Path validation.

Ensures the project folder exists, is accessible, and is safe to operate on
before any file operations begin.
"""

from pathlib import Path


class PathValidator:
    """Validates paths required by the Stash pipeline."""

    @staticmethod
    def validate_project_folder(project_folder: str | Path) -> Path:
        """Validate that *project_folder* is an existing directory.

        Args:
            project_folder: The root directory to organize.

        Returns:
            The resolved, absolute path.

        Raises:
            FileNotFoundError: If the path does not exist.
            NotADirectoryError: If the path is not a directory.
        """
        path = Path(project_folder).resolve()
        if not path.exists():
            raise FileNotFoundError(f"Project folder does not exist: {path}")
        if not path.is_dir():
            raise NotADirectoryError(f"Project path is not a directory: {path}")
        return path
