"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    counter = 0
    new = cls.__new__

    def get_instance(self=None):
        return counter

    def reset_counter(self=None):
        nonlocal counter
        counter = 0
        return counter  # noqa: R504

    def new_instance(cls, *args, **kwargs):
        nonlocal counter
        counter += 1
        return new(cls)

    cls.__new__ = new_instance
    cls.get_created_instances = get_instance
    cls.reset_instances_counter = reset_counter
    return cls


@instances_counter
class User:
    pass


if __name__ == "__main__":
    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
