from random import choices
import string

simbols = '23456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'


def generate_password(m, n=1, z=1):
    lol = []
    for i in range(n):
        password = ''.join(choices(string.digits[2:]) + choices(simbols, k=m - 1))
        while password in lol or password.upper() == password or password.lower() == password:
            password = ''.join(choices(string.digits[2:]) + choices(simbols, k=m - 1))
        lol.append(password)
    if z == 1:
        return lol[0]
    else:
        return lol


def main(n, m):
    return [i for i in generate_password(m, n, z=2)]