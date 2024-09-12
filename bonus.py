import constants
import random


class Bonus:
    def __init__(self):
        self.bonus = constants.BONUSES[random.randint(0, len(constants.BONUSES) - 1)]
        self.sprite_image = constants.SPRITES[fr"image\{self.bonus}.png"]

    def update(self, center):
        rect = self.sprite_image.get_rect(center=center)
        constants.screen.blit(self.sprite_image, rect)