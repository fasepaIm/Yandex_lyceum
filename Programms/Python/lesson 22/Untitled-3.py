z = [5, 10, 15, 55, 63, 1, 8]
print(f'Изначальный список_1 {z}')
a = sorted([5, 10, 15, 55, 63, 1, 8])  # переменная a принимает
print(f'Конченый список: {a}')  # значение отсортированного списка
  

b = [5, 10, 15, 55, 63, 1, 8]
print(f'Изначальный список_2 {b}')
b.sort()  # здесь мы сортируем уже имеющийся список
print(f'Конченый список_2: {b}')