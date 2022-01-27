import functools
import tempfile
from pathlib import Path
from typing import Callable, Concatenate, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def use_tmp_folder(func: Callable[Concatenate[Path, P], R]) -> Callable[P, R]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        with tempfile.TemporaryDirectory() as tmp_folder:
            result = func(Path(tmp_folder), *args, **kwargs)
        return result

    return wrapper
