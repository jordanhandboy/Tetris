import pygame
import sys

pygame.init()

from tetris_pencil import *
from tetris_controller import *

# Import the pygame.font module
import pygame.font

screen = None

fps = 60

def main():
    global screen
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tetris")
    start_screen()

def game_loop():
    game = TetrisGame()
    pencil = TetrisPencil(screen, game)
    controller = TetrisController(game)
    game.next_block()
    while True:
        if not game.get_running():
            # Use "DejaVu Sans" font here
            Text(screen, "Game Over", (255, 255, 255), (125, 125, 125), 270, 100, pygame.font.SysFont("DejaVuSans", size=40)).draw()
            break
        screen.fill((0, 0, 0))
        controller.handle_events()
        controller.update()

        pencil.draw_everything()

        pygame.display.flip()
        pygame.time.Clock().tick(fps)

def start_screen():
    def leave():
        pygame.quit()
        sys.exit()
    start_button = Button(screen, "Start", (0, 0, 0), (255, 255, 255), 350, 200, game_loop)
    exit_button = Button(screen, "Exit", (0, 0, 0), (255, 255, 255), 355, 400, leave)
    buttons = [start_button, exit_button]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leave()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for button in buttons:
                    button.check_pressed(pos)
        for button in buttons:
            button.draw()
        pygame.display.flip()

if __name__ == "__main__":
    main()

