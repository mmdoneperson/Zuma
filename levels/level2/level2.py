import pygame as pg
import constants
import level


def get_vectors_for_level2():
    vectors = [pg.Vector2(2, 0)] * 27
    length = 900
    width = 430
    angle = 1
    while length > 300:
        for i in range(length):
            vectors.append(pg.Vector2(2 * angle, 0))
        for i in range(width):
            vectors.append(pg.Vector2(0, 2 * angle))
        length -= 100
        width -= 50
        angle *= -1
    return vectors


def download():
    constants.GAME.level = level.Level(
        get_vectors_for_level2(),
        pg.Vector2(-20, 100),
        pg.Vector2(constants.WINDOW_WIDTH // 2, constants.WINDOW_HEIGHT // 2),
        pg.transform.scale(pg.image.load("levels/level2/map_road.png"),
                           (constants.WINDOW_WIDTH,
                            constants.WINDOW_HEIGHT)).convert(),
        "level 2"
    )
