def matrix(n=1, m=-1, a=0):
    if m == -1:
        m = n
    lol = [[a] * m for i in range(n)]
    return lol