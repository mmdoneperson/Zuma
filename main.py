from constants import *
from frog import Frog
from way import Way
import sys


class Game:
    def __init__(self):
        self.active_menu = True
        self.game_finished = False
        self.menu_background = pg.transform.scale(
            pg.image.load("menu.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.rect_menu_background = self.menu_background.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.level = None
        self.vectors = None

    def start_game(self):
        screen.blit(self.menu_background, self.rect_menu_background)
        while self.active_menu:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    for button in BUTTONS:
                        if not button.check_click(pg.mouse.get_pos()):
                            continue
                        self.level = button.command()
                        if self.level is None:
                            self.active_menu = False
                            self.game_finished = True
                        else:
                            self.vectors = self.level.vectors
                            UNITS['way'] = Way(self.vectors,
                                               self.level.starting_point_of_way)
                            UNITS['frog'] = Frog()
                            UNITS['frog'].center = self.level.frog_point
                            UNITS['frog'].rect.center = self.level.frog_point
                            self.active_menu = False
            pg.display.flip()
        if self.game_finished:
            pg.quit()
            sys.exit()
        self.update_all()

    def update_all(self):
        while True:
            pg.time.Clock().tick(60)
            screen.fill([255, 255, 255])

            UNITS['way'].draw_road()
            UNITS['frog'].update()
            for key in UNITS:
                if key == 'frog' or key == 'way':
                    continue
                UNITS[key].update()
            UNITS['way'].update()
            for obj in DELS:
                UNITS.pop(obj.hash)
            DELS.clear()
            pg.display.flip()


if __name__ == "__main__":
    Game().start_game()
