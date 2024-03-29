<p align="center">
  <img src="https://raw.githubusercontent.com/jalvaradosegura/tmp-folder/main/docs/tmp-folder.png" alt="tmp-folder">
</p>

<p align="center">

  <a href="https://codecov.io/gh/jalvaradosegura/tmp-folder">
    <img src="https://codecov.io/gh/jalvaradosegura/tmp-folder/branch/main/graph/badge.svg?token=IL5PVTYVRV"/>
  </a>

  <a href="https://github.com/psf/black" target="_blank">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="black">
  </a>

  <a href="https://pycqa.github.io/isort/" target="_blank">
    <img src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336" alt="isort">
  </a>

  <a href="https://github.com/jalvaradosegura/tmp-folder/actions/workflows/unit_tests.yml" target="_blank">
    <img src="https://github.com/jalvaradosegura/tmp-folder/actions/workflows/unit_tests.yml/badge.svg" alt="License">
  </a>

  <a href="https://pepy.tech/project/tmp-folder" target="_blank">
    <img src="https://static.pepy.tech/personalized-badge/tmp-folder?period=total&units=international_system&left_color=grey&right_color=blue&left_text=downloads" alt="downloads">
  </a>

  <a href="https://www.instagram.com/circus.infernus/" target="_blank">
    <img src="https://img.shields.io/badge/image--by-%40circus.infernus-blue" alt="image-by">
  </a>

</p>

---

Documentation: https://jalvaradosegura.github.io/tmp-folder/

---

## tmp-folder
Easily create a temporary folder. Put files in it and after you're done tmp-folder will delete the folder automatically.

## Installation

Install from PyPI:

```
pip install tmp-folder
```

## Usage
This is the minimum you need to get started with `tmp-folder`:
```py
from pathlib import Path

from tmp_folder import use_tmp_folder


@use_tmp_folder
def foo(tmp_folder: Path):
    pass
```

Just decorate the function in which you need a temporary folder. Then add as first parameter, the variable that will hold the temporary folder path (it can be named however you want). Finally, after the function execution is completed, the folder will be deleted.
