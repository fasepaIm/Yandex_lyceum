import math


def roots_of_quadratic_equation(a, b, c):
    roots = []
    if a == 0 and a != b and a != c:
        return [(-1 * c) / b]
    elif a == b == c == 0:
        return ['all']
    elif a == b == 0:
        return []
    else:
        d = b ** 2 - 4 * a * c
        if d == 0:
            roots.append((-1 * b + math.sqrt(d)) / (2 * a))
        elif d > 0:
            roots.append((-1 * b + math.sqrt(d)) / (2 * a))
            roots.append((-1 * b - math.sqrt(d)) / (2 * a))
        return roots