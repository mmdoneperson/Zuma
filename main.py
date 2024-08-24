from constants import *
from frog import *


class Game:
    def __init__(self):
        self.units = None

    def start_game(self):
        screen = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
        screen.fill([255, 255, 255])
        self.units = [Frog(screen)]
        pg.display.flip()
        self.update_all()

    def update_all(self):
        while True:
            pg.time.Clock().tick(60)
            for unit in self.units:
                unit.update()
            pg.display.flip()


if __name__ == "__main__":
    Game().start_game()
