with open('castle.txt',encoding='utf-8', mode='r') as line:
    line_f = line.readline().rstrip()
    line = list(''.join(line_f.lower().split()))
    test = sorted(line)
    if line == test:
        result = 'OKAY'
    else:
        for i in range(len(line)):
            if line[i] != test[i]:
                f = line_f.count(' ')
                result = line_f[i + f + 1
                break
res = open('verdict.txt', encoding='utf-8', mode='w')
res.write(result)
res.close()
