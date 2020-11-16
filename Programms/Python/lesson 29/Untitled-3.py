from PIL import Image


def mirror():
    im = Image.open("image.jpg")
    pixels = im.load()
    x, y = im.size
 
    for i in range(y):
        for j in range(x // 2):
            pixels[j, i], pixels[x - j - 1, i] = pixels[x - j - 1, i], pixels[j, i]

    im.save("res.jpg")