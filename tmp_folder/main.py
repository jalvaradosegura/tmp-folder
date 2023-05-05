from __future__ import annotations

import functools
import sys
import tempfile
from pathlib import Path
from typing import Callable, TypeVar

if sys.version_info < (3, 10):  # pragma: no cover
    from typing_extensions import Concatenate, ParamSpec
else:
    from typing import Concatenate, ParamSpec

P = ParamSpec("P")
R = TypeVar("R")


def use_tmp_folder(func: Callable[Concatenate[Path, P], R]) -> Callable[P, R]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        with tempfile.TemporaryDirectory() as tmp_folder:
            return func(Path(tmp_folder), *args, **kwargs)

    return wrapper
