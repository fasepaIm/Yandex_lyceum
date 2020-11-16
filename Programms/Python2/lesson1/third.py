string, a = input(), int(input())
if a > 0:
    if a > len(string):
        a = a % len(string)
    first_string = string[a::] + string[:a]
    third_string = string[len(string) - a:] + string[:len(string) - a]
else:
    a = abs(a)
    if abs(a) > len(string):
        a = abs(a) % len(string)
    first_string = string[len(string) - a:] + string[:len(string) - a]
    third_string = string[a::] + string[:a]
print(first_string, string, third_string, sep='\n')