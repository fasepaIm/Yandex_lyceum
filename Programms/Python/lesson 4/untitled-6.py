correct = -1
while correct == -1:
    password1 = input()
    password2 = input()
    if len(password1) < 8:
        print("Короткий!")
        continue
    elif "123" in password1:
        print("Простой!")
        continue
    elif password1 != password2:
        print("Различаются.")
        continue
    elif password1 == password2:
        print("OK")
        break