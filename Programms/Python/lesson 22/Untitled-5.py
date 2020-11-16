def mirror(arr): 
    mirrored_part = []
    for i in range(-1, (len(arr) + 1) * -1, -1):
        mirrored_part.append(arr[i])
    arr += mirrored_part
# создаём новый список mirrored_part и засовываем туда элементы arr в обратном порядке
# затем прибавляем к arr mirrored_part и выводим