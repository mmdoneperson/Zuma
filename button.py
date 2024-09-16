import pygame as pg


class Button:
    def __init__(self, functions, is_active, x, y, width, height):
        self.functions = functions
        self.rect = pg.rect.Rect(x, y, width, height)
        self.image = None
        self.rect_image = None
        self.sound = pg.mixer.Sound(r"sounds\button1.ogg")
        self.is_active = is_active

    def check_click(self, mouse_point):
        return self.rect.collidepoint(mouse_point) and self.is_active

    def command(self):
        self.sound.play()
        for function in self.functions:
            function()