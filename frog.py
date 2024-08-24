from constants import *
from ball import Ball
from pygame import Vector2
import math


class Frog:
    def __init__(self):
        self.sprite_image = pg.transform.scale(pg.image.load("zuma.png"), (150, 150))
        self.center = Vector2(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.rect = self.sprite_image.get_rect(center=self.center)
        self.coord = Vector2(0, 1)
        self.direction = Vector2(0, 1)
        self.mouth = None
        self.spine = None

    def update(self):
        x, y = pg.mouse.get_pos()
        self.direction = Vector2(x, y) - self.center
        cos = ((self.coord.x * self.direction.x + self.coord.y * self.direction.y)
               / (self.coord.length() * self.direction.length()))
        temp = -1 if x < self.center.x else 1
        rotated_sprite = pg.transform.rotate(self.sprite_image, (math.acos(cos) * 180) / math.pi * temp)
        sprite_rect = rotated_sprite.get_rect(center=self.rect.center)
        screen.blit(rotated_sprite, sprite_rect)
        self.mouth = Ball(Vector2(self.center + self.direction.normalize() * 35))
        self.spine = Ball(Vector2(self.center - self.direction.normalize() * 30))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.shoot()
                elif event.button == 3:
                    self.swap()

    def shoot(self):
        self.mouth.update_direction(self.direction.normalize() * 20)
        UNITS.append(self.mouth)
        self.mouth = self.spine
        self.spine = Ball(Vector2(self.center - self.direction.normalize() * 30))

    def swap(self):
        self.spine, self.mouth = self.mouth, self.spine

