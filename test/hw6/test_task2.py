from collections import defaultdict
from unittest.mock import patch

import pytest

from All_home_works.hw6.task2 import (
    DeadlineError,
    Homework,
    HomeworkResult,
    InstanceNotHomeworkError,
    Student,
    Teacher,
)


@pytest.fixture()
def teacher():
    yield Teacher
    Teacher.homework_done = defaultdict(set)


@patch("All_home_works.hw6.task2.datetime.datetime")
@patch("All_home_works.hw6.task2.Homework.is_active", return_value=True)
def test_homework_result__attributes(mock, datetime):
    time = 1
    datetime.now.return_value = time
    student = Student("Roman", "Petrov")
    homework = Homework("Test Homework", 5)
    solution = "I have done this homework"
    homework_result = HomeworkResult(
        author=student, homework=homework, solution=solution
    )
    assert homework_result.author == student
    assert homework_result.solution == solution
    assert homework_result.created == time


def test_student__do_homework__raise_exception_if_homework_not_homework_object():
    student = Student("Roman", "Petrov")
    with pytest.raises(
        InstanceNotHomeworkError, match="You gave a not Homework object, Got"
    ):
        student.do_homework(student, "I have done this homework")


def test_homework_result__raise_exception_if_homework_not_homework_object():
    student = Student("Roman", "Petrov")
    with pytest.raises(
        InstanceNotHomeworkError, match="You gave a not Homework object, Got"
    ):
        HomeworkResult(
            author=student, homework=student, solution="I have done this homework"
        )


@patch("All_home_works.hw6.task2.Homework.is_active", return_value=False)
def test_student__do_homework__raise_exception_if_homework_expired(is_active):
    student = Student("Roman", "Petrov")
    homework = Homework("Test Homework", 5)
    solution = "I have done this homework"
    with pytest.raises(DeadlineError, match="You are late. Deadline was:"):
        student.do_homework(homework, solution)


def test_student__do_homework__ok_return_homework_result():
    student = Student("Roman", "Petrov")
    homework = Homework("Test Homework", 5)
    solution = "I have done this homework"
    hw_result = student.do_homework(homework, solution)
    assert isinstance(hw_result, HomeworkResult)


def test_student__attributes__from_parent_class():
    first_name, last_name = "Roman", "Petrov"
    student = Student(first_name, last_name)
    assert student.first_name == first_name
    assert student.last_name == last_name


def test_teacher__attributes__from_parent_class():
    first_name, last_name = "Lev", "Sokolov"
    teacher = Teacher(first_name, last_name)
    assert teacher.first_name == first_name
    assert teacher.last_name == last_name


def test_teacher__have_attribute_homework_done():
    assert hasattr(Teacher, "homework_done")


def test_teacher_method__check_homework_returns_true():
    student = Student("Roman", "Petrov")
    homework = Homework("Test Homework", 5)
    solution = "I have done this homework"
    hw_result = student.do_homework(homework, solution)
    result = Teacher.check_homework(homework_result=hw_result)
    assert True is result
    assert Teacher.homework_done[homework] == {hw_result}


def test_teacher_method__check_homework_returns_false():
    student = Student("Roman", "Petrov")
    homework = Homework("Test Homework", 5)
    solution = "Done"
    hw_result = student.do_homework(homework, solution)
    result = Teacher.check_homework(homework_result=hw_result)
    assert False is result
    assert set() == Teacher.homework_done[homework]


def test_teacher__attribute_homework_done__do_not_have_identical_homework_result(
    teacher,
):
    student = Student("Roman", "Petrov")
    homework = Homework("Test Homework", 5)
    solution = "I have done this homework"
    hw_result = student.do_homework(homework, solution)
    result1 = teacher.check_homework(homework_result=hw_result)
    result2 = teacher.check_homework(homework_result=hw_result)
    assert True is result1
    assert True is result2
    assert 1 == len(teacher.homework_done[homework])


def test_teacher__reset_result__with_param_homework__delete_only_this_homework_form_homework_done(
    teacher,
):
    student = Student("Roman", "Petrov")
    homework1 = Homework("Test Homework1", 5)
    homework2 = Homework("Test Homework2", 6)
    solution1 = "I have done this homework"
    hw_result1 = student.do_homework(homework1, solution1)
    hw_result2 = student.do_homework(homework2, solution1)
    teacher.check_homework(hw_result1)
    teacher.check_homework(hw_result2)
    teacher.reset_results(homework1)
    assert 1 == len(teacher.homework_done)


def test_teacher_method__reset_result__without_param__delete_all_homeworks_form_homework_done(
    teacher,
):
    student = Student("Roman", "Petrov")
    homework1 = Homework("Test Homework1", 5)
    homework2 = Homework("Test Homework2", 6)
    solution1 = "I have done this homework"
    hw_result1 = student.do_homework(homework1, solution1)
    hw_result2 = student.do_homework(homework2, solution1)
    teacher.check_homework(hw_result1)
    teacher.check_homework(hw_result2)
    teacher.reset_results()
    assert 0 == len(teacher.homework_done)
