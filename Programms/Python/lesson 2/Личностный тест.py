print("Любите ли вы котиков?")
a = input()
print("Умеете ли вы программировать?")
b = input()
if a == "да" and b == "нет":
    print("Вы человек тонкой натуры.")
elif a == "да" and b == "да":
    print("Вы коммуникабельная личность.")
elif a == "нет" and b == "да":
    print("Вы человек с техническим складом ума.")
elif a == "нет" and b == "нет":
    print("Вы человек любящий отрицать.")
else:
    print("Критическая ошибка! Сейчас программа завершит свою работу.")