import pygame

class Text():
    DEFAULT_FONT = pygame.font.Font('Assets/BergenMono-Regular.otf', size=20)

    def __init__(self, window, text: str, text_color: tuple, background_color, x: int, y: int, font=DEFAULT_FONT):
        self.window = window
        self.text = text
        self.text_color = text_color
        self.background_color = background_color
        self.font = font
        self.image = font.render(text, True, text_color, background_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update_text(self, text):
        self.text = text
        self.image = self.font.render(text, True, self.text_color, self.background_color)
        self.rect = self.image.get_rect()

    def draw(self):
        self.window.blit(self.image, self.rect.topleft)

    def get_rect(self):
        return self.rect

class Button(Text):
    def __init__(self, window, text: str, text_color: tuple, background_color: tuple, x: int, y: int, func, font=Text.DEFAULT_FONT):
        super().__init__(window, text, text_color, background_color, x, y)
        self.func = func

    def check_pressed(self, pos):
        if super().get_rect().collidepoint(pos):
            self.func()