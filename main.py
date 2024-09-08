from constants import *
from frog import Frog
from way import Way
from score import Score
from abyss import Abyss
from pygame import Vector2
import sys


class Game:
    def __init__(self):
        self.active_menu = True
        self.game_finished = False
        self.map_background = None
        self.rect_map_background = None
        self.menu_background = pg.transform.scale(
            pg.image.load("menu.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.rect_menu_background = self.menu_background.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.level = None
        self.vectors = None

    def start_game(self):
        UNITS.clear()
        self.active_menu = True
        screen.blit(self.menu_background, self.rect_menu_background)
        while self.active_menu:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    for button in MENU_BUTTONS:
                        if not button.check_click(pg.mouse.get_pos()):
                            continue
                        self.level = button.command()
                        if self.level is None:
                            self.active_menu = False
                            self.game_finished = True
                        else:
                            self.map_background = self.level.map_background
                            self.rect_map_background =\
                                self.map_background.get_rect(
                                    center=(WINDOW_WIDTH // 2,
                                            WINDOW_HEIGHT // 2))
                            self.vectors = self.level.vectors
                            UNITS['way'] = Way(self.vectors,
                                               self.level.starting_point_of_way)
                            UNITS['frog'] = Frog()
                            UNITS['frog'].center = self.level.frog_point
                            UNITS['frog'].rect.center = self.level.frog_point
                            UNITS['score'] = Score(150)
                            start = Vector2(self.level.starting_point_of_way)
                            for vect in self.vectors:
                                start += vect
                            UNITS['abyss'] = Abyss(start.x, start.y, len(self.vectors))
                            self.active_menu = False
            pg.display.flip()
        if self.game_finished:
            pg.quit()
            sys.exit()
        self.update_all()

    def update_all(self):
        while True:
            pg.time.Clock().tick(60)
            screen.blit(self.map_background, (0, 0))
            screen.blit(BUTTON_RETURN_MENU.image, BUTTON_RETURN_MENU.rect)
            UNITS['abyss'].update()
            #UNITS['way'].draw_road()
            UNITS['frog'].update()
            for key in UNITS:
                if key == 'frog' or key == 'way' or key == 'score' or key == 'abyss':
                    continue
                UNITS[key].update()
            UNITS['way'].update()
            UNITS['score'].update()
            for obj in DELS:
                UNITS.pop(obj.hash)
            DELS.clear()
            pg.display.flip()


if __name__ == "__main__":
    GAME.append(Game())
    GAME[0].start_game()
