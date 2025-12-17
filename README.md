# marimo-report-builder
Generic framework for building reports from a series of customized visualization elements, using marimo for reactivity

### Organization

The functionality for the report builder is broken up into:

1. The `marimo-report-builder` Python library which has generic functionality for buiding reports.
2. The `report.py` marimo app which builds an example report using that library.

Note that the example report only includes the report elements defined in the
`src/marimo_report_builder/examples/display/` folder.

### Building Your Own

To build your own report using this framework, follow the example shown here to define
a set of display elements which are appropriate to your needs.
Modify the following block of code from `report.py` to add those custom visualization elements:

```{python}
from marimo_report_builder.examples.display.scatter_plot import ScatterPlot
catalog = DisplayCatalog([ScatterPlot])
```

You may also need to use a different type of `DataBackend`, depending on where you want to
source input data from.

### Development

To develop the base `marimo-report-builder` library, make sure to have `uv` available in your
environment.

The `report.py` can be run interactively with `bash edit.sh` or:

```{shell}
uv run marimo edit report.py
```

Note that this notebook has been set up such that modifications to any imported library
will automatically trigger a reload and rerun of any dependent cells.

With this setup, the library defining all display elements can be installed in development
mode (`pip install -e`) and then tested interactively using the marimo interface.
