"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
from enum import Enum
class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"
class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"
Should become:
class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")
class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


class SimplifiedEnum(type):
    def __init__(cls, *args, **kwargs):
        cls.__getattr__ = SimplifiedEnum.__getattr__
        cls.__keys = SimplifiedEnum.__keys
        super().__init__(*args, **kwargs)

    def __getattr__(cls, item):
        if item in cls.__keys:
            return item
        raise AttributeError(f"Does not exist: {item}")

    def __new__(cls, name, bases, attrs):
        cls.__keys = set()
        for key, value in attrs.copy().items():
            if key == value:
                cls.__keys.add(attrs.pop(key))
        return super().__new__(cls, name, bases, attrs)
