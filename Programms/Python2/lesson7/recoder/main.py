import os

cyrillic_symbols = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
                    "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
                    "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
                    "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
                    "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
                    "б": "b", "ю": "ju", "ё": "jo"
                    }
new_text = []
text = open('cyrillic.txt', encoding='utf-8')
lines = text.readlines()
for i in range(len(lines)):
    if cyrillic_symbols.keys() & set(lines[i]):
        line = ''
        for j in range(len(lines[i])):
            if lines[i][j].lower() in cyrillic_symbols:
                if lines[i][j] == lines[i][j].upper():
                    line += cyrillic_symbols[lines[i][j].lower()].capitalize()
                else:
                    line += cyrillic_symbols[lines[i][j]]
            else:
                line += lines[i][j]
        new_text.append(line)
    else:
        new_text.append(lines[i])
text.close()
text = open('transliteration.txt', encoding='utf-8', mode='w')
for i in new_text:
    text.write(i)
text.close()
