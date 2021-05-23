import tempfile

import pytest

from All_home_works.hw9.task3 import universal_file_counter


@pytest.fixture()
def make_dir():
    with tempfile.TemporaryDirectory() as directory:
        files = []

        def _dirname(data, file_extensions):
            nonlocal files
            for extension in file_extensions:
                named_file = tempfile.NamedTemporaryFile(
                    dir=directory, suffix=extension, mode="w"
                )
                named_file.writelines(data)
                named_file.seek(0)
                files.append(named_file)
            return directory

        yield _dirname


@pytest.mark.parametrize(
    ("files", "extension", "expected"),
    [((".txt", ".txt"), "txt", 4), ((".py", ".txt"), "py", 2)],
)
def test_universal_file_counter__without_tokenizer(
    make_dir, files, extension, expected
):
    data = ["one line\n", "second line"]
    dirname = make_dir(data, files)
    res = universal_file_counter(dirname, extension)
    assert res == expected


def test_universal_file_counter__without_tokenizer_if_file_is_empty(make_dir):
    data = []
    dirname = make_dir(data, (".py",))
    res = universal_file_counter(dirname, "py")
    assert res == 0


def test_universal_file_counter__without_tokenizer_if_only_one_line_in_file(make_dir):
    data = ["first line"]
    dirname = make_dir(data, (".py",))
    res = universal_file_counter(dirname, "py")
    assert res == 1


def test_universal_file_counter__without_tokenizer_file_ends_with_empty_line(make_dir):
    data = ["first line\n"]
    dirname = make_dir(data, (".py",))
    res = universal_file_counter(dirname, "py")
    assert res == 2


def test_universal_file_counter__with_tokenizer(make_dir):
    expected = 4
    data = ["one line\n", "second line\n"]
    dirname = make_dir(data, (".py",))
    res = universal_file_counter(dirname, "py", str.split)
    assert res == expected
