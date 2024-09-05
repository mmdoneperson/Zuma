import math
import constants
from pygame import Vector2


class Level:
    def __init__(self, vectors, start_point, frog_point):
        self.vectors = vectors
        self.starting_point_of_way = start_point
        self.frog_point = frog_point


def load_level_1():
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
    return Level(vectors, Vector2(450, 250), Vector2(1340, 400))


def load_level_2():
    vectors = []
    length = 900
    width = 430
    angle = 1
    while length > 300:
        for i in range(length):
            vectors.append(Vector2(2 * angle, 0))
        for i in range(width):
            vectors.append(Vector2(0, 2 * angle))
        length -= 100
        width -= 50
        angle *= -1
    return Level(vectors, Vector2(30, 100), Vector2(
        constants.WINDOW_WIDTH // 2, constants.WINDOW_HEIGHT // 2))


def load_level_3():
    vectors = []

    for t in range(1, 1400):
        x = abs(t / 100 * math.cos(t / 100))
        y = t / 100 * math.sin(t / 100)
        vectors.append(Vector2(x, y).normalize() * 2)
    for i in range(300):
        vectors.append(Vector2(0, 2))
    for t in range(500, 1890):
        x = -abs(t / 100 * math.cos(t / 100))
        y = -t / 100 * math.sin(t / 100)
        vectors.append(Vector2(x, y).normalize() * 2)
    return Level(vectors, Vector2(40, 100), Vector2(
        848, 546))
