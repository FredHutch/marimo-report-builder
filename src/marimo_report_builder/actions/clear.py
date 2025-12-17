from marimo_report_builder.action import Action
from marimo_report_builder.catalog import DisplayCatalog
import marimo as mo


class Clear(Action):
    name = "Clear"

    def select_1(self):

        n_displays = len(self._get_displays())

        return mo.md("{confirm}").batch(
            confirm=mo.ui.run_button(
                label="Clear Displays",
                disabled=n_displays == 0
            )
        )

    def execute(self, confirm):
        n_displays = len(self._get_displays())

        if n_displays == 0:
            return mo.md("The report does not have any displays")
        else:
            if confirm:
                self._set_displays([])
                return mo.md("Displays have been cleared")
            else:
                return mo.md(f"Are you sure you want to clear {n_displays:,} {'displays' if n_displays > 1 else 'display'}?")
