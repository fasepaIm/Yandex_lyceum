import string


bad_combinations_line = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm',
                         'йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']
error_message = 'error'
true_message = 'ok'


def check_password(password):
    try:
        assert len(password) > 8
        for c in string.punctuation:
            password = password.replace(c, "")
        assert not any([password.islower(), password.isupper()])
        password = password.lower()
        assert not any([password.isalpha(), password.isdigit()])
        assert not any(sum([list(map(lambda n: password[i:i + 3] in n, bad_combinations_line))
                            for i in range(len(password) - 2)], []))
        return true_message
    except AssertionError:
        return error_message


print(check_password(input()))
