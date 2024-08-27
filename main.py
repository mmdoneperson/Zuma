from constants import *
from frog import Frog
from way import Way


class Game:
    def __init__(self):
        UNITS.append(Frog())
        UNITS.append(Way())

    def start_game(self):
        pg.display.flip()
        self.update_all()

    def update_all(self):
        while True:
            pg.time.Clock().tick(144)
            screen.fill([255, 255, 255])
            for unit in UNITS:
                unit.update()
            pg.display.flip()


if __name__ == "__main__":
    Game().start_game()
