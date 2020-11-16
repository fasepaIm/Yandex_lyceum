people = input().split(' -> ')
for i in range(int(input())):
    go = []
    num = people.index(input())
    if num != 0:
        go.append(people[num - 1])
    go.append(people[num])
    if num != len(people) - 1:
        go.append(people[num + 1])
    print(' -> '.join(go))