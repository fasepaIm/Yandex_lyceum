def reverse():
    data = open('input.dat', mode='rb').read()
    a = list(data)
    a.reverse()

    text = open('output.dat', mode='wb')
    text.write(bytes(a))
    text.close()
