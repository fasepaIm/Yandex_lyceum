lol = ''


def print_without_duplicates(message):
    global lol
    if message != lol:
        print(message)
        lol = message