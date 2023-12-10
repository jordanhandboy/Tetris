import pygame
from tetris_game import *
from text import *

class TetrisPencil:
    CELL_SIZE = 25
    OUTLINE_SIZE = 4
    def __init__(self, window, game):
        self.window = window
        self.game = game
        self.game.add_view(self)

    def draw_everything(self):
        self.draw_board()
        self.draw_score()
        self.draw_instructions()
        self.draw_next_block()
        self.draw_hold()

    def draw_board(self):
        white = (255, 255, 255)
        gray = (15, 15, 15)
        board = self.game.get_board()
        x = 250
        y = 50
        for line in board:
            curr_x = x
            for cell in line:
                cell_rect = (curr_x+TetrisPencil.OUTLINE_SIZE, y+TetrisPencil.OUTLINE_SIZE, TetrisPencil.CELL_SIZE-TetrisPencil.OUTLINE_SIZE, TetrisPencil.CELL_SIZE-TetrisPencil.OUTLINE_SIZE)
                if cell[0] == 1:
                    pygame.draw.rect(self.window, cell[1], cell_rect)
                if cell[0] == 0:
                    pygame.draw.rect(self.window, gray, cell_rect)
                curr_x += TetrisPencil.CELL_SIZE
            y += TetrisPencil.CELL_SIZE

    def draw_piece(self, piece, x, y):
        for line in piece.get_shape():
            curr_x = x
            for cell in line:
                cell_rect = (curr_x+TetrisPencil.OUTLINE_SIZE, y+TetrisPencil.OUTLINE_SIZE, TetrisPencil.CELL_SIZE-TetrisPencil.OUTLINE_SIZE, TetrisPencil.CELL_SIZE-TetrisPencil.OUTLINE_SIZE)
                if cell == 1:
                    pygame.draw.rect(self.window, piece.get_color(), cell_rect)
                curr_x += TetrisPencil.CELL_SIZE
            y += TetrisPencil.CELL_SIZE

    def draw_next_block(self):
        white = (255, 255, 255)
        x = 250
        next_text = Text(self.window, f"Next:", white, (0, 0, 0), TetrisPencil.CELL_SIZE*10+x+30, 80)
        next_text.draw()
        self.draw_piece(self.game.get_bag()[-1], TetrisPencil.CELL_SIZE*10+x+30, 110)
        self.draw_piece(self.game.get_bag()[-2], TetrisPencil.CELL_SIZE*10+x+30, 170)
        self.draw_piece(self.game.get_bag()[-3], TetrisPencil.CELL_SIZE*10+x+30, 230)

    def draw_hold(self):
        white = (255, 255, 255)
        x = 150
        next_text = Text(self.window, f"Hold:", white, (0, 0, 0), x, 80)
        next_text.draw()
        if self.game.get_held_piece() != 0:
            self.draw_piece(self.game.get_held_piece(), x, 110)

    def draw_instructions(self):
        white = (255, 255, 255)
        x = 250
        instructions_text1 = Text(self.window, f"Movement: W,A,S,D", white, (0, 0, 0), TetrisPencil.CELL_SIZE*10+x+30, 470)
        instructions_text2 = Text(self.window, f"Rotation: K,L", white, (0, 0, 0), TetrisPencil.CELL_SIZE*10+x+30, 500)
        instructions_text3 = Text(self.window, f"Drop: Space", white, (0, 0, 0), TetrisPencil.CELL_SIZE*10+x+30, 530)
        instructions_text1.draw()
        instructions_text2.draw()
        instructions_text3.draw()

    def draw_score(self):
        white = (255, 255, 255)
        x = 250
        score = self.game.get_lines_cleared()
        score_text = Text(self.window, f"Score: {score}", white, (0, 0, 0), TetrisPencil.CELL_SIZE*10+x+30, 400)
        score_text.draw()
        