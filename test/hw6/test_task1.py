import pytest

from All_home_works.hw6.task1 import instances_counter


@pytest.fixture()
def test_class():
    @instances_counter
    class TestClass:
        attribute = 1

        def add_one(self):
            self.attribute += 1

        def __init__(self, var=None, kwarg_var=None):
            self.var = var
            self.kwarg_var = kwarg_var

    return TestClass


def test__get_created_instances__check_from_class(test_class):
    assert 0 == test_class.get_created_instances()
    test_class()
    assert 1 == test_class.get_created_instances()


def test__get_created_instances__check_method_from_class_instance(test_class):
    _, instance, _ = test_class(), test_class(), test_class()
    assert 3 == instance.get_created_instances()


def test__reset_instances_counter(test_class):
    _, _, _ = test_class(), test_class(), test_class()
    test_class.reset_instances_counter()
    assert 0 == test_class.get_created_instances()


def test__instances_counter__check_class_instance_not_broken(test_class):
    test = test_class(1, kwarg_var=2)
    assert 1 == test.attribute
    test.add_one()
    assert 2 == test.attribute
    assert 1 == test.var
    assert 2 == test.kwarg_var


def test__instances_counter__check_inherit_from_class_with_decorator(test_class):
    class A(test_class):
        pass

    _, _, _ = A(), A(), A()
    assert 3 == A.get_created_instances()
    A.reset_instances_counter()
    assert 0 == A.get_created_instances()


def test__instances_counter_overwrites_class_methods():
    @instances_counter
    class A:
        @staticmethod
        def get_created_instances():
            return "foo"

        @staticmethod
        def reset_instances_counter():
            return "foofoo"

    assert "foofoo" != A.get_created_instances()
    assert "foo" != A.reset_instances_counter()


def test__instances_counter_not_works__if_decorators_methods_was_overload_with_inherit_class(
    test_class,
):
    class A(test_class):
        def __init__(self, new_var, new_kwarg_var=None, *args, **kwargs):
            self.new_var = new_var
            self.new_kwarg_var = new_kwarg_var
            super().__init__(*args, **kwargs)

        @staticmethod
        def get_created_instances():
            return "foo"

        @staticmethod
        def reset_instances_counter():
            return "foofoo"

    assert "foo" == A.get_created_instances()
    assert "foofoo" == A.reset_instances_counter()
    test_class = A(1, 2, 3, kwarg_var=4)
    assert test_class.new_var == 1
    assert test_class.new_kwarg_var == 2
    assert test_class.var == 3
    assert test_class.kwarg_var == 4


def test__instance_attributes_overwrite_decorators_methods__but_in_class_methods_decorator_works_fine():
    @instances_counter
    class Test:
        def __init__(self, reset_instances_counter, get_created_instances):
            self.reset_instances_counter = reset_instances_counter
            self.get_created_instances = get_created_instances

    test_class = Test("reset", "get")
    assert test_class.get_created_instances == "get"
    assert test_class.reset_instances_counter == "reset"

    assert 1 == Test.get_created_instances()
    with pytest.raises(TypeError, match="'str' object is not callable"):
        test_class.get_created_instances()
