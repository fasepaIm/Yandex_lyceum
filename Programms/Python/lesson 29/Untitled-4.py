from PIL import Image


def mirror():
    im = Image.open("image.jpg")
    pixels = im.load()
    x, y = im.size
    m = x * 1
 
    for i in range(y):
        if i > 0:
            x -= 1
        for j in range(x - 1, -1, -1):
            pixels[j, i], pixels[m - i - 1, y - j - 1] = pixels[m - i - 1, y - j - 1], pixels[j, i]

    im.save("res.jpg")