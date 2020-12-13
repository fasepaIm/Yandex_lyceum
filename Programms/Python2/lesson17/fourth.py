import pygame

def draw():
    screen.fill((0, 0, 0))
    colors = ['red', 'green', 'blue']
    for i in range(n, 0, -1):
        pygame.draw.circle(screen, pygame.Color(f'{colors[0]}'), (circle, circle), w * i)
        colors.append(colors[0])
        del colors[0]

def sizes():
    cords = [i for i in input().split()]
    if len(list(filter(lambda x: x.isdigit(), cords))) != 2:
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
        w, n = int(cords[0]), int(cords[1])
        size = w * n * 2, w * n * 2
        circle = w * n
        # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode(size)
        # формирование кадра:
        # команды рисования на холсте
        draw()
        # ...
        # смена (отрисовка) кадра:
        pygame.display.flip()
        pygame.display.set_caption('Мишень')
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
        pygame.quit()
    else:
        print('Неправильный формат ввода')
