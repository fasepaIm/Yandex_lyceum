import sys


letters = {}
sas = []
for i in input():
    if i in letters:
        letters[i] += 1
    else:
        letters[i] = 1
words = list(map(str.strip, sys.stdin))
for i in words:
    word = list(i)
    a = set(i)
    z = 0
    for j in a:
        if j in letters and letters[j] >= word.count(j):
            z += 1
            continue
        else:
            z = 0
            break
    if z != 0:
        sas.append(i)
print(len(sas))
for i in sas:
    print(i)