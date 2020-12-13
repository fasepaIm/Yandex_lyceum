import pygame

def draw():
    screen.fill(pygame.Color('yellow'))
    for j in range(1, screen_sizes[1] // n + 1):
        draw_string(j)

def draw_string(j):
    for i in range(1, screen_sizes[0] // n + 1):
        pygame.draw.polygon(screen, pygame.Color('orange'), ((n * i - n, n * j - n + n // 2),
                                                             (n * i - n + n // 2, n * j - n),
                                                             (n * i, n * j - n + n // 2),
                                                             (n * i - n + n // 2, n * j)))

def sizes():
    size = input()
    if not size.isdigit() or '.' in size:
        return False
    return int(size)

if __name__ == '__main__':
    size = sizes()
    if size:
        pygame.init()
        n = size
        screen_sizes = (300, 300)
        screen = pygame.display.set_mode(screen_sizes)
        draw()
        pygame.display.flip()
        pygame.display.set_caption('Ромбики')
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    else:
        print('Неправильный формат ввода')
