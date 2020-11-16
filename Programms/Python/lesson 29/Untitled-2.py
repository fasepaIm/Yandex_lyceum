from PIL import Image
 
im = Image.open("image.jpg")
pixels = im.load()
x, y = im.size
r, g, b = 0, 0, 0
m = 0
 
for i in range(x):  
    for j in range(y):
        a, v, c = pixels[i, j]
        r += a
        g += v
        b += c
        m += 1     
print(r // m, g // m, b // m)