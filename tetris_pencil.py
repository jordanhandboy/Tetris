import pygame
from tetris_game import *
from text import *

class TetrisPencil:
    def __init__(self, window, game):
        self.window = window
        self.game = game
        self.game.add_view(self)

    def draw_board(self):
        white = (255, 255, 255)
        gray = (15, 15, 15)
        board = self.game.get_board()
        cell_size = 25
        outline_size = 4
        x = 200
        y = 50
        for line in board:
            curr_x = x
            for cell in line:
                cell_rect = (curr_x+outline_size, y+outline_size, cell_size-outline_size, cell_size-outline_size)
                if cell[0] == 1:
                    pygame.draw.rect(self.window, cell[1], cell_rect)
                if cell[0] == 0:
                    pygame.draw.rect(self.window, gray, cell_rect)
                curr_x += cell_size
            y += cell_size

        score = self.game.get_lines_cleared()
        score_text = Text(self.window, f"Score: {score}", white, (0, 0, 0), cell_size*10+x+30, 200)
        score_text.draw()
        