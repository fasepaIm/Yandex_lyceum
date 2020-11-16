class Note:
    def __init__(self, name, long=False):
        self.name = name
        self.long = long
         
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
        if self.long:
            return notes[self.name]
        else:
            return self.name