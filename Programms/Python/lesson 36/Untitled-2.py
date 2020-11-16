class LeftParagraph:
    def __init__(self, num):
        self.size = num
        self.txt = []
        self.ends = []
        self.line = ''

    def add_word(self, word):
        self.txt.append(word)
        
    def end(self):
        for i in self.txt:
            if self.line:
                if len(self.line) + len(i) + 1 <= self.size:
                    self.line += ' ' + i
                else:
                    self.ends.append(self.line)
                    self.line = i
            else:
                self.line = i
        if i == self.txt[-1]:
            self.ends.append(self.line)
        for i in self.ends:
            print(i)
        self.txt.clear()
        self.ends.clear()
        self.line = ''


class RightParagraph:
    def __init__(self, num2):
        self.size2 = num2
        self.txt2 = []
        self.ends2 = []
        self.line2 = ''

    def add_word(self, word2):
        self.txt2.append(word2)

    def end(self):
        for j in self.txt2:
            if self.line2:
                if len(self.line2) + len(j) + 1 <= self.size2:
                    self.line2 += ' ' + j
                else:
                    self.ends2.append(self.line2)
                    self.line2 = j
            else:
                self.line2 = j 
        if j == self.txt2[-1]:
            self.ends2.append(self.line2)      
        for j in self.ends2:
            print(j.rjust(self.size2, ' '))
        self.txt2.clear()
        self.ends2.clear()
        self.line2 = ''