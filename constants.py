import pygame as pg

pg.init()
screen_info = pg.display.Info()
WINDOW_WIDTH = screen_info.current_w
WINDOW_HEIGHT = screen_info.current_h
UNITS = []
radius_ball = 40

screen = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
screen.fill([255, 255, 255])

COLORS = ['purpleBall.png', 'redBall.png', 'yellowBall.png', 'greenBall.png', 'blueBall.png']