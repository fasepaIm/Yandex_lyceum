class Balance:
    def __init__(self):
        self.r = 0
        self.d = 0

    def add_right(self, weight):
        self.r += weight

    def add_left(self, weight):
        self.d += weight

    def result(self):
        if self.d == self.r:
            return '='
        if self.d > self.r:
            return 'L'
        if self.d < self.r:
            return 'R'