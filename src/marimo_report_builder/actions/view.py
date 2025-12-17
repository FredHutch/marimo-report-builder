from marimo_report_builder.action import Action
import marimo as mo


class View(Action):
    name = "View"

    def execute(self):
        """
        Display all of the configured elements.
        """
        displays = self._get_displays()
        return mo.vstack([
            self.get_display(display["display_type"], ix).output()
            for ix, display in enumerate(displays)
        ])
