import constants
import pygame as pg
from frog import Frog
from way import Way
from score import Score
from abyss import Abyss
from pygame import Vector2
import system_functions


class Game:
    def __init__(self):
        self.active_menu = True
        self.game_finished = False
        self.map_background = None
        self.rect_map_background = None
        self.menu_background = pg.transform.scale(
            pg.image.load("image/menu.png"),
            (constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
        self.rect_menu_background = self.menu_background.get_rect(
            center=(constants.WINDOW_WIDTH // 2, constants.WINDOW_HEIGHT // 2))
        self.level = None
        self.vectors = None

    def start_game(self):
        system_functions.start_music("sounds/music_menu.mp3")
        constants.EXPOSED_BALLS.clear()
        self.active_menu = True
        constants.screen.blit(self.menu_background, self.rect_menu_background)
        while self.active_menu:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    for button in constants.MENU_BUTTONS:
                        if not button.check_click(pg.mouse.get_pos()):
                            continue
                        self.level = button.command()
                        if self.level is not None:
                            self.start_level()
                        self.update_menu()
            pg.display.flip()
        system_functions.pause_music()
        self.update_all()

    def update_menu(self):
        constants.screen.blit(self.menu_background, self.rect_menu_background)
        for button in constants.BUTTONS_FOR_UPDATE.values():
            button.draw()



    def update_all(self):
        system_functions.start_music("sounds/music_level.mp3")
        while True:
            pg.time.Clock().tick(60)
            constants.screen.blit(self.map_background, (0, 0))
            constants.screen.blit(constants.BUTTON_RETURN_MENU.image,
                                  constants.BUTTON_RETURN_MENU.rect)
            constants.ABYSS.update()
            constants.FROG.update()
            for key in constants.EXPOSED_BALLS:
                constants.EXPOSED_BALLS[key].update()
            constants.WAY.update()
            constants.SCORE.update()
            for obj in constants.REMOVED_BALLS:
                constants.EXPOSED_BALLS.pop(obj.hash)
            constants.REMOVED_BALLS.clear()
            pg.display.flip()

    def check_end_game(self):
        if self.game_finished:
            system_functions.close_game()

    def start_level(self):
        self.map_background = self.level.map_background
        self.rect_map_background = \
            self.map_background.get_rect(
                center=(constants.WINDOW_WIDTH // 2,
                        constants.WINDOW_HEIGHT // 2))
        self.vectors = self.level.vectors
        constants.WAY = Way(self.vectors,
                                     self.level.starting_point_of_way)
        constants.FROG = Frog()
        constants.FROG.center = self.level.frog_point
        constants.FROG.rect.center = self.level.frog_point
        constants.SCORE = Score(150)
        start = Vector2(self.level.starting_point_of_way)
        for vect in self.vectors:
            start += vect
        constants.ABYSS = Abyss(start.x, start.y,
                                         len(self.vectors))
        self.active_menu = False


if __name__ == "__main__":
    constants.GAME = Game()
    constants.GAME.start_game()
