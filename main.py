import pygame as pg
from frog import *

class Game:
    def __init__(self):
        self.units = None

    def start_game(self):
        screen = pg.display.set_mode([1920, 1080])
        screen.fill([255, 255, 255])
        self.units = [Frog(screen)]
        pg.display.flip()
        self.update_all()

    def update_all(self):
        while True:
            for unit in self.units:
                unit.update()
            pg.display.flip()


if __name__ == "__main__":
    Game().start_game()
