def eratosthenes(N):
    simple = 0
    n = 0
    f = 0
    end = []
    cnt = [i for i in range(2, N + 1)]
    while n == 0:
        for i in cnt:
            if i > simple:
                simple = i
                break
        if f == simple:
            break
        m = []
        for i in range(len(cnt)):
            if cnt[i] % simple == 0 and cnt[i] != simple:
                end.append(cnt[i])
                m.append(cnt[i])
        cnt = list(set(cnt) - set(m))
        f = simple
    print(' '.join([str(i) for i in end]))