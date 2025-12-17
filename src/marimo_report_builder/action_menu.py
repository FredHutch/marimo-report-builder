from marimo_report_builder.action import Action
from marimo_report_builder.actions import all_actions
from marimo_report_builder.settings import Settings
from marimo_report_builder.catalog import DisplayCatalog
from marimo_report_builder.data_backend import DataBackend
from typing import List, Optional
import marimo as mo


class ActionMenu:
    """
    The menu element used to select and execute actions.
    """

    actions: List[Action]

    def __init__(self, actions: Optional[List[Action]] = all_actions):
        self.actions = actions
        assert len(self.actions) > 0, "Must provide action(s)"

        # Make sure there are no duplicate names
        self._assert_action_names_are_unique()

    def _assert_action_names_are_unique(self):
        seen_names = set()
        duplicate_names = set()

        for action in self.actions:
            name = getattr(action, "name", None)
            assert name is not None, "All actions must have a name attribute."
            if name in seen_names:
                duplicate_names.add(name)
            else:
                seen_names.add(name)

            assert len(duplicate_names) == 0, f"Cannot have duplicated action names: {', '.join(list(duplicate_names))}"

    def select(self, settings: Settings, label="Select Action:"):
        """
        Return the marimo menu used to select an action.
        """

        options = [action.name for action in self.actions]
        return mo.ui.dropdown(
            label=label,
            options=options,
            value=settings.get("action_menu_selection", options=options, default=self.actions[0].name),
            on_change=lambda v: settings.set("action_menu_selection", v),
            searchable=True
        )

    def get(self, selection: str, catalog: DisplayCatalog, settings: Settings, data_backend: DataBackend) -> Action:
        """
        Return the action that was selected.
        """
        action_cls = next(action for action in self.actions if action.name == selection)
        return action_cls(catalog, settings, data_backend)
