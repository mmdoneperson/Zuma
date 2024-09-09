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
        self.rects = []
        self.statuses = []

    def update(self):
        if self.is_end:
            self.end_level()
            return
        if self.reverse_count > 0:
            for snake in self.snakes:
                snake.update()
            self.reverse_count -= 1
            if self.reverse_count == 0:
                for i in range(len(self.snakes)):
                    self.snakes[i].status = self.statuses[i]
        else:
            self.spawn()
            for snake in self.snakes:
                snake.update()

    def spawn(self):
        if self.count >= 20 and self.is_spawn:
            if (len(self.snakes[-1].balls) > 0
                    and self.snakes[-1].balls[-1].index_way < 20):
                return
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
            constants.GAME.start_game()
        self.is_end = True
        constants.FROG.is_end = True
        for snake in self.snakes:
            snake.status = Status.Forward
            for i in range(30):
                snake.update()

    def reverse(self):
        self.statuses = []
        self.reverse_count = 200
        for snake in self.snakes:
            self.statuses.append(snake.status)
            snake.status = Status.Back
