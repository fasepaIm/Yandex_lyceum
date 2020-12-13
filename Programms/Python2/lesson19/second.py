import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                                               self.cell_size, self.cell_size), 1)
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                                               self.cell_size, self.cell_size))

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        cords = ((x - self.left) // self.cell_size, (y - self.top) // self.cell_size)
        if cords[0] <= self.width - 1 and cords[1] <= self.height - 1 and cords[0] >= 0 and cords[1] >= 0:
            return cords
        else:
            return None

    #def on_click(self, cell_coords):
    #    if self.board[cell_coords[1]][cell_coords[0]] == 0:
    #        self.board[cell_coords[1]][cell_coords[0]] = 1
    #    else:
    #        self.board[cell_coords[1]][cell_coords[0]] = 0

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        print(cell)
    #    self.on_click(cell)


if __name__ == '__main__':
    pygame.init()
    #board = Board(4, 3)
    #board.set_view(100, 100, 50)
    board = Board(5, 7)
    running = True
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Координаты клетки')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
