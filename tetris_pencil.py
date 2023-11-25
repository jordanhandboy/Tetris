import pygame
from tetris_game import *

class TetrisPencil:
    def __init__(self, window, game):
        self.window = window
        self.game = game
        self.game.add_view(self)

    def draw_board(self):
        white = (255, 255, 255)
        black = (15, 15, 15)
        board = self.game.get_board()
        x = 0
        y = 0
        for line in board:
            x = 0
            y += 20
            for cell in line:
                x += 20
                cell_rect = (x, y, 20, 20)
                if cell == 1:
                    pygame.draw.rect(self.window, white, cell_rect)
                if cell == 0:
                    pygame.draw.rect(self.window, black, cell_rect)