import pytest

from All_home_works.hw6.task1 import instances_counter


@pytest.fixture()
def test_class():
    @instances_counter
    class TestClass:
        test = 1

        def test_plus_one(self):
            self.test += 1

        def __init__(self, var=None):
            self.var = var

    return TestClass


def test__get_created_instances__class(test_class):
    assert 0 == test_class.get_created_instances()
    test_class()
    assert 1 == test_class.get_created_instances()


def test__get_created_instances__class_instance(test_class):  # noqa:
    _, _, _ = test_class(), test_class(), test_class()
    assert 3 == test_class.get_created_instances()


def test__reset_instances_counter__class_instance(test_class):
    _, _, _ = test_class(), test_class(), test_class()
    test_class.reset_instances_counter()
    assert 0 == test_class.get_created_instances()


def test__get_created_instances__check_class_instance_not_broken(test_class):
    test = test_class(var=10)
    assert 1 == test.test
    test.test_plus_one()
    assert 2 == test.test
    assert 10 == test.var
