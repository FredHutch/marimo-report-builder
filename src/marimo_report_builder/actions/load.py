from marimo_report_builder.action import Action
import marimo as mo
import json
from io import BytesIO


class Load(Action):
    name = "Load"

    def select_1(self):
        """
        Let the user provide a saved config file.
        """
        return mo.md("{config}").batch(
            config=mo.ui.file(
                label="Upload Report File (JSON)",
                kind="area"
            )
        )

    def select_2(self, config):

        return mo.md("{confirm}").batch(
            confirm=mo.ui.run_button(
                label="Load Report",
                disabled=len(config) == 0
            )
        )

    def execute(self, config, confirm):
        if len(config):
            config = json.load(BytesIO(config[0].contents))
        else:
            config = None
        if config and confirm:
            self._set_displays(config)
            return mo.md("Report has been loaded")
        else:
            return mo.md("")
