people = {}
for i in range(int(input())):
    a = input().split()
    if a[-1] in people:
        people[a[-1]].append(a[0])
        people[a[-1]].sort()
    if a[-1] not in people:
        people[a[-1]] = []
        people[a[-1]].append(a[0])
for i in range(int(input())):
    a = input()
    if a in people:
        print(' '.join(people[a]))
    else:
        print()