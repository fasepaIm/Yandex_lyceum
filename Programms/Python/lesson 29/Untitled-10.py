from PIL import Image, ImageDraw

im = Image.new('RGB', (355, 100))
drawer = ImageDraw.Draw(im)
drawer.rectangle(((0, 0), (177.5, 100)), 'White')
drawer.rectangle(((177.5, 0), (355, 100)), 'Black')
drawer.polygon(((10, 5),
                (10, 95),
                (90, 95),
                (90, 77),
                (30, 77),
                (30, 59),
                (90, 59),
                (90, 41),
                (30, 41),
                (30, 23),
                (90, 23),
                (90, 5),
                (10, 5)),
               'Black')

drawer.polygon(((100, 5),
                (100, 95),
                (120, 95),
                (120, 23),
                (175, 23),
                (175, 5),
                (100, 5)),
               'Black')

drawer.ellipse([185, 5, 265, 95], fill=None, outline='White', width=20)

drawer.polygon(((275, 5),
                (275, 95),
                (295, 95),
                (295, 5),
                (275, 5)),
               'White')

drawer.ellipse([275, 5, 345, 68], fill=None, outline='White', width=20)

im.save('name.png')