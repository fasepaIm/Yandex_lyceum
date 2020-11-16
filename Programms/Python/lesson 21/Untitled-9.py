jokes = []


def print_only_new(message):
    global jokes
    if message not in jokes:
        jokes.append(message)
        print(message)