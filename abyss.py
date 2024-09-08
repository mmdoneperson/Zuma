from constants import *


class Abyss:
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length - 500
        self.image = pg.transform.scale(pg.image.load("end.png"), (150, 150))
        self.rect_image = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        black = (0, 0, 0)
        screen.blit(self.image, self.rect_image)
        if len(UNITS['way'].snakes[0].balls) > 0:
            index = UNITS['way'].snakes[0].balls[0].index_way
            if index >= self.length:
                pg.draw.circle(screen, black, (self.x, self.y), 40 * (index - self.length) / 500, 0)
