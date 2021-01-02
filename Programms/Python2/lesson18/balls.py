import time

import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Шарики')
    size = width, height = 500, 400
    balls = []
    screen = pygame.display.set_mode(size)

    running = True
    drawing = False
    v = 100 # пикселей в секунду
    fps = 60
    clock = pygame.time.Clock()
    while running: # главный игровой цикл
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                x_pos, y_pos = event.pos
                balls.append([x_pos, y_pos, -1, -1])
        if drawing:
            for i in range(len(balls)):
                pygame.draw.circle(screen, (255, 255, 255), (balls[i][0], balls[i][1]), 10)
                balls[i][0] += v / fps * balls[i][2]
                balls[i][1] += v / fps * balls[i][3]
                if balls[i][0] - 10 <= 0:
                    if balls[i][3] == 1:
                        balls[i][3] = 1
                    balls[i][2] = 1
                elif balls[i][0] + 10 >= width:
                    if balls[i][3] == -1:
                        balls[i][3] = -1
                    balls[i][2] = -1
                elif balls[i][1] - 10 <= 0:
                    balls[i][3] = 1
                elif balls[i][1] + 10 >= height:
                    balls[i][3] = -1
        clock.tick(fps)
        pygame.display.flip()
