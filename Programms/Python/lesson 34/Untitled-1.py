import sys


test, data1 = [], []
data = sys.stdin.read()
data = ''.join([i if i.isalpha() else ' ' for i in data])
data = list(filter(lambda word: word[-1] == word[-1].capitalize(), enumerate(data.split())))
for i in data:
    if i[-1] not in test:
        test.append(i[-1])
        data1.append([str(i[0]), str(i[-1])])
data1 = sorted(data1, key=lambda x: x[-1])
for i in data1:
    print(' - '.join(i))