g = int(input())
goroda = set()
a = "OK"
for i in range(g + 1):
    gorod = input()
    if gorod in goroda:
        a = 'TRY ANOTHER'
    else:
        goroda.add(gorod)
print(a)