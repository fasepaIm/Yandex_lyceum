from random import sample

simbols = '23456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'


def generate_password(m, n=1, z=1):
    lol = []
    for i in range(n):
        password = ''.join(sample(simbols, m))
        while password in lol:
            password = ''.join(sample(simbols, m))
        lol.append(password)
    if z == 1:
        return lol[0]
    else:
        return lol


def main(n, m):
    return [i for i in generate_password(m, n, z=2)]