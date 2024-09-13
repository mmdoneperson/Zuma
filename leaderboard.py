import pygame as pg
import json
import constants


class Leaderboard:
    def __init__(self):
        self.font120 = pg.font.SysFont(None, 120)
        self.font50 = pg.font.SysFont(None, 50)
        self.font30 = pg.font.SysFont(None, 30)
        self.shift = pg.Vector2(0, 30)
        self.sprite_image = pg.transform.scale(
            pg.image.load("image/new_board.png"),
            (900, 700))
        self.id = None
        self.color_text = (255, 255, 255)
        self.input_box = pg.Rect(870, 425, 425, 50)
        self.color_inactive = pg.Color('lightskyblue3')
        self.color_active = pg.Color('dodgerblue2')
        self.is_input_box_active = False
        self.player_name = ""
        self.max_length_player_name = 12
        self.coordinate_leaderboard = pg.Vector2(
            constants.WINDOW_WIDTH // 2 - 500, 200)
        self.json_data = None
        self.leaderboard = None

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

    def sort_leaderboard(self):
        sorted_leaderboard = []
        for player in self.leaderboard:
            sorted_leaderboard.append((self.leaderboard[player], player))
        sorted_leaderboard.sort(reverse=True)
        return sorted_leaderboard[:min(len(sorted_leaderboard), 10)]

    def print_last_player(self):
        last_player_data = self.json_data["last_player"][
            constants.GAME.level.name]
        last_player = self.font50.render(
            "LAST PLAYER: " + last_player_data[0] + " " + str(
                last_player_data[1]),
            True,
            self.color_text)
        constants.screen.blit(last_player, pg.Vector2(520, 770))

    def print_leaderboard(self):
        start_point_print = pg.Vector2(530, 400)
        sort_leaderboard = self.sort_leaderboard()
        self.print_last_player()
        for player in sort_leaderboard:
            text = self.font30.render(
                player[1] + "  " + str(player[0]),
                True,
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
        txt_surface = self.font50.render(self.player_name, True,
                                         self.color_text)
        # Отображаем текст
        constants.screen.blit(txt_surface,
                              (self.input_box.x + 5, self.input_box.y + 5))
        # Отрисовка поля ввода
        pg.draw.rect(constants.screen, color, self.input_box, 2)
        # Обновляем экран
        pg.display.flip()

    def remember_score(self):
        self.leaderboard[self.player_name] = constants.SCORE.total_score
        self.json_data["last_player"][constants.GAME.level.name] = \
            [self.player_name, constants.SCORE.total_score]
        with open("players.json", "w") as json_file:
            json.dump(self.json_data, json_file, indent=2)
        self.close()

    def draw_leaderboard(self):
        constants.screen.blit(self.sprite_image, self.coordinate_leaderboard)
        text_level = self.font120.render(
            constants.GAME.level.name, True, self.color_text)
        constants.screen.blit(text_level, pg.Vector2(800, 250))
        text_leaderboard = self.font50.render("LEADERBOARD:", True,
                                              self.color_text)
        constants.screen.blit(text_leaderboard, pg.Vector2(500, 350))
        constants.screen.blit(
            self.font30.render(
                "введите имя",
                True, self.color_text),
            pg.Vector2(870, 400))
        with open("players.json", "r") as json_file:
            self.json_data = json.load(json_file)
        self.leaderboard = self.json_data["levels"][constants.GAME.level.name]
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
