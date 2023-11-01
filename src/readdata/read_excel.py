from pathlib import Path
from typing import Callable

import pandas as pd

cacheDir: Path | None = None


def _initialize_cache_directory():
    global cacheDir
    if cacheDir is None:
        cacheDir = Path("data/cache")
        cacheDir.mkdir(parents=True, exist_ok=True)


def read_excel(path: Path, set: str, sheet_name: str) -> pd.DataFrame:
    _initialize_cache_directory()
    cached_file_path = cacheDir / set / path.stem / (sheet_name + ".pkl")
    name = str(path) + " sheet " + sheet_name

    if not cached_file_path.exists():
        print("Reading excel " + name)
        df = pd.read_excel(path.as_posix(), sheet_name)
        print("Pickling excel " + name)
        cached_file_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_pickle(cached_file_path.as_posix())

    print("Reading " + name)
    return pd.read_pickle(cached_file_path.as_posix())
