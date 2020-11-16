class OddEvenSeparator:
    def __init__(self):
        self.nums = []

    def add_number(self, count):
        self.nums.append(count)

    def even(self):
        return [str(i) for i in self.nums if i % 2 == 0]

    def odd(self):
        return [str(i) for i in self.nums if i % 2 != 0]