import pygame

def draw():
    screen.fill((0, 0, 0))
    color = pygame.Color(0, 0, 0)
    hsv = color.hsva
    color.hsva = (hue, 100, 100, hsv[3])
    pygame.draw.polygon(screen, color, ((150 - w / 2, 150),
                                           (150, 150 - w / 2), 
                                           (150 + w, 150 - w / 2),
                                           (150 + w / 2, 150)))

    color.hsva = (hue, 100, 75, hsv[3])
    pygame.draw.polygon(screen, color, ((150 - w / 2, 150),
                                              (150 + w / 2, 150),
                                              (150 + w / 2, 150 + w),
                                              (150 - w / 2, 150 + w)))

    color.hsva = (hue, 100, 50, hsv[3])
    pygame.draw.polygon(screen, color, ((150 + w / 2, 150),
                                             (150 + w, 150 - w / 2),
                                             (150 + w, 150 + w / 2),
                                             (150 + w / 2, 150 + w)))

def row(x, y):
    pass

def sizes():
    cords = [i for i in input().split()]
    if len(list(filter(lambda x: x.isdigit(), cords))) != 2:
        return False
    elif '.' in cords[0] or '.' in cords[1]:
        return False
    else:
        w, hue = int(cords[0]), int(cords[1])
        if w > 100 or w % 4 != 0 or hue < 0 or hue > 360:
            return False
    return cords

if __name__ == '__main__':
    cords = sizes()
    if cords:
        pygame.init()
        screen = pygame.display.set_mode((300, 300))
        w, hue = int(cords[0]), int(cords[1])
        draw()
        pygame.display.flip()
        pygame.display.set_caption('Куб')
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    else:
        print('Неправильный формат ввода')

