class Knight():
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row1, col1):
        self.row = row1
        self.col = col1

    def get_color(self):
        return self.color

    def char(self):
        return 'N'

    def can_move(self, row1, col1):
        if not(0 <= row1 < 8 and 0 <= col1 < 8):
            return False
        if abs(self.col - col1) * abs(self.row - row1) == 2 and\
                self.row != row1 and self.col != col1:
            return True
        return False