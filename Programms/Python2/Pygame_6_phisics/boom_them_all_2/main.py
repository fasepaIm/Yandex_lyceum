import os
import sys
import random
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


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb2.png")
    image_boom = load_image("boom.png")

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, width - 120)
        self.rect.y = random.randrange(0, height - 144)
        print(pygame.sprite.spritecollide(self, self.rect, True))

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Boom them all — 2')
    size = width, height = 500, 500
    running = True
    screen = pygame.display.set_mode(size)
    bomb_image = load_image("bomb2.png")

    all_sprites = pygame.sprite.Group()

    for _ in range(20):
        Bomb(all_sprites)

    while running: # главный игровой цикл
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.draw(screen)
        all_sprites.update(event)
        pygame.display.flip()
