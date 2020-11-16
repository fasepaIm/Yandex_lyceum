PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]


class Note:
    def __init__(self, name, is_long=False):
        self.name = name
        self.is_long = is_long

    def __str__(self):
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
            return notes[self.name]
        else:
            return self.name


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
