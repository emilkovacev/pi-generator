import math


class Fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    def __str__(self):
        return f'{self.num}/{self.den}'

    def multiply(self, c):
        return Fraction(self.num * c, self.den * c)

    def simplify(self):
        i: int = 2
        while i <= min(self.num, self.den):
            if self.num % i == 0 and self.den % i == 0:
                return Fraction(self.num // i, self.den // i)
            else:
                i += 1
        return self

    def opposite(self):
        return Fraction(self.num * -1, self.den)

    def reciprocal(self):
        return Fraction(self.den, self.num)

    def sqrt(self):
        return Fraction(math.sqrt(self.num), math.sqrt(self.den)).simplify()

    def eval(self):
        return self.num / self.den


class RMath:
    @classmethod
    def add(self, a: Fraction, b: Fraction):
        return Fraction(a.num * b.den + b.num * a.den, a.den * b.den)

    @classmethod
    def subtract(self, a: Fraction, b: Fraction):
        return self.add(a, b.opposite())

    @classmethod
    def multiply(self, a: Fraction, b: Fraction):
        return Fraction(a.num * b.num, a.den * b.den)

    @classmethod
    def divide(self, a: Fraction, b: Fraction):
        return self.multiply(a, b.reciprocal())
