def password_level(password):
    if len(password) < 6:
        return 'Недопустимый пароль'
    if not password.isdigit() and not password.isalpha():
        if password.islower() or password.isupper():
            return 'Слабый пароль'
        if not password.isalpha():
            return 'Надежный пароль'
    if password.isdigit():
        return 'Ненадежный пароль'
    if password.isalpha():
        if password.isupper() or password.islower():
            return 'Ненадежный пароль'
        if not password.isupper() or not password.islower():
            return 'Слабый пароль'