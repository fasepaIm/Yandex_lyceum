import os
import random
import sys
import pygame

# Изображение не получится загрузить 
# без предварительной инициализации pygame
pygame.init()
size = width, height = 600, 300
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Hero(pygame.sprite.Sprite):
    image = load_image("gameover.png")

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. 
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (-1 * self.rect.width, 0)

    def update(self):
        if self.rect.x + self.rect.width < width:
            self.rect.x += v / fps
    
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Game over')
    size = width, height = 600, 300
    running = True
    screen = pygame.display.set_mode(size)
    bomb_image = load_image("gameover.png")

    all_sprites = pygame.sprite.Group()

    Hero(all_sprites)

    v = 200 # количество кадров в секунду
    fps = 60
    clock = pygame.time.Clock()
    while running: # главный игровой цикл
        screen.fill((0, 0, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(fps)
        pygame.display.flip()
