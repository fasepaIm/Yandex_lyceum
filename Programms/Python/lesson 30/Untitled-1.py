from PIL import Image


def twist_image(input_ﬁle_name, output_ﬁle_name):
    im = Image.open(input_ﬁle_name)
    pixels = im.load()
    x, y = im.size

    for i in range(y):
        for j in range(x // 2):
            pixels[j, i], pixels[x // 2 + j, i] = pixels[x // 2 + j, i], pixels[j, i]

    im.save(output_ﬁle_name)