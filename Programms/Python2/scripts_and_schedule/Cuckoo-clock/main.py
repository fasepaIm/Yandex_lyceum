import datetime


import schedule


def job():
    hour = int(str(datetime.datetime.now().time()).split(':')[0])
    i = hour % 12 if hour % 12 else 12
    print('Ку ' * i)


schedule.every().hour.at(":00").do(job)


while True:
    schedule.run_pending()
