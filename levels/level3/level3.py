import pygame as pg
import math
import constants
import level


def get_vectors_for_level3():
    vectors = []
    for t in range(1, 1400):
        x = abs(t / 100 * math.cos(t / 100))
        y = t / 100 * math.sin(t / 100)
        vectors.append(pg.Vector2(x, y).normalize() * 2)
    for i in range(300):
        vectors.append(pg.Vector2(0, 2))
    for t in range(500, 1835):
        x = -abs(t / 100 * math.cos(t / 100))
        y = -t / 100 * math.sin(t / 100)
        vectors.append(pg.Vector2(x, y).normalize() * 2)
    return vectors


def download():
    constants.GAME.level = level.Level(
        get_vectors_for_level3(),
        pg.Vector2(-20, 100),
        pg.Vector2(848, 546),
        pg.transform.scale(
            pg.image.load("levels/level3/map_sin.png"),
            (constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)).convert(),
        "level 3")
