a = input()
b = int(a)
bolshoy = 0
malenkiy = 190
goden = 0
while a != "!":
    if b >= 150 and b <= 190:
        goden += 1
    if bolshoy < b <= 190:
        bolshoy = b
    if malenkiy > b >= 150:
        malenkiy = b
    a = input()
    if a != "!":
        b = int(a)
print(goden)
print(malenkiy, bolshoy)