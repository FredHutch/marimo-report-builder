from marimo_report_builder.display import ReportDisplay
import marimo as mo


class Markdown(ReportDisplay):
    name = "Text"
    description = "Render a block of text using markdown syntax"

    def input1(self):

        return mo.md("""
        - {text}
        """).batch(
            text=mo.ui.text_area(
                label="Text:",
                value=self.config.get("text", "")
            )
        )

    def output(self):
        return mo.md(self.config.get("text", ""))
