import pygame
import random


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        for _ in range(height):
            row = []
            for n in range(width):
                row.append(random.randint(1, 2))
            self.board.append(row)
        # значения по умолчанию
        self.left = 15
        self.top = 15
        self.cell_size = 30
        self.runner = 1

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255), (x * self.cell_size + self.left,
                                                           y * self.cell_size + self.top,
                                                           self.cell_size, self.cell_size), 1)
                if self.board[y][x] == 1:
                    pygame.draw.ellipse(screen, (0, 0, 255), (x * self.cell_size + self.left + 2,
                                                              y * self.cell_size + self.top + 2,
                                                              self.cell_size - 4, self.cell_size - 4))
                elif self.board[y][x] == 2:
                    pygame.draw.ellipse(screen, (255, 0, 0), (x * self.cell_size + self.left + 2,
                                                              y * self.cell_size + self.top + 2,
                                                              self.cell_size - 4, self.cell_size - 4))

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        cords = ((x - self.left) // self.cell_size, (y - self.top) // self.cell_size)
        if cords[0] <= self.width - 1 and cords[1] <= self.height - 1:
            return cords
        else:
            return None

    def on_click(self, cell_coords):
        if cell_coords:
            if self.board[cell_coords[1]][cell_coords[0]] == self.runner:
                for i in range(self.width):
                    self.board[cell_coords[1]][i] = self.runner
                for i in range(self.height):
                    if i != cell_coords[1]:
                        self.board[i][cell_coords[0]] = self.runner
                if self.runner == 1:
                    self.runner = 2
                else:
                    self.runner = 1


    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


if __name__ == '__main__':
    pygame.init()
    #board = Board(4, 3)
    #board.set_view(100, 100, 50)
    n = int(input())
    board = Board(n, n)
    running = True
    size = width, height = (n + 1) * 30, (n + 1) * 30
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Недореверси')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
