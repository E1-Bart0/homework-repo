from unittest.mock import Mock

from All_home_works.hw11.task2 import Order


def test_order():
    discount_program = Mock()
    order = Order(1, discount_program)
    order.final_price()
    discount_program.assert_called_once_with(order)


def test_order_change_discount_program():
    discount_program_1 = Mock()
    discount_program_2 = Mock()
    order = Order(1, discount_program_1)
    order.strategy = discount_program_2
    order.final_price()
    discount_program_1.assert_not_called()
    discount_program_2.assert_called_once_with(order)
