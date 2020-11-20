# -*- coding: utf-8 -*-


class MathSymbol():
    '''
    Class that performs the verification
    of operation and operand types
    '''
    def __init__(self, text):
        self.text = text

    def is_digit(self):
        try:
            float(self.text)
            return True
        except ValueError:
            return False

    def is_simple_operation(self):
        if (self.text == '+' or self.text == '-' or
                self.text == u'÷' or self.text == u'×' or
                self.text == u'^' or self.text == u'.'):
            return True
        return False

    def is_ce(self):
        if self.text == 'CE':
            return True
        return False

    def is_equal(self):
        if self.text == '=':
            return True
        return False

    def is_square_root(self):
        if self.text == u'√':
            return True
        return False

    def is_sign(self):
        if self.text == '+/-':
            return True
        return False
