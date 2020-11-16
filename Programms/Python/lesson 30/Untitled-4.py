from PIL import Image, ImageFilter


def motion_blur(n):
    im = Image.open("image.jpg")
    im2 = im.transpose(Image.ROTATE_270)

    im3 = im2.filter(ImageFilter.GaussianBlur(radius=n))

    im3.save('res.jpg')