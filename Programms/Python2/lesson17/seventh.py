import pygame

def draw():
    screen.fill((255, 255, 255))
    for i in range(0, 12, 2):
        row(0, i)
    for i in range(1, 12, 2):
        row(-15, i)

def row(x, y):
    print(x, y)
    for i in range(300 // 30):
        pygame.draw.rect(screen, pygame.Color(255, 0, 0), (x, y * 15 + y * 2, 30, 15))
        x += 32

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((300, 200))
    draw()
    pygame.display.flip()
    pygame.display.set_caption('Кирпичи')
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
