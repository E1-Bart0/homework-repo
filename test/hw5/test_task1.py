import datetime
from unittest.mock import patch

from All_home_works.hw5.task1 import Homework, Student, Teacher

TIME = datetime.datetime.now()


def test_teacher__first_name__last_name():
    name, last_name = "Daniil", "Shadrin"
    teacher = Teacher(name, last_name)
    assert name == teacher.first_name
    assert last_name == teacher.last_name


def test_student__first_name__last_name():
    name, last_name = "Roman", "Petrov"
    teacher = Student(name, last_name)
    assert name == teacher.first_name
    assert last_name == teacher.last_name


@patch(
    "All_home_works.hw5.task1.datetime.datetime",
)
def test_homework__init(time):
    deadline = 0
    text = "Learn functions"

    time.now.return_value = TIME

    expired_homework = Homework(text, deadline)
    assert expired_homework.created == TIME
    assert expired_homework.deadline == datetime.timedelta(days=deadline)
    assert expired_homework.text == text


@patch(
    "All_home_works.hw5.task1.datetime.datetime",
)
def test_teacher__create_home_work(time):
    text, deadline = "Learn functions", 0
    time.now.return_value = TIME

    create_homework = Teacher.create_homework(text, deadline)
    assert isinstance(create_homework, Homework)
    assert create_homework.text == text
    assert create_homework.deadline == datetime.timedelta(days=deadline)
    assert create_homework.text == text


@patch(
    "All_home_works.hw5.task1.datetime.datetime",
)
def test_student__do_homework__oop_homework(time):
    text, deadline = "Learn functions", 5
    time.now.return_value = TIME
    homework = Homework(text, deadline)
    done_homework = Student.do_homework(homework)
    assert isinstance(done_homework, Homework)


@patch(
    "All_home_works.hw5.task1.datetime.datetime",
)
def test_student__do_homework__expired_homework(time, capsys):
    text, deadline = "Learn functions", 5
    time.now.return_value = TIME
    homework = Homework(text, deadline)

    time.now.return_value = TIME + datetime.timedelta(days=6)
    done_homework = Student.do_homework(homework)
    out, err = capsys.readouterr()
    assert "You are late\n" == out
    assert None is done_homework
