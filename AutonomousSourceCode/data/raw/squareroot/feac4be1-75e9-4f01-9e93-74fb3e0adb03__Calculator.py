import math
import sys


# class Button(QToolButton):
#     def __init__(self, text, parent=None):
#         super(Button, self).__init__(parent)
#         self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
#         self.setText(text)

#     def sizeHint(self):
#         size = super(Button, self).sizeHint()
#         size.setHeight(size.height() + 20)
#         size.setWidth(max(size.width(), size.height()))
#         return size


class Calculator(QWidget):
    NumberDigit = 10

    def __init__(self, parent=None):
        self.Pi = math.pi
        self.e = math.e
        self.factorial_memo = {0: 1, 1: 1}

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def mod(self, a, b):
        return a % b

    def power(self, a, b):
        return a ** b

    def factorial(self, a):
        if a not in self.factorial_memo:
            self.factorial_memo[a] = self.factorial(a-1) * a

        return self.factorial_memo[a]

    def log(self, number, base):
        return math.log(number, base)

    def square_root(self, number):
        return math.sqrt(number)
