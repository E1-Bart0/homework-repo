from unittest.mock import Mock

from All_home_works.hw11.task2 import Order


def test_order():
    discount_program = Mock()
    order = Order(1, discount_program)
    order.final_price()
    discount_program.assert_called_once_with(order)
