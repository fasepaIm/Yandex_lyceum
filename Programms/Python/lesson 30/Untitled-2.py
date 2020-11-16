from PIL import Image


def transparency(a, b):
    im = Image.open(a)
    imm = Image.open(b)
    pixels1 = im.load()
    pixels2 = imm.load()
    x, y = im.size

    for i in range(y):
        for j in range(x):
            r1, g1, b1 = pixels1[j, i]
            r2, g2, b2 = pixels2[j, i]
            pix = (int(r1 * 0.5 + r2 * 0.5), int(g1 * 0.5 + g2 * 0.5), int(b1 * 0.5 + b2 * 0.5))
            pixels1[j, i] = pix

    im.save('res.jpg')