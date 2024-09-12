import constants
import pygame as pg


class Abyss:
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length - 500
        self.image = pg.transform.scale(
            pg.image.load("image/end.png"), (150, 150))
        self.rect_image = self.image.get_rect(center=(self.x - 2, self.y - 2))

    def update(self):
        black = (0, 0, 0)
        constants.screen.blit(self.image, self.rect_image)
        if len(constants.WAY.snakes) > 0 and len(constants.WAY.snakes[0].balls) > 0:
            index = constants.WAY.snakes[0].balls[0].index_way
            if index >= self.length:
                pg.draw.circle(constants.screen,
                               black,
                               (self.x, self.y),
                               38 * (index - self.length) / 500,
                               0)