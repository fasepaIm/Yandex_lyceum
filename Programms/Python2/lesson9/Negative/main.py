with open('input.bmp', mode='rb') as img:
    name = img.read(54)
    res = [255 - i for i in img.read()]
    with open("res.bmp", mode="wb") as result:
        result.write(name)
        result.write(bytes(res))
