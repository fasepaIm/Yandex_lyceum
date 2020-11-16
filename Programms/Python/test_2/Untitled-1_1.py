def remove_inappropriate(spells):
    lol = []
    speels = list(filter(lambda x: len(x.split()) < 3, spells))
    spells[:], speels[:] = speels[:], spells[:]
    speels = []
    for i in spells:
        lol.append(set(i.lower()))
    for i in range(len(spells)):
        if len(spells[i]) != len(lol[i]):
            speels.append(spells[i])
    spells[:], speels[:] = speels[:], spells[:]