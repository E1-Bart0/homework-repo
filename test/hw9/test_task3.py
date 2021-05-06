import tempfile

import pytest

from All_home_works.hw9.task3 import universal_file_counter


@pytest.fixture(scope="module", name="dirname")
def make_dir_with_files():
    directory = tempfile.TemporaryDirectory()
    files = []
    for extension in (".py", ".txt", ".txt"):
        file = tempfile.NamedTemporaryFile(
            dir=directory.name, suffix=extension, mode="w"
        )
        data = ["first_line", "second line", "third line. Stop"]
        file.writelines([line + "\n" for line in data])
        file.seek(0)

        files.append(file)

    yield directory.name
    directory.cleanup()


@pytest.mark.parametrize("extension,expected", [("txt", 6), ("py", 3)])  # noqa: PT006
def test_universal_file_counter__without_tokenizer(dirname, extension, expected):
    res = universal_file_counter(dirname, extension)
    assert res == expected


def test_universal_file_counter__with_tokenizer(dirname):
    expected = 6
    extension = "py"
    res = universal_file_counter(dirname, extension, str.split)
    assert res == expected
