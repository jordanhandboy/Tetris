import pygame
from pygame.locals import *

class TetrisController:
    def __init__(self, tetris_game):
        self.tetris_game = tetris_game

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                self.handle_keydown(event.key)

    def handle_keydown(self, key):
        if key == K_LEFT:
            self.tetris_game.move_left()
        elif key == K_RIGHT:
            self.tetris_game.move_right()
        elif key == K_DOWN:
            self.tetris_game.move_down()
        elif key == K_UP:
            self.tetris_game.rotate_right()