import pytest

from All_home_works.hw11.task1 import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class SizesEnum(metaclass=SimplifiedEnum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"


@pytest.mark.parametrize(
    ("cls", "attr"),
    [
        (ColorsEnum, "RED"),
        (ColorsEnum, "BLACK"),
        (SizesEnum, "XL"),
        (SizesEnum, "S"),
    ],
)
def test_simplified_enum_metaclass_works_fine_for_class(cls, attr):
    assert getattr(cls, attr) == attr


@pytest.mark.parametrize(
    ("cls", "attr"),
    [
        (ColorsEnum, "O"),
        (SizesEnum, "O"),
    ],
)
def test_simplified_enum_metaclass__if_attr_does_not_exist(cls, attr):
    with pytest.raises(AttributeError, match="Does not exist:"):
        getattr(cls, attr)


def test_simplified_enum_metaclass__if_class_instance_is_ok():
    class Test(metaclass=SimplifiedEnum):
        A = "A"

        def __init__(self, a):
            self.a = a

        def add_one_to_a(self):
            self.a += 1
            return self.a

    test = Test(0)
    assert Test.A == "A"
    assert test.A == "A"
    assert test.a == 0
    test.add_one_to_a()


def test_simplified_enum_metaclass_is_ok__if_class_instance_overwrite__keys():
    class Test(metaclass=SimplifiedEnum):
        A = "A"

        def __init__(self, a):
            self.__keys = a

    test = Test(0)
    assert Test.A == "A"
    assert test.A == "A"
    assert test._Test__keys == 0


def test_simplified_enum_metaclass__if_class_instance_overwrite_attrs():
    class Test(metaclass=SimplifiedEnum):
        A = "A"
        B = "B"

        def __init__(self, a):
            self.A = a

    test = Test(0)
    assert Test.A == "A"
    assert test.A == 0
    assert test.B == "B"


def test_simplified_enum_metaclass__overwrite__getattr_for_instance():
    class Test(metaclass=SimplifiedEnum):
        A = "A"

        def __getattr__(self, attr):
            return "EXISTS"

    test = Test()
    assert Test.A == "A"
    with pytest.raises(AttributeError, match="Does not exist:"):
        _ = Test.NOT_EXISTS
    assert test.A == "A"
    with pytest.raises(AttributeError, match="Does not exist:"):
        _ = test.NOT_EXISTS
