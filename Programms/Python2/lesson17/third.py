import pygame

def draw():
    screen.fill((255, 0, 0))
    cur_y = 0
    if n % 2 == 0:
        for i in range(n // 2):
            first_white(cur_y)
            cur_y += pix
            first_black(cur_y)
            cur_y += pix
    else:
        for i in range((n + 1) // 2):
            first_black(cur_y)
            cur_y += pix
            if cur_y == a:
                break
            first_white(cur_y)
            cur_y += pix

def first_white(cur_y):
    current_color = pygame.Color('white')
    cur_x = 0
    for i in range(n):
        screen.fill(current_color, (cur_x, cur_y, pix, pix))
        if current_color == pygame.Color('white'):
            current_color = pygame.Color('black')
        else:
            current_color = pygame.Color('white')
        cur_x += pix

def first_black(cur_y):
    current_color = pygame.Color('black')
    cur_x = 0
    for i in range(n):
        screen.fill(current_color, (cur_x, cur_y, pix, pix))
        if current_color == pygame.Color('white'):
            current_color = pygame.Color('black')
        else:
            current_color = pygame.Color('white')
        cur_x += pix

def sizes():
    cords = [i for i in input().split()]
    if len(cords) != 2:
        return False
    elif '.' in cords[0] or '.' in cords[1]:
        return False
    return cords

if __name__ == '__main__':
    cords = sizes()
    if cords:
        # инициализация Pygame:
        pygame.init()
        # размеры окна: 
        a, n = int(cords[0]), int(cords[1])
        pix = a // n
        size = a, a
        # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode(size)
        # формирование кадра:
        # команды рисования на холсте
        draw()
        # ...
        # смена (отрисовка) кадра:
        pygame.display.flip()
        pygame.display.set_caption('Шахматная клетка')
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
        pygame.quit()
    else:
        print('Неправильный формат ввода')

