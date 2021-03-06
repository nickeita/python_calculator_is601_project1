from math import sqrt


class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return b - a

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        if a == 0:
            return '###'
        else:
            return b / a

    @staticmethod
    def sqr(a):
        return a * a

    @staticmethod
    def sqroot(a):
        if a < 0:
            return '###'
        else:
            return sqrt(a)
