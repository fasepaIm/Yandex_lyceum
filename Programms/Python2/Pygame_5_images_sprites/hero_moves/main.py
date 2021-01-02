import os
import random
import sys
import pygame

# Изображение не получится загрузить 
# без предварительной инициализации pygame
pygame.init()
size = width, height = 500, 500
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
    image = load_image("creature.png")

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. 
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (0, 0)

    def update(self, args):
        if pygame.key.get_pressed()[pygame.K_RIGHT]: 
            self.rect.x += 10
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x -= 10
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.rect.y -= 10
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.rect.y += 10

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Герой двигается!')
    size = width, height = 300, 300
    running = True
    screen = pygame.display.set_mode(size)
    bomb_image = load_image("creature.png")

    all_sprites = pygame.sprite.Group()

    Hero(all_sprites)

    while running: # главный игровой цикл
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                all_sprites.update(event)
        all_sprites.draw(screen)
        #all_sprites.update(event)
        pygame.display.flip()
