from constants import *


class Abyss:
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length - 500

    def update(self):
        yellow = (114, 116, 118)
        black = (0, 0, 0)
        pg.draw.circle(screen, yellow, (self.x, self.y), 50, 0)
        if len(UNITS['way'].snakes[0].balls) > 0:
            index = UNITS['way'].snakes[0].balls[0].index_way
            if index >= self.length:
                pg.draw.circle(screen, black, (self.x, self.y), 50 * (index - self.length) / 500, 0)
