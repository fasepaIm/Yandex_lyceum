class BaseObject():
    def __init__(self, x, y, z):
        self.block = [x, y, z]

    def get_coordinates(self):
        return self.block


class Block(BaseObject):
    def shatter(self):
        self.block = [None, None, None]


class Entity(BaseObject):
    def move(self, x, y, z):
        self.block = [x, y, z]


class Thing(BaseObject):
    pass