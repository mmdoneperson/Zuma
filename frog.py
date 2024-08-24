from constants import *
from pygame import Vector2
import math


class Frog:
    def __init__(self, screen):
        self.screen = screen
        self.sprite_image = pg.transform.scale(pg.image.load("player.png"),(120, 120))
        self.center = Vector2(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.rect = self.sprite_image.get_rect(center=self.center)
        self.coord = Vector2(0, 1)


    def update(self):
        x, y = pg.mouse.get_pos()
        vect = Vector2(x, y) - self.center
        cos = (self.coord.x * vect.x + self.coord.y * vect.y) / (self.coord.length() * vect.length())
        rotated_sprite = pg.transform.rotate(self.sprite_image, (math.acos(cos) * 180) / math.pi)
        sprite_rect = rotated_sprite.get_rect(center=self.rect.center)
        self.screen.blit(rotated_sprite, sprite_rect)
        self.coord = vect
        #pg.draw.rect(self.screen, [0, 255, 0], [225, 225, 25, 25])


        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("Нажата левая кнопка мыши")
                elif event.button == 3:
                    print("Нажата правая кнопка мыши")
            a = pg.mouse.get_pos()
