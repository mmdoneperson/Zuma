from ball import Ball
from pygame import Vector2
from constants import *


class Snake:
    def __init__(self, vectors, id):
        self.vectors = vectors
        self.balls = []
        self.id = id
        self.status = Status.Forward

    def update(self):
        if self.status == Status.Forward:
            for ball in self.balls:
                if ball.index_way + 1 == len(self.vectors):
                    continue
                ball.update_direction(self.vectors[ball.index_way])
                ball.update()
                ball.index_way += 1
            if self.id == 0:
                return
            if abs(self.balls[0].index_way - UNITS['way'].snakes[self.id - 1].balls[-1].index_way) - 20 < 1e-6:
                snake = UNITS['way'].snakes[self.id - 1]
                snake.status = Status.Forward
                snake.balls = snake.balls + self.balls
                UNITS['way'].snakes.pop(self.id)
                self.recover_indexes()
        if self.status == Status.Stop:
            for ball in self.balls:
                ball.update_direction(Vector2(0, 0))
                ball.update()
        if self.status == Status.Back:
            for i in range(3):
                for ball in self.balls:
                    if ball.index_way - 1 == 0:
                        continue
                    ball.update_direction(-1 * self.vectors[ball.index_way - 1])
                    ball.update()
                    ball.index_way -= 1
                if abs(self.balls[-1].index_way - UNITS['way'].snakes[self.id + 1].balls[0].index_way) - 20 < 1e-6:
                    self.status = Status.Forward
                    index = len(self.balls) - 1
                    self.balls = self.balls + UNITS['way'].snakes[self.id + 1].balls
                    UNITS['way'].snakes.pop(self.id + 1)
                    self.recover_indexes()
                    self.remove_balls(index)
                    break

    def kek(self, color):
        sum_vectors = Vector2(0, 0)
        for i in range(self.balls[0].index_way, self.balls[0].index_way + 20):
            sum_vectors += self.vectors[i]

        new_ball = Ball(self.balls[0].center + sum_vectors)
        new_ball.index_way = self.balls[0].index_way + 20
        new_ball.update_direction(self.vectors[new_ball.index_way])
        new_ball.change_color(color)
        self.balls.insert(0, new_ball)
        self.remove_balls(0)

    def insert(self, index, color):
        sum_vectors = Vector2(0, 0)
        for i in range(self.balls[0].index_way, self.balls[0].index_way + 20):
            sum_vectors += self.vectors[i]
        cur_color = color
        for i in range(index, -1, -1):
            temp = self.balls[i].color
            self.balls[i].change_color(cur_color)
            cur_color = temp
        new_ball = Ball(self.balls[0].center + sum_vectors)
        new_ball.index_way = self.balls[0].index_way + 20
        new_ball.update_direction(self.vectors[new_ball.index_way])
        new_ball.change_color(cur_color)

        self.balls.insert(0, new_ball)
        self.remove_balls(index + 1)

    def remove_balls(self, index):
        color = self.balls[index].color
        indexes = []
        for i in range(index, -1, -1):
            if color == self.balls[i].color:
                indexes.append(i)
            else:
                break
        for i in range(index + 1, len(self.balls)):
            if color == self.balls[i].color:
                indexes.append(i)
            else:
                break
        if len(indexes) <= 2:
            return
        indexes.sort(reverse=True)
        if indexes[0] == len(self.balls) - 1:
            self.balls = self.balls[:indexes[-1]]
            return
        if indexes[-1] == 0:
            self.balls = self.balls[indexes[0] + 1:]
            return
        self.split(indexes)


    def split(self, indexes):
        new_ball = self.balls[indexes[0] + 1:]
        cur_ball = self.balls[0: indexes[-1]]
        self.balls = cur_ball
        new_snake = Snake(self.vectors, 0)
        new_snake.balls = new_ball
        UNITS['way'].snakes.insert(self.id + 1, new_snake)
        self.recover_indexes()
        if new_ball[0].color == cur_ball[-1].color:
            self.status = Status.Back
            new_snake.status = Status.Stop
            return
        if self.status == Status.Stop:
            new_snake.status = Status.Stop
        self.status = Status.Stop

    def recover_indexes(self):
        for i in range(len(UNITS['way'].snakes)):
            UNITS['way'].snakes[i].id = i
