from __future__ import annotations

import functools
import sys
import tempfile
from pathlib import Path

if sys.version_info < (3, 8):
    from typing import Callable, Concatenate, ParamSpec, TypeVar
else:
    from typing_extensions import Callable, Concatenate, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def use_tmp_folder(func: Callable[Concatenate[Path, P], R]) -> Callable[P, R]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        with tempfile.TemporaryDirectory() as tmp_folder:
            return func(Path(tmp_folder), *args, **kwargs)

    return wrapper
