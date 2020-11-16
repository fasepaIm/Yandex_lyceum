from PIL import Image


im = Image.open('image.png')
pixels = im.load()
x, y = im.size

background = pixels[0, 0]
hight = []
width = []
for i in range(x):
    for j in range(y):
        if pixels[i, j] != background:
            width.append(i)
for i in range(y):
    for j in range(x):
        if pixels[j, i] != background:
            hight.append(i)
im2 = im.crop((width[0], hight[0], width[-1] + 1, hight[-1] + 1))
im2.save('res.png')
