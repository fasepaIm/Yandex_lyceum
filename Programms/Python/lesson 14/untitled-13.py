a = [i for i in input().split(';')]
for i in a:
    b = (str([int(j) for j in i.split(',') if int(j) >= 1000000000])[1:-1])
    if len(i) > 1:
        b = ','.join([j for j in b.split(', ')])
    print(b)