import sqlite3

import pytest

from All_home_works.hw8.task2 import TableData


@pytest.fixture()
def _create_db_table():
    conn = sqlite3.connect("file::memory:?cache=shared")
    cursor = conn.cursor()
    data = [("Book1", "John Doe"), ("Book2", "Jain Doe")]
    cursor.execute("CREATE TABLE test (name, author);")
    cursor.executemany("INSERT INTO test (name, author) VALUES(?, ?);", data)
    conn.commit()
    yield
    conn.close()


@pytest.fixture()
def updated_db(_create_db_table):
    with TableData("file::memory:?cache=shared", "test") as storage:
        conn = sqlite3.connect("file::memory:?cache=shared")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO test (name, author) VALUES ('Test Book', 'Test Author')"
        )
        conn.commit()
        yield storage
        cursor.execute("DELETE FROM test WHERE name='Test Book'")
        conn.commit()
        conn.close()


@pytest.mark.usefixtures("_create_db_table")
def test_table_data__not_such_table():
    with pytest.raises(sqlite3.OperationalError, match="no such table:"):  # noqa: PT012
        with TableData("file::memory:?cache=shared", "NOT EXSISTS"):
            ...


@pytest.mark.usefixtures("_create_db_table")
def test_table_data__if_len_correct():
    with TableData("file::memory:?cache=shared", "test") as storage:
        assert 2 == len(storage)


def test_table_data__if_len_correct__after_update_storage(updated_db):
    storage = updated_db
    assert 3 == len(storage)


@pytest.mark.usefixtures("_create_db_table")
def test_table_data__get_row_from_db_by_name_but_there_is_not_such_record():
    with TableData("file::memory:?cache=shared", "test") as storage:
        assert {"name": "Book1", "author": "John Doe"} == storage["Book1"]
        with pytest.raises(KeyError):
            _ = storage["Book3"]


def test_table_data__get_row_from_db_by_name__check_storage_after_update(updated_db):
    storage = updated_db
    assert {"name": "Test Book", "author": "Test Author"} == storage["Test Book"]


@pytest.mark.usefixtures("_create_db_table")
def test_table_data__for_loop():
    with TableData("file::memory:?cache=shared", "test") as storage:
        iter_storage = iter(storage)
        row = next(iter_storage)
        assert row["name"] == "Book1"
        assert row["author"] == "John Doe"
        row = next(iter_storage)
        assert row["name"] == "Book2"
        assert row["author"] == "Jain Doe"
        with pytest.raises(StopIteration):
            next(iter_storage)


@pytest.mark.usefixtures("_create_db_table")
def test_table_data__for_loop_but_there_is_no_records():
    conn = sqlite3.connect("file::memory:?cache=shared")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM test;")
    conn.commit()
    conn.close()
    with TableData("file::memory:?cache=shared", "test") as storage:
        iter_storage = iter(storage)
        with pytest.raises(StopIteration):
            next(iter_storage)


@pytest.mark.usefixtures("_create_db_table")
def test_table_data__if_something_in_storage():
    with TableData("file::memory:?cache=shared", "test") as storage:
        assert "Book1" in storage
        assert "Jain Doe" in storage


@pytest.mark.usefixtures("_create_db_table")
def test_table_data__if_something_in_storage__but_something_not_exists_in_storage():
    with TableData("file::memory:?cache=shared", "test") as storage:
        assert "Book3" not in storage
