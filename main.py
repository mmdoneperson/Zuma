from constants import *
from frog import Frog
from way import Way


class Game:
    def __init__(self):
        UNITS[COUNTER.get()] = Way()
        UNITS[COUNTER.get()] = Frog()

    def start_game(self):
        pg.display.flip()
        self.update_all()

    def update_all(self):
        while True:
            pg.time.Clock().tick(144)
            screen.fill([255, 255, 255])
            UNITS[3].update()
            for key in UNITS:
                if key == 3:
                    continue
                UNITS[key].update()
            for obj in DELS:
                UNITS.pop(obj.hash)
            DELS.clear()
            pg.display.flip()


if __name__ == "__main__":
    Game().start_game()
