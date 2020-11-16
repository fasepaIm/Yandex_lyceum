a = input()
b = [int(i) for i in a.split() if i.isdigit()]
c = [i for i in a.split() if not i.isalnum()]
print(b)
print(c)