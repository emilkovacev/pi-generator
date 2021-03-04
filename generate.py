import math
import random


# inspired by Matt Parker: https://youtu.be/RZBhSi_PwHU
def generate_pi(samples=100_000, r=120):
    count = 0
    for _ in range(samples):
        a = random.randint(1, r)
        b = random.randint(1, r)
        if math.gcd(a, b) == 1:
            count += 1
    p = count / samples
    pi = math.sqrt(6 / p)
    precision = (math.pi - pi) / pi * 100
    return pi, precision
