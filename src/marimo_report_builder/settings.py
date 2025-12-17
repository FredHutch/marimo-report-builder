from typing import Any, Optional
from pathlib import Path
import json


class Settings:
    _values: dict
    _cache: Path

    def __init__(self, cache_fp: Optional[str] = ".cache/settings.json"):
        self._cache = Path(cache_fp)
        if cache_fp and self._cache.exists():
            self._values = json.load(self._cache.open())
        else:
            self._values = dict()

    def get(self, kw: str, options=[], default=None):
        val = self._values.get(kw, default)
        if len(options) > 0:
            if val not in options:
                return default

        return val

    def set(self, kw: str, value: Any):
        self._values[kw] = value
        self._cache.parent.mkdir(parents=True, exist_ok=True)
        with self._cache.open(mode="w") as handle:
            json.dump(self._values, handle, indent=4)
