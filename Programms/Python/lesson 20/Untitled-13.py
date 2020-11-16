def catalan(n):
    c = [1]
    for j in range(1, n + 1):
        ccc = 0
        for i in range(j):
            cc = c[i] * c[j - i - 1]
            ccc += cc
        c.append(ccc)
    return c[n]