import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    ### Report Builder
    """)
    return


@app.cell
def _():
    from marimo_report_builder.action_menu import ActionMenu
    from marimo_report_builder.catalog import DisplayCatalog
    from marimo_report_builder.data_backend import DataBackend
    return ActionMenu, DataBackend, DisplayCatalog


@app.cell
def _():
    # Set up an object that is used to preserve state without triggering reruns
    from marimo_report_builder.settings import Settings
    settings = Settings()
    return (settings,)


@app.cell
def _(DisplayCatalog):
    # Set up the types of displays that are available
    # Note that this will likely be populated with different options for other types of reports
    from marimo_report_builder.examples.display.scatter_plot import ScatterPlot
    from marimo_report_builder.examples.display.markdown import Markdown
    catalog = DisplayCatalog([ScatterPlot, Markdown])
    return (catalog,)


@app.cell
def _(DataBackend):
    # Set up a generic data backend
    data_backend = DataBackend()
    return (data_backend,)


@app.cell
def _(ActionMenu):
    # Set up the action menu
    action_menu = ActionMenu()
    return (action_menu,)


@app.cell
def _(action_menu, settings):
    menu_selection = action_menu.select(settings)
    menu_selection
    return (menu_selection,)


@app.cell
def _(action_menu, catalog, data_backend, menu_selection, settings):
    # Get the action that was selected
    action = action_menu.get(menu_selection.value, catalog, settings, data_backend)
    return (action,)


@app.cell
def _(action):
    # Each action may have nested opportunities to provide input
    action_selection_1 = action.select_1()
    action_selection_1
    return (action_selection_1,)


@app.cell
def _(action, action_selection_1):
    action_selection_2 = action.select_2(**action_selection_1.value)
    action_selection_2
    return (action_selection_2,)


@app.cell
def _(action, action_selection_1, action_selection_2):
    action_selection_3 = action.select_3(**action_selection_1.value, **action_selection_2.value)
    action_selection_3
    return (action_selection_3,)


@app.cell
def _(action, action_selection_1, action_selection_2, action_selection_3):
    action_selection_4 = action.select_4(
        **action_selection_1.value,
        **action_selection_2.value,
        **action_selection_3.value
    )
    action_selection_4
    return (action_selection_4,)


@app.cell
def _(
    action,
    action_selection_1,
    action_selection_2,
    action_selection_3,
    action_selection_4,
):
    action.execute(
        **action_selection_1.value,
        **action_selection_2.value,
        **action_selection_3.value,
        **action_selection_4.value
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
