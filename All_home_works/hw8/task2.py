"""
Description in task2.rst
"""
import sqlite3


class Data:
    def __init__(self, cursor):
        self.cursor = cursor
        self.column_names = [x[0] for x in self.cursor.description]

    def __next__(self):
        try:
            if data := self.cursor.fetchone():
                self.set_attributes_from_row(self.column_names, data)
                return self
            raise StopIteration
        except sqlite3.ProgrammingError:
            raise StopIteration

    def set_attributes_from_row(self, column_names, row):
        for key, value in zip(column_names, row):
            setattr(self, key, value)

    def __getitem__(self, item):
        return self.__dict__[item]

    def __eq__(self, other):
        return other in self.__dict__.values()


class TableData:
    def __init__(self, db_name, db_table):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.db_table = db_table

    def __iter__(self):
        self.cursor.execute(f"SELECT * FROM '{self.db_table}'")  # noqa: S608
        return Data(cursor=self.cursor)  # noqa: S608

    def __len__(self):
        self.cursor.execute(
            f"SELECT count(*) FROM '{self.db_table}' query"  # noqa: S608
        )
        return self.cursor.fetchone()[0]

    def __getitem__(self, item):
        self.cursor.execute(
            f"SELECT * FROM '{self.db_table}' where name='{item}'"  # noqa: S608
        )
        return self.get_row_as_dict_from(self.cursor)

    @staticmethod
    def get_row_as_dict_from(cursor):
        data = cursor.fetchone()
        if data is None:
            return None
        column_name = (x[0] for x in cursor.description)
        return {key: value for key, value in zip(column_name, data)}

    def __del__(self):
        if self.conn:
            self.conn.close()
