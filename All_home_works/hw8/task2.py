"""
Description in task2.rst
"""
import sqlite3


class TableData:
    def __init__(self, db_name, db_table):
        self._db_name = db_name
        self._db_table = db_table

    def check_if_table_in_db(self):
        self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?;",
            (self._db_table,),
        )
        if self.cursor.fetchone() is None:
            raise sqlite3.OperationalError(f"no such table: {self._db_table}")

    def __enter__(self):
        self._conn = sqlite3.connect(self._db_name)
        self._conn.row_factory = sqlite3.Row
        self.cursor = self._conn.cursor()
        self.check_if_table_in_db()
        return self

    def __iter__(self):
        self.cursor.execute(f"SELECT * FROM '{self._db_table}';")  # noqa: S608
        return self

    def __next__(self):
        data = self.cursor.fetchone()
        if data is None:
            raise StopIteration
        return dict(zip(data.keys(), data))

    def __contains__(self, item):
        return self._find_row_with_name(item)

    def __len__(self):
        self.cursor.execute(f"SELECT count(*) FROM '{self._db_table}';")  # noqa: S608
        return self.cursor.fetchone()[0]

    def __getitem__(self, item):
        data = self._find_row_with_name(item)
        if data is None:
            raise KeyError(item)
        return dict(zip(data.keys(), data))

    def _find_row_with_name(self, item):
        self.cursor.execute(
            f"SELECT * FROM '{self._db_table}' where name=?;", (item,)  # noqa: S608
        )
        return self.cursor.fetchone()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._conn:
            self._conn.close()
