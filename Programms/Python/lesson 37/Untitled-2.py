class ReversedList:
    def __init__(self, lst):
        self.rl = lst[::-1]

    def __len__(self):
        return len(self.rl)

    def __getitem__(self, key):
        return self.rl[key]