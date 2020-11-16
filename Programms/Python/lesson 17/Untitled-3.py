a = '''A	.-
B	-...
C	-.-.
D	-..
E	.
F	..-.
G	--.
H	....
I	..
J	.---
K	-.-
L	.-..
M	--
N	-.
O	---
P	.--.
Q	--.-
R	.-.
S	...
T	-
U	..-
V	...-
W	.--
X	-..-
Y	-.--
Z	--..'''
az = {}
a = a.split('\n')
for i in a:
    az[i.split('\t')[0]] = i.split('\t')[1]
c = input().upper()
f = [i for i in c.split()]
for i in f:
    k = list(i)
    print(' '.join(az[j] for j in k))
print()