import pygame

def draw():
    screen.fill((0, 0, 0))
    x, x_step = 0, 300 / 2 / n
    width, width_step = 300, 300 / n
    for i in range(n):
        pygame.draw.ellipse(screen, pygame.Color('white'), (x, 0, width, 300), 1)
        pygame.draw.ellipse(screen, pygame.Color('white'), (0, x, 300, width), 1)
        x += x_step
        width -= width_step

def sizes():
    cords = input()
    if not cords.isdigit() or '.' in cords:
        return False
    return int(cords)

if __name__ == '__main__':
    cords = sizes()
    if cords:
        pygame.init()
        n = cords
        screen = pygame.display.set_mode((300, 300))
        draw()
        pygame.display.flip()
        pygame.display.set_caption('Сфера')
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    else:
        print('Неправильный формат ввода')
