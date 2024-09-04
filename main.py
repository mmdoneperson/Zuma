from constants import *
from frog import Frog
from way import Way
from pygame import Vector2


class Game:
    def __init__(self):
        self.vectors = []
        length = 900
        width = 500
        angle = 1
        while length > 300:
            for i in range(length):
                self.vectors.append(Vector2(2 * angle, 0))
            for i in range(width):
                self.vectors.append(Vector2(0, 2 * angle))
            length -= 100
            width -= 50
            angle *= -1
        UNITS['way'] = Way(self.vectors, Vector2(30, 30))
        UNITS['frog'] = Frog()

    def start_game(self):
        pg.display.flip()
        self.update_all()

    def update_all(self):
        while True:
            pg.time.Clock().tick(60)
            screen.fill([255, 255, 255])
            UNITS['way'].draw_road()
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
