class Button:
    def __init__(self):
        self.clk = 0

    def click(self):
        self.clk += 1

    def click_count(self):
        return self.clk
    
    def reset(self):
        self.clk = 0