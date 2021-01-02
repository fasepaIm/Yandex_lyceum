import string


bad_combinations_line = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm',
                         'йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']
errors = {
    'LengthError': 0,
    'LetterError': 0,
    'DigitError': 0,
    'SequenceError': 0,
    'WordError': 0,
}
errors_name = ['DigitError', 'LengthError', 'LetterError', 'SequenceError', 'WordError']

with open("top-9999-words.txt", encoding="utf8") as file:
    vocabluary_words = [i[:-1] for i in file.readlines()]


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


class WordError(PasswordError):
    pass


class CheckPassword():
    def __init__(self, password):
        self.password = password

    def length_error_check(self):
        if len(self.password) < 9:
            errors['LengthError'] += 1
            raise LengthError()

    def letter_error_check(self):
        for c in string.punctuation:
            self.password = self.password.replace(c, "")
        if any([f'{self.password}l'.islower(), self.password.isupper()]):
            errors['LetterError'] += 1
            raise LetterError()

    def digit_error_check(self):
        if not any(map(str.isdigit, self.password)):
            errors['DigitError'] += 1
            raise DigitError()

    def sequence_error_check(self):
        self.password = self.password.lower()
        if any(sum([list(map(lambda n: self.password[i:i + 3] in n, bad_combinations_line))
                    for i in range(len(self.password) - 2)], [])):
            errors['SequenceError'] += 1
            raise SequenceError()
    
    def word_error_check(self):
        for i in vocabluary_words:
            if i in self.password:
                errors['WordError'] += 1
                raise WordError()


with open("top 10000 passwd.txt", encoding="utf8") as passwords_file:
    passwords = [i.split()[0] for i in passwords_file.readlines()]
    for passwd in passwords:
        try:
            test = CheckPassword(passwd)
            test.length_error_check()
        except LengthError:
            pass
        
        try:
            test.letter_error_check()
        except LetterError:
            pass
        
        try:
            test.digit_error_check()
        except DigitError:
            pass
        
        try:
            test.sequence_error_check()
        except SequenceError:
            pass

        try:
            test.word_error_check()
        except WordError:
            pass

for i in errors_name:
    print(f'{i} - {errors[i]}')
