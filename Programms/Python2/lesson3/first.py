N = 7  
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]  
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]  
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


class Note:
    def __init__(self, name, is_long=False):
        self.name = name
        self.is_long = is_long
        notes = {
            'до': 'до-о',
            'ре': 'ре-э',
            'ми': 'ми-и',
            'фа': 'фа-а',
            'соль': 'со-оль',
            'ля': 'ля-а',
            'си': 'си-и'
        }
        if self.is_long:
            self.name = notes[self.name]

    def need(self, x):
        if x not in PITCHES:
            return PITCHES[LONG_PITCHES.index(x)]
        else:
            return x

    def __str__(self):
        return self.name

    def __lshift__(self, x):  # x<<y
        if x > len(PITCHES):
            if x % len(PITCHES) != 0:
                x = x % len(PITCHES)
            else:
                x = 0
        if self.name in PITCHES:
            if PITCHES.index(self.name) - x >= 0:
                return Note(PITCHES[PITCHES.index(self.name) - x])
            else:
                return Note(PITCHES[len(PITCHES) - (x - PITCHES.index(self.name))])
        else:
            if LONG_PITCHES.index(self.name) - x >= 0:
                return Note(LONG_PITCHES[LONG_PITCHES.index(self.name) - x])
            else:
                return Note(LONG_PITCHES[len(LONG_PITCHES) - (x - LONG_PITCHES.index(self.name))])

    def __rshift__(self, x):  # x>>y
        if x > len(PITCHES) - 1:
            x = x % len(PITCHES)
        if self.name in PITCHES:
            if PITCHES.index(self.name) + x < len(PITCHES) - 1:
                return Note(PITCHES[PITCHES.index(self.name) + x])
            else:
                return Note(PITCHES[0 + (x - (len(PITCHES) - PITCHES.index(self.name)))])
        else:
            if LONG_PITCHES.index(self.name) + x < len(LONG_PITCHES) - 1:
                return Note(LONG_PITCHES[LONG_PITCHES.index(self.name) + x])
            else:
                return Note(LONG_PITCHES[0 + (x - (len(LONG_PITCHES) -
                                              LONG_PITCHES.index(self.name)))])
    
    def __lt__(self, y):  # x<y
        return PITCHES.index(self.need(self.name)) < PITCHES.index(self.need(y.name))

    def __le__(self, y):  # x<=y
        return PITCHES.index(self.need(self.name)) <= PITCHES.index(self.need(y.name))

    def __eq__(self, y):  # x==y
        return PITCHES.index(self.need(self.name)) == PITCHES.index(self.need(y.name))

    def __ne__(self, y):  # x!=y
        return PITCHES.index(self.need(self.name)) != PITCHES.index(self.need(y.name))

    def __gt__(self, y):  # x>y
        return PITCHES.index(self.need(self.name)) > PITCHES.index(self.need(y.name))

    def __ge__(self, y):  # x>=y
        return PITCHES.index(self.need(self.name)) >= PITCHES.index(self.need(y.name))

    def get_interval(self, x):
        return INTERVALS[abs(PITCHES.index(self.need(self.name)) - PITCHES.index(self.need(x.name)))]


class LoudNote(Note):
    def __str__(self):
        return super().__str__().upper()
    

class DefaultNote(Note):
    def __init__(self, name='до', is_long=False):
        super().__init__(name, is_long)


class NoteWithOctave(Note):
    def __init__(self, name, octave, is_long=False):
        self.octave = octave
        super().__init__(name, is_long)
        
    def __str__(self):
        return f'{super().__str__()} ({self.octave})'