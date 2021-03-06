"""
We have a file that works as key-value storage,
each line is represented as key and value separated by = symbol, example:

name=kek
last_name=top
song_name=shadilay
power=9001

Values can be strings or integer numbers.
If a value can be treated both as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt')
that has its keys and values accessible as collection items and as attributes.
Example:
storage['name'] # will be string 'kek'
storage.song_name # will be 'shadilay'
storage.power # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute
(for example when there's a line 1=something) ValueError should be raised.
File size is expected to be small, you are permitted to read it entirely into memory.
"""
import string


class KeyValueStorage:
    allowed_chars = {*string.digits, *string.ascii_letters, "_"}

    def __init__(self, path):
        self.path = path
        self.data = self._get_data_from_file()

    def _get_lines_from_file(self):
        with open(self.path) as file:
            for line in file:
                yield line.rstrip("\n")

    def _get_data_from_file(self):
        data = {}
        for line in self._get_lines_from_file():
            attr_name, attr_value = line.split("=")
            attr_value = int(attr_value) if attr_value.isdigit() else attr_value
            if not attr_name.isidentifier():
                raise ValueError(f"Syntax error: Not valid method name: '{attr_name}'")
            data[attr_name] = attr_value
        return data

    def __getitem__(self, item):
        value = self.data.get(item, None)
        if value is None:
            raise KeyError(
                f"'{KeyValueStorage.__name__}' object has no such key: '{item}'"
            )
        return value

    def __getattr__(self, attr):
        value = self.data.get(attr, None)
        if value is None:
            raise AttributeError(
                f"'{KeyValueStorage.__name__}' object has no such attribute: '{attr}'"
            )
        return value
