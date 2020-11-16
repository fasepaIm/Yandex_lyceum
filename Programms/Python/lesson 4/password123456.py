a, b = input(), input()
if len(a) < 8:
    print("Короткий!")
elif "123" in a:
    print("Простой!")
elif a != b:
    print("Различаются.")
else:
    print("OK")
