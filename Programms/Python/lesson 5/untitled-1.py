b = 0
print("Какое у вас сегодня настроение?")
b = 1
a = input()
while "Всё" not in a or "всё" not in a or "Пока" not in a or "пока" not in a or\
        "До свидания" not in a or "до свидания" not in a or\
        "До встречи" not in a or "до встречи" not in a:
    if "Всё" in a or "всё" in a or "Пока" in a or "пока" in a or\
            "До свидания" in a or "до свидания" in a or "До встречи" in a or "до встречи" in a:
        print("Всего хорошего. Не болейте.")
        break
    elif ('не' not in a and '?' not in a)\
            and ("хорош" in a or "замечательно" in a or "прекрасно" in a or
                 "отлично" in a or "норм" in a or "Норм" in a):
        print("Отлично, у меня тоже всё хорошо :)")
    elif ('не' not in a and '?' not in a)\
            and ("плох" in a or "ужасно" in a or "отвратительно" in a or "отстой" in a):
        print("Ничего, скоро всё наладится")
    else:
        print("Извините, я плохо расслышал вас.")
    if b == 1:
        print("Как вы себя чувствуете?")
        b = 2
    elif b == 2:
        print("Как у вас дела?")
        b = 0
    elif b == 0:
        print("Какое у вас сегодня настроение?")
        b = 1
    a = input()