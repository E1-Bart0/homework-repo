import os
import sqlite3
import tempfile
import time

import pytest

from All_home_works.hw8.task2 import TableData


@pytest.fixture(scope="module")
def create_db_table():
    directory = tempfile.TemporaryDirectory()
    path = os.path.join(directory.name, "test.sqlite")
    db_name = os.path.normpath(path)
    db_table = f"test_table_{time.time_ns()}"

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    data = [("Book1", "John Doe"), ("Book2", "Jain Doe")]
    cursor.execute(f"CREATE TABLE '{db_table}' (name, author);")
    cursor.executemany(f"INSERT INTO '{db_table}'(name, author) VALUES(?, ?);", data)
    conn.commit()
    yield db_name, db_table
    cursor.execute(f"DROP TABLE '{db_table}';")
    conn.commit()
    conn.close()
    directory.cleanup()


@pytest.fixture()
def updated_db(create_db_table):
    db_name, db_table = create_db_table
    with TableData(db_name, db_table) as storage:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO '{db_table}' (name, author) VALUES ('Test Book', 'Test Author')"
        )
        conn.commit()
        yield storage
        cursor.execute(f"DELETE FROM '{db_table}' WHERE name='Test Book'")  # noqa: S608
        conn.commit()
        conn.close()


def test_table_data__not_such_table(create_db_table):
    db_name, db_table = create_db_table
    with pytest.raises(sqlite3.OperationalError, match="no such table:"):  # noqa: PT012
        with TableData(db_name, "NOT EXSISTS") as _:
            ...


def test_table_data__if_len_correct(create_db_table):
    db_name, db_table = create_db_table
    with TableData(db_name, db_table) as storage:
        assert 2 == len(storage)


def test_table_data__if_len_correct__after_update_storage(updated_db):
    storage = updated_db
    assert 3 == len(storage)


def test_table_data__get_row_from_db_by_name_if_not_such_row_none_expect(
    create_db_table,
):
    db_name, db_table = create_db_table
    with TableData(db_name, db_table) as storage:
        assert {"name": "Book1", "author": "John Doe"} == storage["Book1"]
        assert None is storage["Book3"]


def test_table_data__get_row_from_db_by_name__check_storage_after_update(updated_db):
    storage = updated_db
    assert {"name": "Test Book", "author": "Test Author"} == storage["Test Book"]


def test_table_data__for_loop(create_db_table):
    db_name, db_table = create_db_table
    with TableData(db_name, db_table) as storage:
        iter_storage = iter(storage)
        row = next(iter_storage)
        assert row["name"] == "Book1"
        assert row["author"] == "John Doe"
        row = next(iter_storage)
        assert row["name"] == "Book2"
        assert row["author"] == "Jain Doe"
        with pytest.raises(StopIteration):
            next(iter_storage)


def test_table_data__if_something_in_storage(create_db_table):
    db_name, db_table = create_db_table
    with TableData(db_name, db_table) as storage:
        assert "Book1" in storage
        assert "Jain Doe" in storage


def test_table_data__if_something_in_storage__but_something_not_exists_in_storage(
    create_db_table,
):
    db_name, db_table = create_db_table
    with TableData(db_name, db_table) as storage:
        result = "Book3" in storage
        assert False is result
