from marimo_report_builder.display import ReportDisplay
from marimo_report_builder.settings import Settings
from marimo_report_builder.catalog import DisplayCatalog
from marimo_report_builder.data_backend import DataBackend
import marimo as mo
from typing import List


class Action:
    name: str
    _catalog: DisplayCatalog
    _settings: Settings
    _data_backend: DataBackend

    def __init__(self, catalog: DisplayCatalog, settings: Settings, data_backend: DataBackend):
        self._catalog = catalog
        self._settings = settings
        self._data_backend = data_backend

    def select_1(self):
        return mo.md("").batch()

    def select_2(self, **kwargs):
        return mo.md("").batch()

    def select_3(self, **kwargs):
        return mo.md("").batch()

    def select_4(self, **kwargs):
        return mo.md("").batch()

    def execute(self, **kwargs):
        raise NotImplementedError("Subclasses should implement this method")

    def _get_displays(self) -> List[dict]:
        return self._settings.get("displays", default=list())

    def _set_displays(self, displays: List[dict]):
        self._settings.set("displays", displays)

    def _get_display(self, edit_ix: int):
        return self._get_displays()[edit_ix]

    def _set_display(self, edit_ix: int, display_type: str, config: dict):
        displays = self._get_displays()
        displays[edit_ix]["display_type"] = display_type
        displays[edit_ix]["config"] = config
        self._set_displays(displays)

    def get_display(self, display_type: str, edit_ix: int) -> ReportDisplay:

        # Get the display of the selected type
        display_cls = self._catalog.get_display_by_name(display_type)

        # Get the config defined in the settings, if any
        config = self._get_display(edit_ix)["config"]

        # Build the object using the data backend and configuration provided
        return display_cls(
            data_backend=self._data_backend,
            config=config
        )