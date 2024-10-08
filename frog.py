from constants import *
from ball import Ball
from pygame import Vector2
import math
import time


class Frog:
    def __init__(self):
        self.sprite_image = pg.transform.scale(pg.image.load("image/zuma.png"), (150, 150))
        self.center = Vector2(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.rect = self.sprite_image.get_rect(center=self.center)
        self.coord = Vector2(0, 1)
        self.direction = Vector2(0, 1)
        self.mouth = Ball(Vector2(self.center + self.direction.normalize() * 35))
        self.spine = Ball(Vector2(self.center - self.direction.normalize() * 40), radius_ball // 2)
        self.is_end = False
        self.timer_start = time.time()

    def update(self):
        x, y = pg.mouse.get_pos()
        self.direction = Vector2(x, y) - self.center
        if abs(self.direction.length()) >= 1e-6:
            cos = ((self.coord.x * self.direction.x + self.coord.y * self.direction.y)
                   / (self.coord.length() * self.direction.length()))
            temp = -1 if x < self.center.x else 1
            rotated_sprite = pg.transform.rotate(self.sprite_image, (math.acos(cos) * 180) / math.pi * temp)
            sprite_rect = rotated_sprite.get_rect(center=self.rect.center)
            screen.blit(rotated_sprite, sprite_rect)
            self.mouth.draw(self.center + self.direction.normalize() * 35)
            self.spine.draw(self.center - self.direction.normalize() * 40)

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN and not self.is_end:
                if event.button == 1:
                    if BUTTON_RETURN_MENU.rect.collidepoint(pg.mouse.get_pos()):
                        GAME[0].start_game()
                    if time.time() - self.timer_start >= 0.2:
                        self.shoot()
                        self.timer_start = time.time()
                elif event.button == 3:
                    self.swap()

    def shoot(self):
        sound_shot.play()
        self.mouth.update_direction(self.direction.normalize() * 40)
        self.mouth.is_shoot = True
        UNITS[self.mouth.hash] = self.mouth
        self.mouth = Ball(Vector2(self.center + self.direction.normalize() * 35))
        self.mouth.change_color(self.spine.color)
        self.spine = Ball(Vector2(self.center - self.direction.normalize() * 40), radius_ball // 2)

    def swap(self):
        temp = self.mouth.color
        self.mouth.change_color(self.spine.color, True)
        self.spine.change_color(temp, True)
