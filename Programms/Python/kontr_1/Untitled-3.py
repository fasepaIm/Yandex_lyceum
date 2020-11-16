a = input().split('/:-[')
b = input().split(':-|')
c = []
for i in a:
    d = []
    g = set(i)
    for j in b:
        gg = set(j)
        if len(g & gg) == 2:
            d.append(j)
    if len(d) != 0:
        v = ', '.join(d)
        v_ = i + ': ' + v
    else:
        v_ = i + ': ' + 'таких слов нет'
    c.append(v_)
for i in c:
    print(i)