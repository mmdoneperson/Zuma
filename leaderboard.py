import pygame as pg
import json
import constants


class Leaderboard:
    def __init__(self):
        self.font_for_level_number = pg.font.SysFont(None, 70)
        self.font_for_player_name = pg.font.SysFont(None, 50)
        self.font_for_text = pg.font.SysFont(None, 30)
        self.shift = pg.Vector2(0, 30)
        self.sprite_image = pg.transform.scale(pg.image.load("image/board.png"),
                                               (900, 700))
        self.id = None
        self.color_text = (255, 255, 255)
        self.input_box = pg.Rect(constants.WINDOW_WIDTH // 2 - 100, 350, 400, 50)
        self.color_inactive = pg.Color('lightskyblue3')
        self.color_active = pg.Color('dodgerblue2')
        self.is_input_box_active = False
        self.player_name = ""
        self.max_length_player_name = 19
        self.coordinate_leaderboard =pg.Vector2(constants.WINDOW_WIDTH // 2 - 500, 200)
        self.json_data = None
        self.leaderboard = None

        # self.text_level1 = self.font_for_level_number.render("Level 1:", True, (255, 255, 255))
        # self.rect_text_level1 = self.text_level1.get_rect(center=pg.Vector2(150, 100))
        #
        # self.text_level2 = self.font_for_level_number.render("Level 2:", True, (255, 255, 255))
        # self.rect_text_level2 = self.text_level2.get_rect(center=pg.Vector2(350, 100))
        #
        # self.text_level3 = self.font_for_level_number.render("Level 3:", True,(255, 255, 255))
        # self.rect_text_level3 = self.text_level3.get_rect(center=pg.Vector2(550, 100))

    def reversed_active(self):
        constants.MENU_BUTTONS["level1"].is_active = \
            not constants.MENU_BUTTONS["level1"].is_active
        constants.MENU_BUTTONS["level2"].is_active = \
            not constants.MENU_BUTTONS["level2"].is_active
        constants.MENU_BUTTONS["level3"].is_active = \
            not constants.MENU_BUTTONS["level3"].is_active
        constants.MENU_BUTTONS["exit game"].is_active = \
            not constants.MENU_BUTTONS["exit game"].is_active
        constants.LEADERBOARD_BUTTONS["close leaderboard"].is_active = \
            not constants.LEADERBOARD_BUTTONS["close leaderboard"].is_active
        constants.LEADERBOARD_BUTTONS["start level"].is_active = \
            not constants.LEADERBOARD_BUTTONS["start level"].is_active

    def close(self):
        self.player_name = ""
        self.reversed_active()

    def print_leaderboard(self):
        start_point_print = pg.Vector2(610, 350)
        for player in self.leaderboard:
            text = self.font_for_text.render(
                player + "  " + str(self.leaderboard[player]), True,
                self.color_text)
            constants.screen.blit(text, start_point_print)
            start_point_print += self.shift

    def check_input_box(self, pos):
        if self.input_box.collidepoint(pos):
            self.is_input_box_active = not self.is_input_box_active
        else:
            self.is_input_box_active = False
        return self.color_active if self.is_input_box_active else self.color_inactive

    def draw_input_box(self, color):
        # Рендер текста
        txt_surface = self.font_for_player_name.render(self.player_name, True,
                                                       self.color_text)
        # Отображаем текст
        constants.screen.blit(txt_surface,
                              (self.input_box.x + 5, self.input_box.y + 5))
        # Отрисовка поля ввода
        pg.draw.rect(constants.screen, color, self.input_box, 2)
        # Обновляем экран
        pg.display.flip()

    def remember_score(self):
        self.leaderboard[self.player_name] = constants.SCORE.score
        with open("players.json", "w") as json_file:
            json.dump(self.json_data, json_file, indent=2)


    def draw_leaderboard(self):
        constants.screen.blit(self.sprite_image, self.coordinate_leaderboard)
        text_level = self.font_for_level_number.render(
            constants.GAME.name_level + " :", True, self.color_text)
        constants.screen.blit(text_level, pg.Vector2(560, 300))
        constants.screen.blit(
            self.font_for_text.render(
                "введите имя",
                True, self.color_text),
            pg.Vector2(constants.WINDOW_WIDTH // 2 - 100, 330))
        with open("players.json", "r") as json_file:
            self.json_data = json.load(json_file)
        self.leaderboard = self.json_data["levels"][constants.GAME.name_level]
        self.print_leaderboard()

    def update_input_box(self, event):
        # Обработка клавиатуры
        if event.type == pg.KEYDOWN:
            if self.is_input_box_active:
                if event.key == pg.K_BACKSPACE:
                    self.draw_leaderboard()
                    self.player_name = self.player_name[:-1]
                else:
                    if self.max_length_player_name >= len(self.player_name):
                        self.player_name += event.unicode

    def start_leaderboard(self):
        self.reversed_active()
        self.draw_leaderboard()
        color = self.color_inactive

        is_active_leaderboard = True
        while is_active_leaderboard:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for button_name in constants.LEADERBOARD_BUTTONS:
                            button = constants.LEADERBOARD_BUTTONS[button_name]
                            if not button.check_click(pg.mouse.get_pos()):
                                continue
                            if button_name == "start level":
                                if len(self.player_name) > 0:
                                    is_active_leaderboard = False
                                    button.command()
                            else:
                                is_active_leaderboard = False
                                button.command()
                    color = self.check_input_box(event.pos)
                self.update_input_box(event)
                self.draw_input_box(color)
            pg.display.flip()
