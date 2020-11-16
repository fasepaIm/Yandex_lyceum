def search_for_lilies(image, color):
    pixels = image.load()
    x, y = image.size
    z = []
    for i in range(x):
        v = 0
        for j in range(y):
            if pixels[i, j] == color:
                v += 1
        z.append([i, v])
    z = sorted(z, key=lambda m: (m[1], m[0]))
    d = z[-1][-1]
    z = list(filter(lambda k: k[-1] == d, z))
    z = z[0]
    return z[0] * 1001 // x - 500