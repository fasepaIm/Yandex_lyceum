from PIL import Image, ImageDraw


def gradient(color):
    im = Image.new("RGB", (512, 200), (0, 0, 0))
    drawer = ImageDraw.Draw(im)

    color = color.upper()
    if color == 'R':
        color = 0
    elif color == 'G':
        color = 1
    elif color == 'B':
        color = 2

    lol = 0
    intense = [0, 0, 0]
    for i in range(2, 512):
        if lol == 0:
            lol = im
            intense[color] += 1
        else:
            lol = 0
        drawer.line((i, 0, i, 200), fill=tuple(intense), width=1)

    im.save('res.png')