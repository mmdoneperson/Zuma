from constants import *
from pygame import Vector2
import random


class Ball:
    def __init__(self, center, size=radius_ball):
        self.size = size
        self.direction = Vector2(0, 0)
        self.color = COLORS[random.randint(0, 4)]
        self.center = center
        self.index_way = None
        self.sprite_image = pg.transform.scale(pg.image.load(self.color), (size, size))
        self.rect = self.sprite_image.get_rect(center=self.center)
        self.is_shoot = False
        self.hash = COUNTER.get()
        screen.blit(self.sprite_image, self.rect)

    def update_direction(self, direction):
        self.direction = direction

    def draw(self, center):
        self.center = center
        self.sprite_image = pg.transform.scale(pg.image.load(self.color), (self.size, self.size))
        self.rect = self.sprite_image.get_rect(center=self.center)
        screen.blit(self.sprite_image, self.rect)

    def update(self):
        self.center += self.direction
        self.rect = self.sprite_image.get_rect(center=self.center)
        screen.blit(self.sprite_image, self.rect)
        if self.is_shoot:
            UNITS[0].check_collision(self)

    def change_color(self, color):
        self.color = color
        self.sprite_image = pg.transform.scale(pg.image.load(self.color), (self.size, self.size))
        self.rect = self.sprite_image.get_rect(center=self.center)
