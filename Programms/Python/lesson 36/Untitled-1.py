class Selector:
    def __init__(self, num):
        self.cnt = num[:]

    def get_odds(self):
        return list(filter(lambda x: x % 2 != 0, self.cnt))

    def get_evens(self):
        return list(filter(lambda x: x % 2 == 0, self.cnt))