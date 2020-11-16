import random
import sys
from random import choice
from pprint import pprint


def secret(children):
    chop = children[:]
    chill = [i for i in range(len(children))]
    chel = chill[:]
    chil = chill[:]
    for i in chel:
        lol = chill[:]
        if i in lol:
            del lol[lol.index(i)]
        a = choice(lol)
        chil[i] = a
        del chill[chill.index(a)]
    for i in range(len(children)):
        children[i] = [children[i], chop[chil[i]]]
    for i in children:
        print(' - '.join(i))


secret(list(map(str.strip, sys.stdin)))