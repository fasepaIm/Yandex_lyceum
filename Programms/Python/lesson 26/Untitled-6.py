import sys

listt = sys.stdin.readlines()


def gematr(word):
    gem = 0
    for i in word:
        gem += ord(i) - ord('А')
    return gem
        

for i in range(len(listt)):
    listt[i] = [[gematr(listt[i])] + [listt[i]]]
    print(listt[i])