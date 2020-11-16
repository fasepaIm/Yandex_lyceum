print("Какое у вас сегодня настроение?")
a = input()
if ('не' not in a and '?' not in a)\
        and ("хорош" in a or "замечательно" in a or "прекрасно" in a or "отлично" in a):
    print("Отлично, у меня тоже всё хорошо :)")
elif ('не' not in a and '?' not in a)\
        and ("плох" in a or "ужасно" in a or "отвратительное" in a or "отстой" in a):
    print("Ничего, скоро всё наладится")
else:
    print("Извините, я плохо расслышал вас.")