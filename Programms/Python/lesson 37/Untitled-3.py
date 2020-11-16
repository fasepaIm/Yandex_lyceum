class SquareFunction:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __call__(self, args):
        return self.a * args ** 2 + self.b * args + self.c