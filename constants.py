import pygame as pg
import levels
from button import Button
import enum
import system_functions

pg.init()
screen_info = pg.display.Info()
WINDOW_WIDTH = screen_info.current_w
WINDOW_HEIGHT = screen_info.current_h
UNITS = dict()
radius_ball = 40
screen = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

COLORS = [r"image\blueBall.png", r"image\greenBall.png", r"image\purpleBall.png", r"image\redBall.png", r"image\yellowBall.png"]
MENU_BUTTONS = [
    Button(levels.load_level_1, 1375, 154, 390, 159),
    Button(levels.load_level_2, 1326, 364, 436, 116),
    Button(levels.load_level_3, 1298, 541, 452, 110),
    Button(system_functions.close_game, 1247, 705, 526, 174),
]

GAME = []
DELS = []


BUTTON_RETURN_MENU = Button(lambda: GAME[0].start_game(), 1700, 0, 220, 60)
BUTTON_RETURN_MENU.image = pg.transform.scale(pg.image.load(r"image\exit.png"), (180, 70))
BUTTON_RETURN_MENU.rect = BUTTON_RETURN_MENU.image.get_rect(center=pg.Vector2(1810, 30))



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