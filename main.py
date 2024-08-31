from constants import *
from frog import Frog
from way import Way
from pygame import Vector2


class Game:
    def __init__(self):
        self.vectors = []
        for i in range(10000):
            self.vectors.append(Vector2(2, 0))
        UNITS['way'] = Way(self.vectors, Vector2(30,30))
        UNITS['frog'] = Frog()

    def start_game(self):
        pg.display.flip()
        self.update_all()

    def update_all(self):
        while True:
            pg.time.Clock().tick(144)
            screen.fill([255, 255, 255])
            UNITS['frog'].update()
            for key in UNITS:
                if key == 'frog' or key == 'way':
                    continue
                UNITS[key].update()
            UNITS['way'].update()
            for obj in DELS:
                UNITS.pop(obj.hash)
            DELS.clear()
            pg.display.flip()


if __name__ == "__main__":
    Game().start_game()
