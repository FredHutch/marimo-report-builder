import marimo as mo
import pandas as pd
from functools import lru_cache


class DataBackend:

    def select_file(self, label="Select File:", **kwargs):

        return mo.ui.text(
            label=label,
            **kwargs
        )

    def read_csv(self, uri: str, **kwargs) -> pd.DataFrame:
        return pd_read_csv(uri, **kwargs)


@lru_cache
def pd_read_csv(uri, **kwargs):
    with mo.status.spinner(f"Reading {uri}"):
        return pd.read_csv(uri, **kwargs)