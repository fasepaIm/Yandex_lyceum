import pygame

def draw():
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (0, 0), (width, height), 5)
    pygame.draw.line(screen, (255, 255, 255), (0, height), (width, 0), 5)

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
        width, height = int(cords[0]), int(cords[1])
        size = width, height
        # screen — холст, на котором нужно рисовать:
        screen = pygame.display.set_mode(size)
        # формирование кадра:
        # команды рисования на холсте
        draw()
        # ...
        # смена (отрисовка) кадра:
        pygame.display.flip()
        pygame.display.set_caption("Крест")
        # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
        pygame.quit()
    else:
        print('Неправильный формат ввода')
