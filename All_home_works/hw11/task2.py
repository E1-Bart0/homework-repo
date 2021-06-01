"""
You are given the following code:
class Order:
    morning_discount = 0.25
    def __init__(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
Example of the result call:
def morning_discount(order):
    ...
def elder_discount(order):
    ...
order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50
order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""


def morning_discount(order):
    discount = 0.5
    result = order.price - order.price * discount
    return int(result)


def elder_discount(order):
    discount = 0.9
    result = order.price - order.price * discount
    return int(result)


class Order:
    def __init__(self, price, strategy):
        self.price = price
        self._discount_program = strategy

    def final_price(self):
        return self._discount_program(self)