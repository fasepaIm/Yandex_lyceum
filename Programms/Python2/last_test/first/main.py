import sys


data = list(map(str.strip, sys.stdin))
for i in range(len(data)):
    while 'ABB' in data[i] or 'CCA' in data[i]:
        if 'ABB' in data[i]:
            v = data[i].replace('ABB', 'CA', 1)
            data[i] = v
        elif 'CCA' in data[i]:
            v = data[i].replace('CCA', 'AB', 1)
            data[i] = v
for i in data:
    print(i)
