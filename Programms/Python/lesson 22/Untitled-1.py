words = []


def parrot(phrase):
    global words
    if phrase in words:
        print(phrase)
    else:
        words.append(phrase)