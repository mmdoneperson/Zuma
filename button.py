import pygame as pg


class Button:
    def __init__(self, funct, x, y, width, height):
        self.funct = funct
        self.rect = pg.rect.Rect(x, y, width, height)
        self.image = None
        self.rect_image = None

    def check_click(self, mouse_point):
        return self.rect.collidepoint(mouse_point)

    def command(self):
        return self.funct()
