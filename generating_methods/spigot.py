from ratio import Fraction, RMath


# the spigot algorithm can calculate individual digits of pi
# this iteration is an earlier one derived from the Bailey–Borwein–Plouffe formula

# for more algorithmic analysis, and a deeper dive into the math and computing, see
# http://www.cs.ox.ac.uk/people/jeremy.gibbons/publications/spigot.pdf,
# https://vixra.org/pdf/1409.0093v2.pdf

def spigot_algorithm(n):
    pi_sum = Fraction(0, 1)
    for k in range(n):
        const = Fraction(1, 16 ** k)

        s = Fraction(0, 1)
        s = RMath.add(s, Fraction(4, 8 * k + 1))
        s = RMath.add(s, Fraction(-2, 8 * k + 4))
        s = RMath.add(s, Fraction(-1, 8 * k + 5))
        s = RMath.add(s, Fraction(-1, 8 * k + 6))
        pi_sum = RMath.add(pi_sum, RMath.multiply(const, s))
    return pi_sum.eval()


if __name__ == '__main__':
    # n > 10 is enough to approximate pi to the precision of
    # the python math module (17 total digits)
    print(len(str(spigot_algorithm(100))))
    print(f'π ≈ {spigot_algorithm(15)}')
