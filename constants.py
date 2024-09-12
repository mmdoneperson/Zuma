import pygame as pg
import levels
from button import Button
import system_functions
import counter

pg.init()
screen_info = pg.display.Info()
WINDOW_WIDTH = screen_info.current_w
WINDOW_HEIGHT = screen_info.current_h
screen = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
radius_ball = 40
COLORS = ['blue', 'green', 'purple', 'red', 'yellow']
BONUSES = ['bomb', 'pause', 'reverse', 'speed']
SPRITE_COLORS = [r"image\blueBall.png", r"image\greenBall.png",
                 r"image\purpleBall.png", r"image\redBall.png",
                 r"image\yellowBall.png", r"image\bomb.png",
                 r"image\pause.png", r"image\reverse.png",
                 r"image\speed.png"
                 ]
SPRITES = dict()
for color in SPRITE_COLORS:
    sprite_image = pg.image.load(color).convert_alpha()
    sprite_image = pg.transform.scale(sprite_image, (radius_ball, radius_ball))
    SPRITES[color] = sprite_image

MENU_BUTTONS = [
    Button(levels.load_level_1, 1375, 154, 390, 159),
    Button(levels.load_level_2, 1326, 364, 436, 116),
    Button(levels.load_level_3, 1298, 541, 452, 110),
    Button(system_functions.close_game, 1247, 705, 526, 174),
]
BUTTON_RETURN_MENU = Button(lambda: GAME.start_game(), 1700, 0, 220, 60)
BUTTON_RETURN_MENU.image = pg.transform.scale(
    pg.image.load(r"image\exit.png"),
    (180, 70))
BUTTON_RETURN_MENU.rect = BUTTON_RETURN_MENU.image.get_rect(
    center=pg.Vector2(1810, 30))

GAME = None
REMOVED_BALLS = []
EXPOSED_BALLS = dict()
WAY = None
SCORE = None
FROG = None
ABYSS = None
ACTIVATOR = None
GENERATOR = None
COUNTER = counter.Counter()