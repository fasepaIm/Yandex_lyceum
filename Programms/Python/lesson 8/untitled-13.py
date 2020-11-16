d = int(input())
v = int(input())
s = input()
x = v - 2
print(s * v)
for i in range(d - 2):
    print(s, " " * x, s, sep='')
print(s * v)