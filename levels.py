import math
import constants
from pygame import Vector2
import pygame as pg


class Level:
    def __init__(self, vectors, start_point, frog_point, map_background):
        self.vectors = vectors
        self.starting_point_of_way = start_point
        self.frog_point = frog_point
        self.map_background = map_background


def load_level_1():
    vectors = []
    t = 0
    old_x = 900
    old_y = 500
    for i in range(2800):
        t += change_angle(i)
        r = (1 + 0.1 * t)
        x = r * math.cos(t)
        y = r * math.sin(t)
        vectors.append(Vector2(-(y - old_y), x - old_x).normalize() * -2)
        old_x = x
        old_y = y
    vectors.reverse()
    return Level(
        vectors,
        Vector2(450, 250),
        Vector2(1340, 400),
        pg.transform.scale(
            pg.image.load("first_map.png"),
            (constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)).convert())

def change_angle(i):
    if 0 <= i < 500:
        return math.pi / 350
    if 500 <= i < 1350:
        return math.pi / 600
    if 1350 <= i < 2000:
        return math.pi / 700
    return math.pi / 1000



def load_level_2():
    vectors = [Vector2(2,0)] * 27
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
    return Level(vectors, Vector2(-20, 100), Vector2(
        constants.WINDOW_WIDTH // 2, constants.WINDOW_HEIGHT // 2),
                 pg.transform.scale(
                     pg.image.load("map_road.png"),
                     (constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)).convert()
                 )


def load_level_3():
    vectors = []

    for t in range(1, 1400):
        x = abs(t / 100 * math.cos(t / 100))
        y = t / 100 * math.sin(t / 100)
        vectors.append(Vector2(x, y).normalize() * 2)
    for i in range(300):
        vectors.append(Vector2(0, 2))
    for t in range(500, 1850):
        x = -abs(t / 100 * math.cos(t / 100))
        y = -t / 100 * math.sin(t / 100)
        vectors.append(Vector2(x, y).normalize() * 2)
    return Level(vectors, Vector2(-20, 100), Vector2(
        848, 546),
                 pg.transform.scale(
                     pg.image.load("map_sin.png"),
                     (constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)).convert()
                 )
