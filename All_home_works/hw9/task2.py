"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
with Supressor(IndexError):
   [][2]
"""
import contextlib


class Suppressor:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None or exc_type == self.exception:
            return True
        return False


@contextlib.contextmanager
def suppressor(exception):
    try:
        yield
    except exception:
        pass
