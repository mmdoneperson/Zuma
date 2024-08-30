import pygame as pg
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

DELS = []
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

