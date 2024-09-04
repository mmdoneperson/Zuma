from constants import *
from frog import Frog
from way import Way
from pygame import Vector2
import math


class Game:
    def __init__(self):
        self.vectors = self.circle()
        # length = 900
        # width = 500
        # angle = 1
        # while length > 300:
        #     for i in range(length):
        #         self.vectors.append(Vector2(2 * angle, 0))
        #     for i in range(width):
        #         self.vectors.append(Vector2(0, 2 * angle))
        #     length -= 100
        #     width -= 50
        #     angle *= -1
        UNITS['way'] = Way(self.vectors, Vector2(450, 250))
        UNITS['frog'] = Frog()
        UNITS['frog'].center = Vector2(1340, 400)
        UNITS['frog'].rect.center = Vector2(1340, 400)

    def circle(self):
        vectors = []
        t = 0
        old_x = 900
        old_y = 500
        for i in range(500):
            t += math.pi / 350
            r = (1 + 0.1 * t)
            x = r * math.cos(t)
            y = r * math.sin(t)
            vectors.append(Vector2(-(y - old_y), x - old_x).normalize() * -2)
            old_x = x
            old_y = y
        for i in range(500, 1350):
            t += math.pi / 600
            r = (1 + 0.1 * t)
            x = r * math.cos(t)
            y = r * math.sin(t)
            vectors.append(Vector2(-(y - old_y), x - old_x).normalize() * -2)
            old_x = x
            old_y = y
        for i in range(1350, 2000):
            t += math.pi / 700
            r = (1 + 0.1 * t)
            x = r * math.cos(t)
            y = r * math.sin(t)
            vectors.append(Vector2(-(y - old_y), x - old_x).normalize() * -2)
            old_x = x
            old_y = y
        for i in range(2000, 2800):
            t += math.pi / 1000
            r = (1 + 0.1 * t)
            x = r * math.cos(t)
            y = r * math.sin(t)
            vectors.append(Vector2(-(y - old_y), x - old_x).normalize() * -2)
            old_x = x
            old_y = y
        vectors.reverse()
        return vectors

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
