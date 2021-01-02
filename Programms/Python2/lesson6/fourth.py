import string


bad_combinations_line = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm',
                         'йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']
error_message = 'error'
true_message = 'ok'


def check_password(password):
    if len(password) <= 8:
        return error_message
    for c in string.punctuation:
        password = password.replace(c, "")
    if any([password.islower(), password.isupper()]):
        return error_message
    password = password.lower()
    if any([password.isalpha(), password.isdigit()]):
        return error_message
    if any(sum([list(map(lambda n: password[i:i + 3] in n, bad_combinations_line))
                for i in range(len(password) - 2)], [])):
        return error_message
    else:
        return true_message


print(check_password(input()))
