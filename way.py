import constants
from snake import Snake
from pygame import Vector2
from ball import Ball
import pygame as pg
from status import Status


class Way:
    def __init__(self, vectors, start):
        self.count = 0
        self.snakes = [Snake(vectors, 0)]
        self.vectors = vectors
        self.start = start
        self.init = False
        self.is_end = False
        self.is_spawn = True
        self.reverse_count = 0
        self.stop_count = 0
        self.rects = []
        self.statuses = []

    def update(self):
        if len(self.snakes) == 1 and not self.is_spawn:
            if self.reverse_count + self.stop_count == 0:
                if self.snakes[0].status != Status.Forward:
                    self.snakes[0].status = Status.Forward
        if self.is_end:
            self.end_level()
            return
        if self.reverse_count > 0:
            self.__reverse()
        if self.stop_count > 0:
            self.__stop()
        else:
            self.spawn()
            for snake in self.snakes:
                snake.update()
        self.__count_colors_in_balls()

    def __count_colors_in_balls(self):
        constants.COUNTER_COLORS = dict()
        for color in constants.COLORS:
            constants.COUNTER_COLORS[color] = 0
        for snake in self.snakes:
            for ball in snake.balls:
                constants.COUNTER_COLORS[ball.color] += 1

    def __stop(self):
        for snake in self.snakes:
            snake.status = Status.Stop
            snake.update()
        self.stop_count -= 1
        if self.stop_count == 0:
            self.__recover_way()

    def __reverse(self):
        for snake in self.snakes:
            snake.status = Status.Back
            snake.update()
        self.reverse_count -= 1
        if self.reverse_count == 0:
            self.__recover_way()

    def __recover_way(self):
        forward_init = False
        for i in range(min(len(self.snakes), len(self.statuses))):
            self.snakes[i].status = self.statuses[i]
            if self.snakes[i].status == Status.Forward:
                forward_init = True
        if len(self.statuses) < len(self.snakes) and i == len(self.statuses) - 1:
            for x in range(i + 1):
                if self.snakes[x].status == Status.Forward:
                    self.snakes[x].status = Status.Stop
            for q in range(i + 1, len(self.snakes)):
                self.snakes[q].status = Status.Stop
            self.snakes[-1].status = Status.Forward
        if not forward_init:
            if len(self.snakes) == 0:
                self.snakes.append(Snake(self.vectors, 0))
            if len(self.snakes) == 1:
                self.snakes[0].status = Status.Stop
                self.snakes.append(Snake(self.vectors, 1))
            self.snakes[-1].status = Status.Forward
        if len(self.snakes[-1].balls) > 0 and self.snakes[-1].balls[
            -1].index_way > 20 and constants.WAY.is_spawn:
            self.snakes[-1].status = Status.Stop
            self.snakes.append(Snake(self.vectors, len(self.snakes)))

    def spawn(self):
        if self.count >= 20 and self.is_spawn:
            if len(self.snakes) == 0:
                self.snakes.append(Snake(self.vectors, 0))
            if (len(self.snakes[-1].balls) > 0
                    and self.snakes[-1].balls[-1].index_way < 20):
                return
            if len(self.snakes[-1].balls) > 0 and self.snakes[-1].balls[-1].index_way > 20:
                self.snakes[-1].status = Status.Stop
                self.snakes.append(Snake(self.vectors, len(self.snakes)))
            self.count = 0
            ball = Ball(Vector2(self.start), 40)
            ball.index_way = 0
            self.snakes[-1].balls.append(ball)
        self.count += 1

    def check_collision(self, ball):
        for snake in self.snakes:
            colliders = []
            for i in range(len(snake.balls)):
                if ball.rect.colliderect(snake.balls[i].rect):
                    colliders.append(i)
            if len(colliders) == 0:
                continue
            ball.is_shoot = False
            constants.REMOVED_BALLS.append(ball)
            if len(colliders) == 1 and colliders[0] == 0:
                snake.insert_ball_into_beginning(ball.color)
                break
            snake.insert_ball_into_middle(colliders[0], ball.color)
            break

    def end_level(self):
        if (self.snakes[0].balls[0].index_way
                == self.snakes[-1].balls[-1].index_way):
            constants.LEADERBOARD.remember_score()
            constants.GAME.start_game()
        self.is_end = True
        constants.FROG.is_end = True
        for snake in self.snakes:
            snake.status = Status.Forward
            for i in range(30):
                snake.update()

    def reverse(self, statuses=None):
        self.reverse_count = 75
        self.statuses = []
        if statuses is not None:
            self.statuses = statuses
        else:
            for snake in self.snakes:
                self.statuses.append(snake.status)
                snake.status = Status.Back

    def stop(self, statuses=None):
        self.stop_count = 75
        self.statuses = []
        if statuses is not None:
            self.statuses = statuses
        else:
            for snake in self.snakes:
                self.statuses.append(snake.status)
                snake.status = Status.Stop
