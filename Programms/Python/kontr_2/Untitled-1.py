import sys


alll = {}
data = sys.stdin.readlines()
name = []
for i in data:
    drug = i.split(':')
    if drug[-1][1:-1] not in alll:
        alll[drug[-1][1:-1]] = drug[0]
        name.append(drug[-1][1:-1])
    else:
        if drug[0] not in alll[drug[-1][1:-1]]:
            alll[drug[-1][1:-1]] += '-' + drug[0]
for i in range(len(name)):
    print(name[i] + ' - ' + ' # '.join(alll[name[i]].split('-')))