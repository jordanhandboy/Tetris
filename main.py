import pygame
import sys
from tetris_pencil import *
from tetris_controller import *

pygame.init()

screen = None

fps = 60

def main():
    global screen
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tetris")
    game_loop()

def game_loop():
    game = TetrisGame()
    pencil = TetrisPencil(screen, game)
    controller = TetrisController(game)
    game.add_block(BlockCreator.create_block(0))
    while True:

        controller.handle_events()
        
        pencil.draw_board()

        pygame.display.flip()
        pygame.time.Clock().tick(fps)

def start_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()