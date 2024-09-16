import constants
import pygame as pg
from ball import Ball
from pygame import Vector2
import math
import time


class Frog:
    def __init__(self):
        self.sprite_image = pg.transform.scale(pg.image.load("image/zuma.png"),
                                               (150, 150))
        self.center = Vector2(constants.WINDOW_WIDTH // 2,
                              constants.WINDOW_HEIGHT // 2)
        self.rect = self.sprite_image.get_rect(center=self.center)
        self.coord = Vector2(0, 1)
        self.direction = Vector2(0, 1)
        self.mouth = Ball(
            Vector2(self.center + self.direction.normalize() * 35))
        self.spine = Ball(
            Vector2(self.center - self.direction.normalize() * 40),
            constants.radius_ball // 2)
        self.is_end = False
        self.timer_start = time.time()
        self.sound_shot = pg.mixer.Sound(r"sounds\shot.ogg")
        self.fast_shoot = 0

    def update(self):
        x, y = pg.mouse.get_pos()
        self.direction = Vector2(x, y) - self.center
        if abs(self.direction.length()) >= 1e-6:
            self.turn_around_frog(x)
            self.mouth.draw(self.center + self.direction.normalize() * 35)
            self.spine.draw(self.center - self.direction.normalize() * 40)
        self.check_click()

    def calculating_cos_of_angle_of_rotation(self):
        return ((self.coord.x * self.direction.x + self.coord.y * self.direction.y)
                / (self.coord.length() * self.direction.length()))

    def turn_around_frog(self, x):
        cos = self.calculating_cos_of_angle_of_rotation()
        temp = -1 if x < self.center.x else 1
        rotated_sprite = pg.transform.rotate(self.sprite_image, (
                math.acos(cos) * 180) / math.pi * temp)
        sprite_rect = rotated_sprite.get_rect(center=self.rect.center)
        constants.screen.blit(rotated_sprite, sprite_rect)

    def check_click(self):
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN and not self.is_end:
                if event.button == 1:
                    if constants.BUTTON_RETURN_MENU.rect.collidepoint(
                            pg.mouse.get_pos()):
                        constants.BUTTON_RETURN_MENU.command()
                    temp = 1
                    if self.fast_shoot > 0:
                        temp = 2
                    if time.time() - self.timer_start >= 0.2 / temp:
                        self.shoot()
                        self.timer_start = time.time()
                elif event.button == 3:
                    self.swap()

    def shoot(self):
        self.sound_shot.play()
        if self.fast_shoot > 0:
            self.mouth.update_direction(self.direction.normalize() * 80)
            self.fast_shoot -= 1
        else:
            self.mouth.update_direction(self.direction.normalize() * 40)
        self.mouth.is_shoot = True
        self.mouth.bonus = None
        constants.EXPOSED_BALLS[self.mouth.hash] = self.mouth
        self.mouth = Ball(
            Vector2(self.center + self.direction.normalize() * 35))
        self.mouth.change_color(self.spine.color)
        self.spine = Ball(
            Vector2(self.center - self.direction.normalize() * 40),
            constants.radius_ball // 2)

    def swap(self):
        temp = self.mouth.color
        self.mouth.change_color(self.spine.color, True)
        self.spine.change_color(temp, True)

    def speed_up_shoot(self):
        self.fast_shoot += 5
