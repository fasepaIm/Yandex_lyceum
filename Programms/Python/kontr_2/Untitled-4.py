n = -1


class Doctor:
    def __init__(self, name, healthy, dead):
        self.name = name
        self.healthy = healthy
        self.dead = dead
        
    def __lt__(self, other):
        k = []
        m = other.healthy - other.dead
        n = self.healthy - self.dead
        if m > n and m != n:
            k.append(True)
        elif m < n and m != n:
            k.append(False)
        k.append(other.name > self.name)
        if len(k) == 1:
            return True
        else:
            return False

    def __str__(self):
        return f'Doctor {self.name} - {self.healthy}'
        
    def difference(self):
        return self.healthy - self.dead

    def say_clever_phrases(self):
        global n
        n = n + 1
        phrases = ["The puppet is dead.", 
                   "However, if he wasn't completely dead, it would be a sure sign that he was still alive.",
                   "The puppet is still alive.", 
                   "However, if he were not alive, it would be a sure sign that he was actually dead."]\
        
        return phrases[n]

    def treat_patients(self, name):
        if len(name) % 2 == self.healthy % 2:
            self.healthy += 1
            return True
        else:
            self.dead += 1
            return False


d1 = Doctor('Raven', 3, 5)
d2 = Doctor('Owl', 3, 2)
print(d1, d2, sep='\n')
print(d1 > d2)
print(d2.treat_patients('Pinoccio'))
print(d2.treat_patients('Pinoccio'))
print(d2.treat_patients('Pinoccio'))
print(d2.difference())
print(d1 > d2)
print(d1)
print(d2)