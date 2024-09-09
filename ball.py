import constants
from pygame import Vector2
import random
import pygame as pg
from status import Status


class Ball:
    def __init__(self, center, size=constants.radius_ball):
        self.size = size
        self.status = Status.Forward
        self.direction = Vector2(0, 0)
        self.color = constants.BALL_COLORS[random.randint(0, 4)]
        self.center = center
        self.index_way = None
        self.is_shoot = False
        self.hash = constants.COUNTER.get()
        self.sprite_image = constants.BALL_SPRITES[self.color]
        self.sprite_image = pg.image.load(self.color).convert_alpha()
        self.sprite_image = pg.transform.scale(self.sprite_image, (size, size))
        self.rect = self.sprite_image.get_rect(center=self.center)
        constants.screen.blit(self.sprite_image, self.rect)

    def update_direction(self, direction):
        self.direction = direction

    def draw(self, center):
        self.center = center
        self.rect.center = self.center
        constants.screen.blit(self.sprite_image, self.rect)

    def update(self):
        self.center += self.direction
        self.rect.center = self.center
        constants.screen.blit(self.sprite_image, self.rect)
        if self.is_shoot:
            constants.WAY.check_collision(self)

    def change_color(self, color, is_on_frog=False):
        self.color = color
        self.sprite_image = constants.BALL_SPRITES[self.color]
        if is_on_frog:
            self.sprite_image = pg.transform.scale(self.sprite_image,
                                                   (self.size, self.size))
        self.rect = self.sprite_image.get_rect(center=self.center)
