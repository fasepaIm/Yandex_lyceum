def take_large_banknotes(banknotes):
    lol = []
    for i in banknotes:
        if i > 10:
            lol.append(i)
    return lol