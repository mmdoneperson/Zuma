import math
import pygame as pg
import constants
import level


def change_angle(i):
    if 0 <= i < 500:
        return math.pi / 350
    if 500 <= i < 1350:
        return math.pi / 600
    if 1350 <= i < 2000:
        return math.pi / 700
    return math.pi / 1000


def get_vectors_for_level1():
    vectors = []
    t = 0
    old_x = 900
    old_y = 500
    for i in range(2800):
        t += change_angle(i)
        r = (1 + 0.1 * t)
        x = r * math.cos(t)
        y = r * math.sin(t)
        vectors.append(pg.Vector2(-(y - old_y), x - old_x).normalize() * -2)
        old_x = x
        old_y = y
    vectors.reverse()
    return vectors


def download():
    constants.GAME.level = level.Level(
        get_vectors_for_level1(),
        pg.Vector2(450, 250),
        pg.Vector2(1340, 400),
        pg.transform.scale(
            pg.image.load("levels/level1/first_map.png"),
            (constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)).convert(),
        "level 1")
