from PIL import Image


def makeanagliph(filename, delta):
    im = Image.open(filename)
    lol = im.load()
    x, y = im.size

    for i in range(y):
        for j in range(x - delta, x):
            ff = list(lol[j, i])
            ff[0] = 0
            lol[j, i] = tuple(ff)

    for i in range(y):
        for j in range(x - delta - 1, -1, -1):
            r, g, b = lol[j, i]
            lol[j, i] = (0, g, b)
            r1, g1, b1 = lol[j + delta, i]
            lol[j + delta, i] = (r1 + r, g1, b1)

    im.save('res.jpg')


makeanagliph('pep.jpg', 50)