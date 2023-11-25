import pygame
from pygame.locals import *

class TetrisController:
    def __init__(self, game):
        self.game = game
        self.down_timer = pygame.time.get_ticks()
        self.fall_speed = 1000

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                self.handle_keydown(event.key)

    def handle_keydown(self, key):
        if key == K_LEFT:
            self.game.move_left()
        elif key == K_RIGHT:
            self.game.move_right()
        elif key == K_DOWN:
            self.game.move_down()
        elif key == K_SPACE:
            self.game.drop()
        elif key == K_UP:
            self.game.rotate_right()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.down_timer > self.fall_speed:
            self.game.move_down()
            self.down_timer = current_time