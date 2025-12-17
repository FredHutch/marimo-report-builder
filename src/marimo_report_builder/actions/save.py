import json
import marimo as mo
from marimo_report_builder.action import Action
from datetime import datetime


class Save(Action):
    name = "Save"

    def execute(self):
        config = self._get_displays()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"report-builder-config-{timestamp}.json"
        return mo.vstack([
            mo.download(
                label=f"Download report ({len(config):,} {'display' if len(config) == 1 else 'displays'})",
                disabled=len(config) == 0,
                data=json.dumps(config),
                mimetype="application/json",
                filename=filename
            ),
            mo.json(config)
        ])
