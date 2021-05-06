import pytest

from All_home_works.hw6.task1 import instances_counter


@pytest.fixture()
def test_class():
    @instances_counter
    class TestClass:
        attribute = 1

        def add_one(self):
            self.attribute += 1

        def __init__(self, var=None):
            self.var = var

    return TestClass


def test__get_created_instances__check_from_class(test_class):
    assert 0 == test_class.get_created_instances()
    test_class()
    assert 1 == test_class.get_created_instances()


def test__get_created_instances__check_method_from_class_instance(test_class):  # noqa:
    _, instance, _ = test_class(), test_class(), test_class()
    assert 3 == instance.get_created_instances()


def test__reset_instances_counter(test_class):
    _, _, _ = test_class(), test_class(), test_class()
    test_class.reset_instances_counter()
    assert 0 == test_class.get_created_instances()


def test__instances_counter__check_class_instance_not_broken(test_class):
    test = test_class(var=10)
    assert 1 == test.attribute
    test.add_one()
    assert 2 == test.attribute
    assert 10 == test.var


def test__instances_counter__check_inherit_from_class_with_decorator(test_class):
    class A(test_class):
        pass

    _, _, _ = A(), A(), A()
    assert 3 == A.get_created_instances()
    A.reset_instances_counter()
    assert 0 == A.get_created_instances()


def test__instances_counter_breaks_class_methods():
    @instances_counter
    class A:
        @staticmethod
        def get_created_instances():
            return "foo"

        @staticmethod
        def reset_instances_counter():
            return "foofoo"

    _, _, _ = A(), A(), A()
    assert "foofoo" != A.get_created_instances()
    assert "foo" != A.reset_instances_counter()


def test__instances_counter_not_works__if_decorators_methods_was_overload_with_inherit_class(
    test_class,
):
    class A(test_class):
        @staticmethod
        def get_created_instances():
            return "foo"

        @staticmethod
        def reset_instances_counter():
            return "foofoo"

    _, _, _ = A(), A(), A()
    assert "foo" == A.get_created_instances()
    assert "foofoo" == A.reset_instances_counter()


def test__instances_counter_breaks_metaclass_if_metaclass_is_defining_method_for_class_which_are_decorators_method():
    class B(type):
        def __new__(cls, name, bases, dictionary):
            dictionary["a"] = 5
            dictionary["reset_instances_counter"] = cls.foo
            return super().__new__(cls, name, bases, dictionary)

        def foo(cls):
            return "foo"

    @instances_counter
    class A(metaclass=B):
        a = 1

    _, _, _ = A(), A(), A()
    assert 5 == A.a
    assert 3 == A.get_created_instances()
    assert "foo" != A.reset_instances_counter()
    assert 0 == A.get_created_instances()
