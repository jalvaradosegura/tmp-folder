from pathlib import Path

from tmp_folder import use_tmp_folder


def test_use_tmp_folder():
    @use_tmp_folder
    def some_func_that_needs_a_tmp_folder_and_return_its_path(tmp_folder: Path) -> Path:
        with open(tmp_folder / "file.txt", "w") as file:
            file.write("Hi")
        with open(tmp_folder / "file.txt", "r") as file:
            file_content = file.read()

        assert file_content == "Hi"
        assert tmp_folder.exists()

        return tmp_folder

    tmp_folder = some_func_that_needs_a_tmp_folder_and_return_its_path()

    assert not tmp_folder.exists()


@use_tmp_folder
def write_a_file_and_return_its_path(tmp_folder: Path):
    file_path = tmp_folder / "file.txt"
    with open(file_path, "w") as file:
        file.write("Hi")

    assert file_path.exists()

    return file_path


def test_write_a_file_and_return_its_path():
    file_path = write_a_file_and_return_its_path()
    assert not file_path.exists()
