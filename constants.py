import pygame as pg
import levels
from button import Button
import system_functions
import counter
import leaderboard

pg.init()
screen_info = pg.display.Info()
WINDOW_WIDTH = screen_info.current_w
WINDOW_HEIGHT = screen_info.current_h
screen = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
radius_ball = 40

GAME = None
REMOVED_BALLS = []
EXPOSED_BALLS = dict()
WAY = None
SCORE = None
FROG = None
ABYSS = None
LEADERBOARD = leaderboard.Leaderboard()
COUNTER = counter.Counter()

BALL_COLORS = [r"image\blueBall.png", r"image\greenBall.png",
          r"image\purpleBall.png", r"image\redBall.png",
          r"image\yellowBall.png"]

BALL_SPRITES = dict()
for color in BALL_COLORS:
    sprite_image = pg.image.load(color).convert_alpha()
    sprite_image = pg.transform.scale(sprite_image, (radius_ball, radius_ball))
    BALL_SPRITES[color] = sprite_image


MENU_BUTTONS = {
    "level1": Button([levels.load_level_1, LEADERBOARD.start_leaderboard], True, 1375, 154, 390, 159),
    "level2": Button([levels.load_level_2, LEADERBOARD.start_leaderboard], True, 1326, 364, 436, 116),
    "level3": Button([levels.load_level_3, LEADERBOARD.start_leaderboard], True, 1298, 541, 452, 110),
    "exit game": Button([system_functions.close_game], True, 1247, 705, 526, 174),

}

LEADERBOARD_BUTTONS = {
    "close leaderboard": Button([LEADERBOARD.close, lambda: GAME.start_game()], False, 0, 0, 100, 100),
    "start level": Button([lambda: GAME.start_level()], False, 0, WINDOW_HEIGHT - 100, 100, 100)
}

# MENU_BUTTONS = [
#     Button(levels.load_level_1, 1375, 154, 390, 159),
#     Button(levels.load_level_2, 1326, 364, 436, 116),
#     Button(levels.load_level_3, 1298, 541, 452, 110),
#     Button(system_functions.close_game, 1247, 705, 526, 174),
#     Button(LEADERBOARD.click, 0, 0, 100, 100)
# ]

BUTTON_RETURN_MENU = Button([LEADERBOARD.close, LEADERBOARD.remember_score, lambda: GAME.start_game()], True, 1700, 0, 220, 60)
BUTTON_RETURN_MENU.image = pg.transform.scale(
    pg.image.load(r"image\exit.png"),
(180, 70))
BUTTON_RETURN_MENU.rect = BUTTON_RETURN_MENU.image.get_rect(
    center=pg.Vector2(1810, 30))


