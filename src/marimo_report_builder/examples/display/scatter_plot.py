from marimo_report_builder.display import ReportDisplay
import marimo as mo
import pandas as pd
import plotly.express as px


class ScatterPlot(ReportDisplay):
    name = "Scatter"
    description = "Just make a simple scatter plot"

    def input1(self):

        # Ask the user what table to use
        return mo.md("""
        - {table}
        - {field_sep}
        - {query}
        """).batch(
            table=self.data_backend.select_file(
                label="Select Data Table:",
                value=self.config.get("table", "")
            ),
            field_sep=mo.ui.dropdown(
                label="Field Separator",
                options=[",", "\t"],
                value=self.config.get("field_sep", ",")
            ),
            query=mo.ui.text(
                label="Query (optional):",
                value=self.config.get("query", "")
            )
        )

    def _get_table(self, table: str, field_sep: str, query: str, **kwargs) -> pd.DataFrame:
        df = self.data_backend.read_csv(table, sep=field_sep)

        if len(query):
            df = df.query(query)

        return df

    def _make_dropdown_options(self, kw: str, label: str, df: pd.DataFrame):
        """Use the value from the config, if it is one of the options in the DataFrame"""

        config_value = self.config.get(kw)
        if config_value in df.columns.values:
            value = config_value
        else:
            value = None

        return mo.ui.dropdown(label=label, options=df.columns.values, value=value, searchable=True)

    def input2(self, table: str, field_sep: str, query: str):
        df = self._get_table(table, field_sep, query)

        return mo.md(
            """
            - {x}
            - {y}
            - {color}
            - {facet_row}
            - {facet_col}
            - {height}
            - {show_table}
            """).batch(
                x=self._make_dropdown_options("x", "X-Axis:", df),
                y=self._make_dropdown_options("y", "Y-Axis:", df),
                color=self._make_dropdown_options("color", "Color:", df),
                facet_row=self._make_dropdown_options("facet_row", "Facet Row:", df),
                facet_col=self._make_dropdown_options("facet_col", "Facet Col:", df),
                height=mo.ui.number(label="Figure Height:", value=self.config.get("height", 600)),
                show_table=mo.ui.checkbox(label="Show Table", value=self.config.get("show_table", True))
            )

    def output(self):
        df = self._get_table(**self.config)

        plot_kws = ["x", "y", "color", "facet_row", "facet_col", "height"]

        fig = px.scatter(
            data_frame=df,
            template="simple_white",
            **{
                kw: val
                for kw, val in self.config.items()
                if kw in plot_kws
            }
        )

        if self.config.get("show_table", False):
            return mo.vstack([
                df,
                fig
            ])
        else:
            return fig
