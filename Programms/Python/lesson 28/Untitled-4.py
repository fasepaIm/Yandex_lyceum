from datetime import timedelta, datetime


now = datetime.now()
birthday = now + timedelta(days=int(input()))
birthday = birthday.strftime("%Y-%m-%d")
print(*[int(birthday.split('-')[2]), int(birthday.split('-')[1])])