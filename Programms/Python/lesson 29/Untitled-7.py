from PIL import Image, ImageDraw


def board(num, size):
    new_color = (256, 256, 256)  
    im = Image.new("RGB", (num * size, num * size), new_color)
    drawer = ImageDraw.Draw(im)

    for i in range(0, (num * size - size + 1), size * 2):
        for j in range(0, (num * size - size + 1), size * 2):
            drawer.rectangle([j, i, j + size - 1, i + size - 1], fill='Black')
    
    for i in range(size, (num * size - size + 1), size * 2):
        for j in range(size, (num * size - size + 1), size * 2):
            drawer.rectangle([j, i, j + size - 1, i + size - 1], fill='Black')

    im.save('res.png')


board(8, 50)