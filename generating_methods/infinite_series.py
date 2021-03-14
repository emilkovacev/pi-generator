import math

from ratio import Fraction, RMath


# generate pi from Euler's infinite series to generate pi/4
# this series converges quite slowly
def pi_euler(iterations: int):
    i = 0
    retval = Fraction(1, 1)
    while i < iterations:
        if i % 2 == 0:
            retval = RMath.subtract(retval, Fraction(1, retval.den + 2))
        else:
            retval = RMath.add(retval, Fraction(1, retval.den + 2))
        i += 1
    return RMath.multiply(retval, Fraction(4, 1)).eval()


# the Nilakantha series converges to pi much more quickly
def pi_nilakantha(iterations):
    i = 1
    retval = Fraction(3, 1)
    while i <= iterations:
        if i % 2 == 0:
            # print(f'{retval} + {Fraction(4, (2 * i) * (2 * i + 1) * (2 * i + 2))}')
            retval = RMath.subtract(retval, Fraction(4, (2 * i) * (2 * i + 1) * (2 * i + 2)))
        else:
            # print(f'{retval} - {Fraction(4, (2 * i) * (2 * i + 1) * (2 * i + 2))}')
            retval = RMath.add(retval, Fraction(4, (2*i) * (2*i+1) * (2*i+2)))
        i += 1
    return retval.eval()


if __name__ == '__main__':
    # 25 generations is enough to approximate pi to about 11% accuracy
    print(f'π ≈ {pi_euler(25)}')

    # 100,000 generations is enough to approximate pi to
    # the degree of the python math module (17 total digits)
    print(f'π ≈ {pi_nilakantha(1_000)}')
