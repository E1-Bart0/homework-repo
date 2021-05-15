import os
import sqlite3
import tempfile
import uuid

import pytest

from All_home_works.hw8.task2 import TableData


@pytest.fixture(scope="module")
def create_db_table():
    directory = tempfile.TemporaryDirectory()
    path = os.path.join(directory.name, "test.sqlite")
    db_name = os.path.normpath(path)
    db_table = f"test_table_{uuid.uuid4()}"

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE '{db_table}' (name, author)")  # noqa: S608
    cursor.execute(
        f"INSERT INTO '{db_table}' (name, author) VALUES ('Book1', 'John Doe')"  # noqa: S608
    )
    cursor.execute(
        f"INSERT INTO '{db_table}' (name, author) VALUES ('Book2', 'Jain Doe')"  # noqa: S608
    )
    conn.commit()
    yield db_name, db_table
    cursor.execute(f"DROP TABLE '{db_table}'")  # noqa: S608
    conn.commit()
    conn.close()
    directory.cleanup()


@pytest.fixture()
def updated_db(create_db_table):
    db_name, db_table = create_db_table
    storage = TableData(db_name, db_table)

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO '{db_table}' (name, author) VALUES ('Test Book', 'Test Author')"  # noqa: S608
    )
    conn.commit()
    yield storage
    cursor.execute(f"DELETE FROM '{db_table}' WHERE name='Test Book'")  # noqa: S608
    conn.commit()
    conn.close()


def test_table_data__if_len_correct(create_db_table):
    db_name, db_table = create_db_table
    storage = TableData(db_name, db_table)
    assert 2 == len(storage)


def test_table_data__if_len_correct__after_update_storage(updated_db):
    storage = updated_db
    assert 3 == len(storage)


def test_table_data__get_row_from_db_by_name_if_not_such_row_none_expect(
    create_db_table,
):
    db_name, db_table = create_db_table
    storage = TableData(db_name, db_table)
    assert {"name": "Book1", "author": "John Doe"} == storage["Book1"]
    assert None is storage["Book3"]


def test_table_data__get_row_from_db_by_name__check_storage_after_update(updated_db):
    storage = updated_db
    assert {"name": "Test Book", "author": "Test Author"} == storage["Test Book"]


def test_table_data__for_loop(create_db_table):
    db_name, db_table = create_db_table
    storage = TableData(db_name, db_table)
    iter_storage = iter(storage)
    row = next(iter_storage)
    assert row["name"] == "Book1"
    assert row["author"] == "John Doe"
    next(iter_storage)
    assert row["name"] == "Book2"
    assert row["author"] == "Jain Doe"
    with pytest.raises(StopIteration):
        next(iter_storage)


def test_table_data__for_loop__but_conn_was_closed_during_iteration(create_db_table):
    db_name, db_table = create_db_table
    storage = TableData(db_name, db_table)
    iter_storage = iter(storage)
    row = next(iter_storage)
    assert row["name"] == "Book1"
    assert row["author"] == "John Doe"
    del storage
    with pytest.raises(StopIteration):
        next(iter_storage)


def test_table_data__if_something_in_storage(create_db_table):
    db_name, db_table = create_db_table
    storage = TableData(db_name, db_table)
    assert "Book1" in storage
    assert "Jain Doe" in storage


def test_table_data__if_something_in_storage__but_something_not_exists_in_storage(
    create_db_table,
):
    db_name, db_table = create_db_table
    storage = TableData(db_name, db_table)
    result = "Book3" in storage
    assert False is result
