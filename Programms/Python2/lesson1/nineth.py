hours = sorted([int(i) for i in input().split()])
minutes = sorted([int(i) for i in input().split()])
for i in range(len(hours)):
    if len(str(hours[i])) == 1:
        hours[i] = '0' + str(hours[i])
    for j in range(len(minutes)):
        if len(str(minutes[j])) == 1:
            minutes[j] = '0' + str(minutes[j])
        if  int(str(hours[i])[0]) + int(str(hours[i])[-1]) != int(str(minutes[j])[0]) + int(str(minutes[j])[-1]):
            print(f'{hours[i]}:{minutes[j]}')
