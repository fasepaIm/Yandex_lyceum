import math


def larger_root(p, q):
    d = discriminant(1, p, q)
    return (-1 * p + math.sqrt(d)) / 2


def smaller_root(p, q):
    d = discriminant(1, p, q)
    return (-1 * p - math.sqrt(d)) / 2


def discriminant(a, b, c):
    return (b ** 2) - (4 * a * c)


def main():
    p = float(input())
    q = float(input())
    print(discriminant(1, p, q))
    print(smaller_root(p, q), larger_root(p, q))