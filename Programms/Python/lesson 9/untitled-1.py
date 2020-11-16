man = int(input())
namesakes = set()
namesakes2 = set()
a = 0
for i in range(man):
    last_name = input()
    if last_name not in namesakes:
        namesakes.add(last_name)
    elif last_name in namesakes and last_name not in namesakes2:
        a += 2
        namesakes2.add(last_name)
    elif last_name in namesakes2:
        a += 1
print(a)