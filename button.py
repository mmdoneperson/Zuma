import pygame as pg


class Button:
    def __init__(self, functions, x, y, width, height):
        self.functions = functions
        self.rect = pg.rect.Rect(x, y, width, height)
        self.image = None
        self.rect_image = None
        self.sound = pg.mixer.Sound(r"sounds\button1.ogg")

    def check_click(self, mouse_point):
        return self.rect.collidepoint(mouse_point)

    def command(self):
        self.sound.play()
        for function in self.functions:
            function()

