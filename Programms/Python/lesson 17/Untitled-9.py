phone = {}
a = ['Нет', 'в', 'телефонной', 'книге']
for i in range(int(input())):
    b = input().split()
    if b[-1] in phone:
        phone[b[-1]].append(b[0])
    if b[-1] not in phone:
        phone[b[-1]] = []
        phone[b[-1]].append(b[0])
for i in range(int(input())):
    print(' '.join(phone.get(input(), a)))