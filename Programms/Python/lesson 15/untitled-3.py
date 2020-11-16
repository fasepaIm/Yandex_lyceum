a = [int(i) for i in input().split()]
b = [int(j) for j in input().split()]
print(sum(a[b[0]:b[1] + 1]))