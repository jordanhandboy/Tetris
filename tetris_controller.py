import pygame
from pygame.locals import *

class TetrisController:
    def __init__(self, game):
        self.game = game
        self.down_timer = pygame.time.get_ticks()
        self.move_timer = pygame.time.get_ticks()
        self.fall_speed = 1000
        self.move_delay = 100

    def handle_events(self):
        keys = pygame.key.get_pressed()

        if keys[K_LEFT] or keys[K_a]:
            self.handle_continuous_move(self.game.move_left)

        if keys[K_RIGHT] or keys[K_d]:
            self.handle_continuous_move(self.game.move_right)

        if keys[K_DOWN] or keys[K_s]:
            self.handle_continuous_move(self.game.move_down)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                self.handle_keydown(event.key)

    def handle_keydown(self, key):
        if key == K_SPACE:
            self.game.drop()
        elif key == K_k:
            self.game.rotate_left()
        elif key == K_UP or key == K_l:
            self.game.rotate_right()
        elif key == K_LSHIFT:
            self.game.hold_piece()

    def handle_continuous_move(self, move_function):
        current_time = pygame.time.get_ticks()
        if current_time - self.move_timer > self.move_delay:
            move_function()
            self.move_timer = current_time

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.down_timer > self.fall_speed:
            if not self.game.move_down():
                self.game.drop()
            self.down_timer = current_time