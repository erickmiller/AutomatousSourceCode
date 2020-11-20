from math import pow

def sqrt_n(value, exponent):
    return pow(value, 1.0/exponent)

class Visitor(object):
    def __init__(self):
        pass
    def visitNumber(self, number):
        pass
    def visitPlus(self, plus):
        pass
    def visitMul(self, mul):
        pass
    def visitPower(self, power):
        pass
    def visitSquareRoot(self, sqrt):
        pass

class CalculatorVisitor(Visitor):
    def __init__(self):
        pass

    def visitNumber(self, number):
        return int(number.value.value)

    def visitPlus(self, plus):
        return plus.left.accept(self) + plus.right.accept(self)

    def visitMul(self, mul):
        return mul.left.accept(self)* mul.right.accept(self)

    def visitPower(self, power):
        return pow(power.value.accept(self), power.power.accept(self))

    def visitSquareRoot(self, sqrt):
        return sqrt_n(sqrt.value.accept(self), sqrt.sqrtpower.accept(self))

    def visitEquation(self, eq):
        return

class PrinterVisitor(Visitor):
    def __init__(self):
        pass

    def visitNumber(self, number):
        return "{}".format(number.value)

    def visitPlus(self, plus):
        return "({} + {})".format(plus.left.accept(self), plus.right.accept(self))

    def visitMul(self, mul):
        return "({} * {})".format(mul.left.accept(self), mul.right.accept(self))

    def visitPower(self, power):
        return "pow({}, {})".format(power.value.accept(self), power.power.accept(self))

    def visitSquareRoot(self, sqrt):
        return "sqrt_n({}, {})".format(sqrt.value.accept(self), sqrt.sqrtpower.accept(self))

    def visitEquation(self, eq):
        return "{} = {}".format(eq.left.accept(self), eq.right.accept(self))

class Expression(object):
    def __init__(self):
        pass

class SquareRoot(Expression):
    def __init__(self, value, sqrtpower):
        self.value = value
        self.sqrtpower = sqrtpower
    def accept(self, visitor):
        return visitor.visitSquareRoot(self)

class Power(Expression):
    def __init__(self, value, power):
        self.value = value
        self.power = power
    def accept(self, visitor):
        return visitor.visitPower(self)

class Mul(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def accept(self, visitor):
        return visitor.visitMul(self)

class Plus(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def accept(self, visitor):
        return visitor.visitPlus(self)

class Number(Expression):
    def __init__(self, value):
        self.value = value
    def accept(self, visitor):
        return visitor.visitNumber(self)

class Equation(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def accept(self, visitor):
        return visitor.visitEquation(self)


