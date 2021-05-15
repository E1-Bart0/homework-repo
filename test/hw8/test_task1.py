from tempfile import NamedTemporaryFile
from unittest.mock import patch

import pytest

from All_home_works.hw8.task1 import KeyValueStorage


@pytest.fixture(scope="module")
def file_name():
    file = NamedTemporaryFile(mode="w")
    data = ["name=NAME\n", "new_1=NEW_1\n", "int_value=10\n"]
    file.writelines(data)
    file.seek(0)
    yield file.name
    file.close()


def test_key_value_storage__has_attributes(file_name):
    storage = KeyValueStorage(file_name)
    assert storage.name == "NAME"
    assert storage.new_1 == "NEW_1"
    assert storage.int_value == 10


def test_key_value_storage__has_attributes_as_item(file_name):
    storage = KeyValueStorage(file_name)
    assert storage["name"] == "NAME"
    assert storage["new_1"] == "NEW_1"
    assert storage["int_value"] == 10


def test_key_value_storage__not_existing_attributes(file_name):
    storage = KeyValueStorage(file_name)
    with pytest.raises(ValueError, match="object has no attribute"):
        _ = storage.not_existing
    with pytest.raises(ValueError, match="object has no attribute"):
        _ = storage["not_existing"]


@patch(
    "All_home_works.hw8.task1.KeyValueStorage._get_lines_from_file",
    return_value=("1not_valid=ERROR",),
)
def test_key_value_storage__invalid_attribute_starts_with_digit(mock, file_name):
    with pytest.raises(ValueError, match="Syntax error: Not valid method name:"):
        KeyValueStorage(file_name)


@patch(
    "All_home_works.hw8.task1.KeyValueStorage._get_lines_from_file",
    return_value=("not:valid=ERROR",),
)
def test_key_value_storage__invalid_attribute_not_legal_char_in_name(mock, file_name):
    with pytest.raises(ValueError, match="Syntax error: Not valid method name:"):
        KeyValueStorage(file_name)


@patch(
    "All_home_works.hw8.task1.KeyValueStorage._get_lines_from_file",
    return_value=("path=ERROR",),
)
def test_key_value_storage__if_attribute_already_exists(mock, file_name):
    storage = KeyValueStorage(file_name)
    assert storage.path == file_name
    assert storage["path"] == "ERROR"


@patch(
    "All_home_works.hw8.task1.KeyValueStorage._get_lines_from_file",
    return_value=("foo=1", "foo_method=1"),
)
def test_if_attribute_clash_existing_built_in_attributes_take_precedence(
    mock, file_name
):
    class Test(KeyValueStorage):
        @property
        def foo(self):
            return 5

        @staticmethod
        def foo_method():
            return 5

    storage = Test(file_name)
    assert storage.foo == 5
    assert storage["foo"] == 1
    assert storage.foo_method() == 5
    assert storage["foo_method"] == 1
