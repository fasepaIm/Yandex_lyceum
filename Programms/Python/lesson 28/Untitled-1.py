import random
from random import sample
from pprint import pprint


def make_bingo():
    binn = sample(range(1, 76), 25)
    bingo = []
    for i in range(5):
        bingo.append(binn[:5])
        del binn[:5]
    bingo[2][2] = 0
    bingo = tuple([tuple(bingo[i]) for i in range(len(bingo))])
    return bingo