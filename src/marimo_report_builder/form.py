import marimo as mo


class ReportForm:
    """
    A class for building a form to capture inputs for an element of a report.
    """
    config: dict

    def __init__(self, config: dict):
        self.config = config

    def render(self, **kwargs):
        """
        Render a form based on the kwargs provided.
        Each key:value pair in the kwargs is used to build a form input element.
        Each value must be a dictionary with the "display_type" key specifying the type of input element,
        which maps to the input_* functions defined below.
        """
        return mo.md("\n".join([
            " - {" + k + "}" for k in kwargs.keys()
        ])).batch(**{
            k: self.get_input_element(key=k, **v)
            for k, v in kwargs.items()
        })

    def get_input_element(self, display_type: str, **kwargs):
        input_method = getattr(self, f"input_{display_type}", None)
        if input_method is None:
            raise ValueError(f"Input type '{display_type}' is not supported.")
        return input_method(**kwargs)

    # -------------------------------------------------------------------------
    # Selection Inputs
    # -------------------------------------------------------------------------

    def input_dropdown(
        self,
        key: str,
        options: list,
        label: str = "",
        searchable: bool = True,
        **kwargs
    ):
        """Single-select dropdown menu."""
        return mo.ui.dropdown(
            label=label,
            options=options,
            searchable=searchable,
            value=self.config.get(key, None),
            on_change=lambda v: self.config.__setitem__(key, v),
            **kwargs
        )

    def input_multiselect(
        self,
        key: str,
        options: list,
        label: str = "",
        max_selections: int = None,
        **kwargs
    ):
        """Multi-select dropdown allowing multiple choices."""
        return mo.ui.multiselect(
            label=label,
            options=options,
            max_selections=max_selections,
            value=self.config.get(key, []),
            on_change=lambda v: self.config.__setitem__(key, v),
            **kwargs
        )

    def input_radio(
        self,
        key: str,
        options: list,
        label: str = "",
        inline: bool = False,
        **kwargs
    ):
        """Radio button group for single selection."""
        return mo.ui.radio(
            label=label,
            options=options,
            inline=inline,
            value=self.config.get(key, None),
            on_change=lambda v: self.config.__setitem__(key, v),
            **kwargs
        )

    # -------------------------------------------------------------------------
    # Boolean Inputs
    # -------------------------------------------------------------------------

    def input_checkbox(
        self,
        key: str,
        label: str = "",
        **kwargs
    ):
        """Boolean checkbox input."""
        return mo.ui.checkbox(
            label=label,
            value=self.config.get(key, False),
            on_change=lambda v: self.config.__setitem__(key, v),
            **kwargs
        )

    def input_switch(
        self,
        key: str,
        label: str = "",
        **kwargs
    ):
        """Boolean toggle switch input."""
        return mo.ui.switch(
            label=label,
            value=self.config.get(key, False),
            on_change=lambda v: self.config.__setitem__(key, v),
            **kwargs
        )

    # -------------------------------------------------------------------------
    # Numeric Inputs
    # -------------------------------------------------------------------------

    def input_number(
        self,
        key: str,
        label: str = "",
        start: float = None,
        stop: float = None,
        step: float = None,
        **kwargs
    ):
        """Numeric input field with optional bounds."""
        return mo.ui.number(
            label=label,
            start=start,
            stop=stop,
            step=step,
            value=self.config.get(key, start),
            on_change=lambda v: self.config.__setitem__(key, v),
            **kwargs
        )

    def input_slider(
        self,
        key: str,
        label: str = "",
        start: float = 0,
        stop: float = 100,
        step: float = 1,
        show_value: bool = True,
        **kwargs
    ):
        """Slider for selecting a numeric value within a range."""
        return mo.ui.slider(
            label=label,
            start=start,
            stop=stop,
            step=step,
            show_value=show_value,
            value=self.config.get(key, start),
            on_change=lambda v: self.config.__setitem__(key, v),
            **kwargs
        )

    def input_range_slider(
        self,
        key: str,
        label: str = "",
        start: float = 0,
        stop: float = 100,
        step: float = 1,
        show_value: bool = True,
        **kwargs
    ):
        """Range slider for selecting a numeric range (two values)."""
        return mo.ui.range_slider(
            label=label,
            start=start,
            stop=stop,
            step=step,
            show_value=show_value,
            value=self.config.get(key, [start, stop]),
            on_change=lambda v: self.config.__setitem__(key, v),
            **kwargs
        )

    # -------------------------------------------------------------------------
    # Text Inputs
    # -------------------------------------------------------------------------

    def input_text(
        self,
        key: str,
        label: str = "",
        placeholder: str = "",
        max_length: int = None,
        **kwargs
    ):
        """Single-line text input field."""
        return mo.ui.text(
            label=label,
            placeholder=placeholder,
            max_length=max_length,
            value=self.config.get(key, ""),
            on_change=lambda v: self.config.__setitem__(key, v),
            **kwargs
        )

    def input_text_area(
        self,
        key: str,
        label: str = "",
        placeholder: str = "",
        max_length: int = None,
        rows: int = None,
        **kwargs
    ):
        """Multi-line text input area."""
        return mo.ui.text_area(
            label=label,
            placeholder=placeholder,
            max_length=max_length,
            rows=rows,
            value=self.config.get(key, ""),
            on_change=lambda v: self.config.__setitem__(key, v),
            **kwargs
        )

    # -------------------------------------------------------------------------
    # Date/Time Inputs
    # -------------------------------------------------------------------------

    def input_date(
        self,
        key: str,
        label: str = "",
        start=None,
        stop=None,
        **kwargs
    ):
        """Date picker input."""
        return mo.ui.date(
            label=label,
            start=start,
            stop=stop,
            value=self.config.get(key, None),
            on_change=lambda v: self.config.__setitem__(key, v),
            **kwargs
        )

    def input_date_range(
        self,
        key: str,
        label: str = "",
        start=None,
        stop=None,
        **kwargs
    ):
        """Date range picker for selecting a start and end date."""
        return mo.ui.date_range(
            label=label,
            start=start,
            stop=stop,
            value=self.config.get(key, None),
            on_change=lambda v: self.config.__setitem__(key, v),
            **kwargs
        )

    def input_datetime(
        self,
        key: str,
        label: str = "",
        start=None,
        stop=None,
        **kwargs
    ):
        """Date and time picker input."""
        return mo.ui.datetime(
            label=label,
            start=start,
            stop=stop,
            value=self.config.get(key, None),
            on_change=lambda v: self.config.__setitem__(key, v),
            **kwargs
        )

    # -------------------------------------------------------------------------
    # File Inputs
    # -------------------------------------------------------------------------

    def input_file(
        self,
        key: str,
        label: str = "",
        filetypes: list = None,
        multiple: bool = False,
        **kwargs
    ):
        """File upload input."""
        return mo.ui.file(
            label=label,
            filetypes=filetypes,
            multiple=multiple,
            on_change=lambda v: self.config.__setitem__(key, v),
            **kwargs
        )

    def input_file_browser(
        self,
        key: str,
        label: str = "",
        initial_path: str = "",
        filetypes: list = None,
        multiple: bool = True,
        **kwargs
    ):
        """File browser for selecting files from the filesystem."""
        return mo.ui.file_browser(
            label=label,
            initial_path=initial_path,
            filetypes=filetypes,
            multiple=multiple,
            on_change=lambda v: self.config.__setitem__(key, v),
            **kwargs
        )

    # -------------------------------------------------------------------------
    # Interactive Inputs
    # -------------------------------------------------------------------------

    def input_button(
        self,
        key: str,
        label: str = "",
        kind: str = "neutral",
        **kwargs
    ):
        """Button input that tracks click count."""
        return mo.ui.button(
            label=label,
            kind=kind,
            on_change=lambda v: self.config.__setitem__(key, v),
            **kwargs
        )

    def input_code_editor(
        self,
        key: str,
        label: str = "",
        language: str = "python",
        **kwargs
    ):
        """Code editor input with syntax highlighting."""
        return mo.ui.code_editor(
            label=label,
            language=language,
            value=self.config.get(key, ""),
            on_change=lambda v: self.config.__setitem__(key, v),
            **kwargs
        )
