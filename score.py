import constants
import pygame as pg


class Score:
    def __init__(self, max_score):
        self.score = 0
        self.max_score = max_score
        self.is_full = False

    def add(self, point):
        self.score += point
        if self.score >= self.max_score:
            self.score = self.max_score
            if not self.is_full:
                constants.WAY.is_spawn = False
                constants.WAY.reverse()
            self.is_full = True

    def update(self):
        black = (0, 0, 0)
        green = (0, 255, 0)
        black_rect = [20, 20, 150, 40]
        length_green = self.score * 120 / self.max_score
        green_rect = [35, 25, length_green, 30]
        pg.draw.rect(constants.screen, black, black_rect)
        pg.draw.rect(constants.screen, green, green_rect)
