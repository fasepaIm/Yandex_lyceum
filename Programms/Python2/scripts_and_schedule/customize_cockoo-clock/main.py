import datetime


import schedule


def job():
    hour = int(str(datetime.datetime.now().time()).split(':')[0])
    i = hour % 12 if hour % 12 else 12
    if need_range != 'no':
        a, b = map(int, need_range.split('-'))
        if hour < a and hour > b:
            print(f'{message} ' * i)
    else:
        print(f'{message} ' * i)


schedule.every().hour.at(":00").do(job)


message = input("Введите необходимое сообщение: ")
need_range = input("Введите диапазон тишины (если ничего не надо выводить - напишите: 'no'): ")
while True:
    schedule.run_pending()
