pi = 3.14159


def circle_length(radius):
    return 2 * (pi * radius)


def circle_area(radius):
    return pi * (radius ** 2)


def main():
    rad = float(input())
    print(circle_length(rad), circle_area(rad))