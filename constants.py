import pygame as pg
from pygame import Vector2

pg.init()
screen_info = pg.display.Info()
WINDOW_WIDTH = screen_info.current_w
WINDOW_HEIGHT = screen_info.current_h
UNITS = []
radius_ball = 20
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
purple = (128, 0, 255)

screen = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
screen.fill([255, 255, 255])

COLORS = [green, yellow, blue, red, purple]