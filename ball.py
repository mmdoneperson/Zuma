from constants import *
import random


class Ball:
    def __init__(self, center):
        self.direction = Vector2(0, 0)
        self.radius = radius_ball
        self.color = COLORS[random.randint(0, 4)]
        self.center = center
        self.sprite_image = pg.transform.scale(pg.image.load("zuma.png"),(40, 40))
        self.rect = self.sprite_image.get_rect(center=self.center)
        screen.blit(self.sprite_image, self.rect)

    def update_direction(self, direction):
        self.direction = direction

    def update(self):
        self.center += self.direction
        self.rect = self.sprite_image.get_rect(center=self.center)
        screen.blit(self.sprite_image, self.rect)
