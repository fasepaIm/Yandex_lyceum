a = [i for i in input().split(input())][-1]
if '&' in a:
    a = a[1:a.find('&')]
else:
    a = a[1:]
print(a)