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


class Arrow(pygame.sprite.Sprite):
    image = load_image("arrow.png")

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. 
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Arrow.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pygame.mouse.get_pos()

    def update(self, *args):
        if pygame.mouse.get_focused():
            if args and args[0].type == pygame.MOUSEMOTION:
                pygame.mouse.set_visible(False)
                self.rect.x, self.rect.y = pygame.mouse.get_pos()
        else:
            self.rect.x = -100
        

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Свой курсор мыши')
    size = width, height = 500, 400
    running = True
    screen = pygame.display.set_mode(size)
    bomb_image = load_image("arrow.png")

    all_sprites = pygame.sprite.Group()

    Arrow(all_sprites)

    while running: # главный игровой цикл
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.draw(screen)
        all_sprites.update(event)
        pygame.display.flip()
