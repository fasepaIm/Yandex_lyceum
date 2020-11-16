a = int(input())
count = []
count_ = []
for i in range(a):
    count.append(int(input()))
for i in range(a - 1):
    for j in range(i, a):
        b = count[i] + count[j]
        if b % 2 != 0:
            count_.append(b)
if len(count_) != 0:
    print(max(count_))
else:
    print('-1')