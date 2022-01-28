# Welcome to tmp-folder

## Installation

Install from PyPI:

```
pip install tmp-folder
```

## Usage

Let's create a `main.py` file with a function that requires a temporary folder during its execution:

``` python hl_lines="4-9"
from pathlib import Path


def this_func_create_a_tmp_file_and_return_its_path(tmp_folder: Path) -> Path:
    tmp_file_path = tmp_folder / "tmp_file.txt"
    with open(tmp_file_path, "w") as file:
        file.write("Hello World")

    return tmp_file_path
```

The type hint is totally optional:

```python hl_lines="1 4"
from pathlib import Path


def this_func_create_a_tmp_file_and_return_its_path(tmp_folder: Path) -> Path:
    tmp_file_path = tmp_folder / "tmp_file.txt"
    with open(tmp_file_path, "w") as file:
        file.write("Hello World")

    return tmp_file_path
```

But is just to make clear that the function expects a Path folder, to store files in it.

Use our decorator (that extends python `tempfile.TemporaryDirectory`) to give the function the superpower to use a temporary folder while it is being executed and after that `tmp-folder` will take care of the clean up:

```python hl_lines="3 6"
from pathlib import Path

from tmp_folder import use_tmp_folder


@use_tmp_folder  # this decorator does the magic
def this_func_create_a_tmp_file_and_return_its_path(tmp_folder: Path) -> Path:
    tmp_file_path = tmp_folder / "tmp_file.txt"
    with open(tmp_file_path, "w") as file:
        file.write("Hello World")

    return tmp_file_path
```

Add the execution of function and add assert statements double check the magic of `tmp-folder`:

```python hl_lines="12 17-21"
from pathlib import Path

from tmp_folder.main import use_tmp_folder


@use_tmp_folder  # this decorator does the magic
def this_func_create_a_tmp_file_and_return_its_path(tmp_folder: Path) -> Path:
    tmp_file_path = tmp_folder / "tmp_file.txt"
    with open(tmp_file_path, "w") as file:
        file.write("Hello World")

    assert tmp_file_path.exists()  # double check that the file actually exists

    return tmp_file_path


if __name__ == "__main__":
    tmp_file_path = this_func_create_a_tmp_file_and_return_its_path()

    # After the function is executed, the folder and its files are gone.
    assert not tmp_file_path.exists()

```

Execute `main.py`

```
python main.py
```
See how there are not assertments error? That's the power of `tmp-folder` 💪
