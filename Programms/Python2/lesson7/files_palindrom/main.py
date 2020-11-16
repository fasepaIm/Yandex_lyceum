def palindrome():
    text = open('input.dat', mode='rb').read().splitlines()
    strings = [list(i) for i in text]
    strings = [x for xs in strings for x in xs]
    strings2 = strings.copy()
    strings2.reverse()
    if strings == strings2:
        return True
    else:
        return Fale
