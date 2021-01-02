class DefaultList(list):
    def __init__(self, default_value):
        list.__init__(self)
        self.default_value = default_value

    def __getitem__(self, i):
        try:
            return list.__getitem__(self, i)
        except IndexError:
            return self.default_value

    def extend(self, addition):
        list.extend(self, addition)
