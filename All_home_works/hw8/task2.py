"""
Description in task2.rst
"""
import sqlite3


class TableData:
    def __init__(self, db_name, db_table):
        self._conn = sqlite3.connect(db_name)
        self._conn.row_factory = sqlite3.Row
        self._db_table = db_table

    def check_if_table_in_db(self):
        self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?;",
            (self._db_table,),
        )
        if self.cursor.fetchone() is None:
            raise sqlite3.OperationalError(f"no such table: {self._db_table}")

    def __enter__(self):
        self.cursor = self._conn.cursor()
        self.check_if_table_in_db()
        return self

    def __iter__(self):
        self.cursor.execute(f"SELECT * FROM '{self._db_table}';")  # noqa: S608
        return (dict(zip(data.keys(), data)) for data in self.cursor.fetchall())

    def __contains__(self, item):
        return any(item in dict_obj.values() for dict_obj in self)

    def __len__(self):
        self.cursor.execute(f"SELECT count(*) FROM '{self._db_table}';")  # noqa: S608
        return self.cursor.fetchone()[0]

    def __getitem__(self, item):
        self.cursor.execute(
            f"SELECT * FROM '{self._db_table}' where name=?;", (item,)  # noqa: S608
        )
        data = self.cursor.fetchone()
        return dict(zip(data.keys(), data)) if data is not None else None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._conn:
            self._conn.close()
