import pygame as pg
import constants


class Leaderboard:
    def __init__(self):
        self.font_for_level_number = pg.font.SysFont(None, 50)
        self.shift = 5
        self.sprite_image = pg.transform.scale(pg.image.load("image/board.png"),(800, 600))
        self.rect = self.sprite_image.get_rect(center=pg.Vector2(400, 300))
        self.is_show = False
        self.id = None

        self.text_level1 = self.font_for_level_number.render("Level 1:", True, (255, 255, 255))
        self.rect_text_level1 = self.text_level1.get_rect(center=pg.Vector2(150, 100))

        self.text_level2 = self.font_for_level_number.render("Level 2:", True, (255, 255, 255))
        self.rect_text_level2 = self.text_level2.get_rect(center=pg.Vector2(350, 100))

        self.text_level3 = self.font_for_level_number.render("Level 3:", True,(255, 255, 255))
        self.rect_text_level3 = self.text_level3.get_rect(center=pg.Vector2(550, 100))


    def click(self):
        if not self.is_show:
            self.id = constants.COUNTER.get()
            self.is_show = True
            constants.BUTTONS_FOR_UPDATE[self.id] = self
        else:
            self.is_show = False
            constants.BUTTONS_FOR_UPDATE.pop(self.id)


    def draw(self):
        constants.screen.blit(self.sprite_image, self.rect)
        constants.screen.blit(self.text_level1, self.rect_text_level1)
        constants.screen.blit(self.text_level2, self.rect_text_level2)
        constants.screen.blit(self.text_level3, self.rect_text_level3)


