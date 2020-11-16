a, b, c, d = int(input()), int(input()), input(), int(input())
f = 'удачно'
if c == 'песок' and d >= a:
    f = 'обидно'
if c == 'река' and d < a >= b:
    f = 'обидно'
if c == 'перебросить' and d < b:
    f = 'обидно'
print(f)