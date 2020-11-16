n = int(input())
m = n
k = 1
i = -1
while n != 0:
    if m == 10 and i < 0:
        i = k
    n = int(input())
    m += n
    k += 1
    
print(i)