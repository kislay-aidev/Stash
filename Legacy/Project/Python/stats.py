"""
Stash — Statistics tracking module.

Tracks run metrics and persists them to Statistics.json in the established
format:

    {
      "Run Time": "YYYY-MM-DD HH:MM:SS",
      "Execution Time (seconds)": 0.42,
      "Files Processed": 0,
      "Files Moved": 0,
      "Duplicate Files Renamed": 0,
      "Unknown Files Found": 0,
      "Category Counts": {}
    }
"""

import json
from datetime import datetime
from typing import Any, Dict


class StatsTracker:
    """Tracks per-run file organization statistics."""

    def __init__(self) -> None:
        """Initialize all counters to zero."""
        self.stats: Dict[str, Any] = {
            "Run Time": None,
            "Execution Time (seconds)": None,
            "Files Processed": 0,
            "Files Moved": 0,
            "Duplicate Files Renamed": 0,
            "Unknown Files Found": 0,
            "Category Counts": {},
        }
        self._category_counts: Dict[str, int] = {}

    def increment_processed(self) -> None:
        """Increment the files processed counter."""
        self.stats["Files Processed"] += 1

    def increment_moved(self) -> None:
        """Increment the files moved counter."""
        self.stats["Files Moved"] += 1

    def increment_duplicate(self) -> None:
        """Increment the duplicate files renamed counter."""
        self.stats["Duplicate Files Renamed"] += 1

    def increment_unknown(self) -> None:
        """Increment the unknown files found counter."""
        self.stats["Unknown Files Found"] += 1

    def add_category_count(self, category: str) -> None:
        """Track a file processed in the given category.

        Args:
            category: The target folder category (e.g., "Documents/PDFs").
        """
        self._category_counts[category] = self._category_counts.get(category, 0) + 1

    def finalize(self, start_time: float, end_time: float) -> Dict[str, Any]:
        """Finalize stats with timing information.

        Args:
            start_time: Start timestamp from time.time().
            end_time: End timestamp from time.time().

        Returns:
            The complete stats dictionary ready for JSON serialization.
        """
        self.stats["Run Time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.stats["Execution Time (seconds)"] = round(end_time - start_time, 2)
        self.stats["Category Counts"] = dict(self._category_counts)
        return self.stats

    def save(self, filepath: str) -> None:
        """Save statistics to a JSON file.

        Args:
            filepath: Path to the output JSON file.
        """
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.stats, f, indent=2)
