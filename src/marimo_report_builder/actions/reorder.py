from time import sleep
from marimo_report_builder.action import Action
import marimo as mo


class Reorder(Action):
    name = "Reorder"

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
        return mo.md(
            f"""
            There are a total of {len(displays):,} displays in the current report.\n\n
            """ + """
            - {edit_ix}
            """).batch(
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
        """Let the user pick the operation to perform."""

        displays = self._get_displays()
        if len(displays) > 1:
            options = ["Duplicate", "Move", "Delete"]
        else:
            options = ["Duplicate", "Delete"]

        return mo.md(" - {operation}").batch(
            operation=mo.ui.dropdown(
                label="Operation:",
                options=options,
                value=self._settings.get("reorder_operation", options=options, default="Duplicate"),
                on_change=lambda v: self._settings.set("reorder_operation", v)
            )
        )

    def select_3(self, edit_ix: int, operation: str):
        """Follow up questions."""

        if operation == "Move":
            n_displays = len(self._get_displays())
            options = [f"Position {i} / {n_displays:,}" for i in range(n_displays)] + ["End"]

            return mo.md(" - {move_to}").batch(
                move_to=mo.ui.dropdown(
                    label="Move To:",
                    options=options,
                    value=self._settings.get("reorder_move_to", options=options, default="End")
                )
            )
        else:
            return mo.md("").batch()

    def select_4(self, **kwargs):
        """Confirm button"""
        self._settings.set("reorder_ready_to_run", True)

        return mo.md("{confirm}").batch(
            confirm=mo.ui.run_button(
                label="Confirm"
            )
        )

    def execute(self, edit_ix: int, operation: str, confirm: bool, **kwargs):
        print('here1')
        if not self._settings.get("reorder_ready_to_run", options=[True, False], default=False):
            return
        if confirm:
            displays = self._get_displays()

            if operation == "Move":
                move_to = kwargs["move_to"]
                msg = f"Moving display from {edit_ix} to {move_to}"
                if move_to > edit_ix:
                    move_to -= 1
                displays.insert(move_to, displays.pop(edit_ix))
            elif operation == "Delete":
                displays.pop(edit_ix)
                msg = f"Deleting item {edit_ix:,}"
            elif operation == "Duplicate":
                displays.insert(edit_ix, displays[edit_ix].copy())
                msg = f"Duplicating item {edit_ix:,}"
            else:
                raise Exception(f"Unsupported operation '{operation}")

            self._set_displays(displays)

            with mo.status.spinner(msg):
                sleep(1)
            self._settings.set("action_menu_selection", "View")
            self._rerun()
