import tempfile

import pytest

from All_home_works.hw9.task3 import universal_file_counter


@pytest.fixture()
def make_dir():
    directory = None
    files = []

    def _dirname(data):
        nonlocal directory, files
        directory = tempfile.TemporaryDirectory()
        for extension in (".py", ".txt", ".txt"):
            named_file = tempfile.NamedTemporaryFile(
                dir=directory.name, suffix=extension, mode="w"
            )
            named_file.writelines(data)
            named_file.seek(0)
            files.append(named_file)
        return directory.name

    yield _dirname
    for file in files:
        file.close()
    directory.cleanup()


@pytest.mark.parametrize(("extension", "expected"), [("txt", 4), ("py", 2)])
def test_universal_file_counter__without_tokenizer(make_dir, extension, expected):
    data = ["one line\n", "second line"]
    dirname = make_dir(data)
    res = universal_file_counter(dirname, extension)
    assert res == expected


def test_universal_file_counter__without_tokenizer_file_ends_with_empty_line(make_dir):
    data = ["first line\n"]
    dirname = make_dir(data)
    res = universal_file_counter(dirname, "py")
    assert res == 2


def test_universal_file_counter__without_tokenizer_if_file_is_empty(make_dir):
    data = []
    dirname = make_dir(data)
    res = universal_file_counter(dirname, "py")
    assert res == 0


def test_universal_file_counter__with_tokenizer(make_dir):
    expected = 4
    data = ["one line\n", "second line\n"]
    dirname = make_dir(data)
    res = universal_file_counter(dirname, "py", str.split)
    assert res == expected
