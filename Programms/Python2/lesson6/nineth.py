import string


bad_combinations_line = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm',
                         'йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']
true_message = 'ok'
farewell_phrase = 'Bye-Bye'
special_password = 'Ctrl+Break'
password_request = True


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


def check_password(password):
    if password == special_password:
        raise KeyboardInterrupt
    elif len(password) < 9:
        raise LengthError()
    for c in string.punctuation:
        password = password.replace(c, "")
    if any([f'{password}l'.islower(), password.isupper()]):
        raise LetterError()
    password = password.lower()
    if any([password.isalpha(), password.isdigit()]):
        raise DigitError()
    elif any(sum([list(map(lambda n: password[i:i + 3] in n, bad_combinations_line))
                  for i in range(len(password) - 2)], [])):
        raise SequenceError()
    else:
        return true_message


while True:
    try:
        print(check_password(input()))
        break
    except KeyboardInterrupt:
        print(farewell_phrase)
        break
    except Exception as error:
        print(error.__class__.__name__)
