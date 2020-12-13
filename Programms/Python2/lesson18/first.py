import time

import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Жёлтый круг')
    size = width, height = 500, 400
    screen = pygame.display.set_mode(size)

    running = True
    drawing = False
    v = 10 # пикселей в секунду
    clock = pygame.time.Clock()
    while running: # главный игровой цикл
        screen.fill((0, 0, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                x_pos, y_pos = event.pos
                circle_size = 0
        if drawing:
            pygame.draw.circle(screen, pygame.Color('Yellow'), (x_pos, y_pos), circle_size)
            circle_size += v * clock.tick() / 1000
        pygame.display.flip()
