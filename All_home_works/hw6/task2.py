"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        return datetime.datetime.now() < self.created + self.deadline


class HomeworkResult:
    def __init__(self, author, homework, solution):
        if not isinstance(homework, Homework):
            raise InstanceNotHomeworkError(homework)
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.now()
        self.homework = homework

    def __str__(self):
        return (
            f'Homework: "{self.homework.text}" was done by: "{self.author.first_name}'
        )


class Human:
    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name


class Student(Human):
    def do_homework(self, homework, solution):
        if isinstance(homework, Homework):
            if homework.is_active():
                return HomeworkResult(author=self, homework=homework, solution=solution)
            raise DeadlineError(homework.created + homework.deadline)
        raise InstanceNotHomeworkError(homework)


class Teacher(Human):
    homework_done = defaultdict(set)

    @staticmethod
    def check_homework(homework_result: HomeworkResult):
        if len(homework_result.solution) > 5:
            Teacher.homework_done[homework_result.homework].add(homework_result)
            return True
        return False

    @staticmethod
    def reset_results(homework=None):
        if homework is None:
            Teacher.homework_done = defaultdict(set)
        else:
            del Teacher.homework_done[homework]

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text=text, deadline=deadline)


class InstanceNotHomeworkError(Exception):
    def __init__(self, homework):
        self.messages = f"You gave a not Homework object, Got {type(homework)}"
        super().__init__(self.messages)


class DeadlineError(Exception):
    def __init__(self, deadline: datetime):
        deadline = datetime.datetime.strftime(deadline, "%d %B")
        self.messages = f'You are late. Deadline was: "{deadline}"'
        super().__init__(self.messages)
