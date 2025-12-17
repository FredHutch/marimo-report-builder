from typing import Optional
import marimo as mo
from marimo_report_builder.data_backend.data_backend import DataBackend


class ReportDisplay:
    # Attributes defined by subclasses
    name: str
    description: str

    # Attributes populated at initiation
    config: dict
    data_backend: DataBackend

    def __init__(self, data_backend: DataBackend, config: dict):
        # Set up the data backend
        self.data_backend = data_backend
        # Set up the configuration.
        # This is used to populate the default settings of the input elements.
        # It is also used to drive the display of this element.
        self.config = config

    def input1(self):
        return mo.md("").batch()

    def input2(self, **kwargs):
        return mo.md("").batch()

    def output(self):
        raise NotImplementedError("Subclasses should implement this method")
