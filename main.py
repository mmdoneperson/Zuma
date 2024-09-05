from constants import *
from frog import Frog
from way import Way
from pygame import Vector2
import levels


class Game:
    def __init__(self):
        self.level_started = False
        self.menu_background = pg.transform.scale(
            pg.image.load("menu.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.rect_menu_background = self.menu_background.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.level = None
        self.vectors = None

    def start_game(self):
        screen.blit(self.menu_background, self.rect_menu_background)
        while not self.level_started:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    print(pg.mouse.get_pos())
                    for button in BUTTONS:
                        if button.check_click(pg.mouse.get_pos()):
                            self.level = button.command()
                            self.vectors = self.level.vectors
                            UNITS['way'] = Way(self.vectors,
                                               self.level.starting_point_of_way)
                            UNITS['frog'] = Frog()
                            UNITS['frog'].center = self.level.frog_point
                            UNITS['frog'].rect.center = self.level.frog_point
                            self.level_started = True
            pg.display.flip()

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
