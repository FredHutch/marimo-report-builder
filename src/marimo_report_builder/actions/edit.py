from marimo_report_builder.action import Action
import marimo as mo


class Edit(Action):
    name = "Edit"

    def select_1(self):
        """
        Ask the user which display element to edit.
        """

        displays = self._get_displays()

        # If there are no displays, set up a blank one
        if len(displays) == 0:
            displays.append(
                dict(
                    display_type=self._catalog.displays[0].name,
                    config={}
                )
            )
            self._set_displays(displays)

        # Get the index of the display to select
        return mo.md("- {edit_ix}").batch(
            edit_ix=mo.ui.number(
                label="Select Display Element (0-indexed):",
                start=0,
                step=1,
                stop=len(displays)-1,
                value=self._settings.get("edit_ix", options=list(range(len(displays))), default=0),
                on_change=lambda v: self._settings.set("edit_ix", v)
            )
        )

    def select_2(self, edit_ix: int):
        """Let the user pick the type of display."""

        display_type = self._get_display(edit_ix)["display_type"]
        if display_type not in self._catalog.display_names:
            raise ValueError(f"No entry in the display catalog for '{display_type}'")

        return mo.md(" - {display_type}").batch(
            display_type=mo.ui.dropdown(
                label="Display Type:",
                options=self._catalog.display_names,
                value=display_type
            )
        )

    def select_3(self, edit_ix: int, display_type: str):
        """Return the first input element for the display."""

        display = self.get_display(display_type, edit_ix)
        return display.input1()

    def select_4(self, edit_ix: int, display_type: str, **kwargs):
        """Return the second input element for the display."""

        display = self.get_display(display_type, edit_ix)
        return display.input2(**kwargs)

    def execute(self, edit_ix: int, display_type: str, **config):
        # Save the updated config
        self._set_display(edit_ix, display_type, config)

        # Get the display object
        display = self.get_display(display_type, edit_ix)

        # Show it
        return display.output()
