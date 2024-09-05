import pygame as pg
import levels
from button import Button
import enum

pg.init()
screen_info = pg.display.Info()
WINDOW_WIDTH = screen_info.current_w
WINDOW_HEIGHT = screen_info.current_h
UNITS = dict()
radius_ball = 40
screen = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
screen.fill([255, 255, 255])

COLORS = ['purpleBall.png', 'redBall.png', 'yellowBall.png', 'greenBall.png', 'blueBall.png']
BUTTONS = [
    Button(levels.load_level_1, 1375, 154, 390, 159),
    Button(levels.load_level_2, 1326, 364, 436, 116),
    Button(levels.load_level_3, 1298, 541, 452, 110),
    Button(lambda: None, 1247, 705, 526, 174)
]

DELS = []

SPRITES = dict()
for color in COLORS:
    sprite_image = pg.image.load(color).convert_alpha()
    sprite_image = pg.transform.scale(sprite_image, (radius_ball, radius_ball))
    SPRITES[color] = sprite_image

class Counter:
    def __init__(self):
        self.counter = 0

    def get(self):
        self.counter += 1
        return self.counter - 1


COUNTER = Counter()


class Status(enum.Enum):
    Stop = 'Stop'
    Forward = 'Forward'
    Back = 'Back'
