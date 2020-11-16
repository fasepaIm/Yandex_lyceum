a = int(input())
b = a // 100
c = a % 10
d = a // 10
e = d % 10
f = (b + e)
g = (e + c)
m = str(f)
n = str(g)
if f > g:
    print(m + n)
if g > f:
    print(n + m)
if f == g:
    print(m + n)