def print_long_words(text):
    text = ''.join([i.lower() if i.isalpha() else ' ' for i in text]).lower().split()
    for i in text:
        x = 0
        for j in i:
            if j == 'а' or j == 'о' or j == 'э' or j == 'и' or j == 'у'\
                    or j == 'ы' or j == 'е' or j == 'ё' or j == 'ю' or j == 'я'\
                    or j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u' or j == 'y':
                x += 1
        if x >= 4:
            print(i)