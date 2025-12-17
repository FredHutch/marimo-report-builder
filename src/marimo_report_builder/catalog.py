from marimo_report_builder.display import ReportDisplay
import marimo as mo
from typing import Optional, List


class DisplayCatalog:
    """
    A class for managing a catalog of displays.
    """
    displays: list[ReportDisplay]

    def __init__(self, displays: List[ReportDisplay]):
        self.displays = displays

    @property
    def display_names(self) -> List[str]:
        return [display.name for display in self.displays]

    def get_display_by_name(self, name: str) -> ReportDisplay:
        for display in self.displays:
            if display.name == name:
                return display
        raise ValueError(f"Could not find display with name {name}")
