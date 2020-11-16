block = ["а", "о", "у", "ы", "и", "э", "е", "ё", "ю", "я",
         "А", "О", "У", "Ы", "И", "Э", "Е", "Ё", "Ю", "Я"]


def translate(text):
    global block, translated_text
    a = text.split()
    end = []
    for i in a:
        strr = ''
        for j in i:
            if j not in block and j.isalpha():
                strr += j
        if len(strr) != 0:
            end.append(strr)
    translated_text = ' '.join(end)
    return translated_text