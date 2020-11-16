import sys

listt = sys.stdin.readlines()
for i in range(len(listt)):
    listt[i] = listt[i].lstrip()
print(len(list(filter(lambda x: x != '' and x[0] == '#', listt))))