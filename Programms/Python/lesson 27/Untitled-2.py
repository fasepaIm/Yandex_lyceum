password = '123'
a = 3


def fib(a):
    print(a)


def check_password(old_func):
    def new_func(*lol):
        global password, a
        ps = input('Введите пароль: ')
        if ps == password:
            old_func(a)
        else:
            print('В доступе отказано')
            return None
    return new_func


fib = check_password(fib)
fib(a)