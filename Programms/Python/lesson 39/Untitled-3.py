class Triangle():
    def __init__(self, len1, len2, len3):
        self.len1 = len1
        self.len2 = len2
        self.len3 = len3
    
    def perimeter(self):
        return self.len1 + self.len2 + self.len3


class EquilateralTriangle(Triangle):
    def __init__(self, len0):
        super().__init__(len0, len0, len0)