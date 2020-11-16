def palindrome(s):
    a = s.lower().split()
    b = []
    s = []
    for i in a:
        for j in i:
            if j != ' ':
                s.append(j)
                b.append(j)
    b.reverse()
    if s == b:
        return 'Палиндром'
    else:
        return 'Не палиндром'