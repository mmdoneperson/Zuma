import constants
import pygame as pg


class Score:
    def __init__(self, max_score):
        self.score = 0
        self.total_score = 0
        self.max_score = max_score
        self.is_full = False

    def add(self, point):
        self.score += point
        self.total_score += point
        if self.score >= self.max_score:
            self.score = self.max_score
            if not self.is_full:
                constants.WAY.is_spawn = False
                if constants.WAY.stop_count > 0:
                    constants.WAY.stop_count = 0
                    constants.WAY.reverse(constants.WAY.statuses)
                else:
                    constants.WAY.reverse()
            self.is_full = True

    def update(self):
        black = (0, 0, 0)
        green = (0, 255, 0)
        black_rect = [20, 20, 150, 40]
        length_green = self.score * 120 / self.max_score
        green_rect = [35, 25, length_green, 30]
        pg.draw.rect(constants.screen, black, black_rect)
        pg.draw.rect(constants.screen, green, green_rect)
        if self.is_full:
            count = 0
            for snake in constants.WAY.snakes:
                count += len(snake.balls)
            if count == 0:
                constants.REMOVED_BALLS.clear()
                constants.EXPOSED_BALLS.clear()
                constants.LEADERBOARD.remember_score()
                constants.GAME.start_game()