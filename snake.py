from ball import Ball
from pygame import Vector2
from constants import *


class Snake:
    def __init__(self, vectors, id):
        self.vectors = vectors
        self.balls = []
        self.id = id


    def update(self):
        for ball in self.balls:
            if ball.index_way + 1 == len(self.vectors):
                continue
            ball.update()
            ball.index_way += 1
            ball.update_direction(self.vectors[ball.index_way])

    def kek(self, color):
        sum_vectors = Vector2(0, 0)
        for i in range(self.balls[0].index_way, min(1000, self.balls[0].index_way + 20)):
            sum_vectors += self.vectors[i]

        new_ball = Ball(self.balls[0].center + sum_vectors)
        new_ball.index_way = self.balls[0].index_way + 20
        new_ball.update_direction(self.vectors[new_ball.index_way])
        new_ball.change_color(color)
        self.balls.insert(0, new_ball)
        self.remove_balls(0)

    def insert(self, index, color):
        sum_vectors = Vector2(0, 0)
        for i in range(self.balls[0].index_way, min(1000, self.balls[0].index_way + 20)):
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
        # if indexes[0] == len(self.balls) - 1:
        if indexes[-1] == 0:
            self.balls = self.balls[indexes[0] + 1:]
            return
        left_ball = self.balls[indexes[0] + 1:]
        right_ball = self.balls[0: indexes[-1]]
        self.balls = left_ball
        right_snake = Snake(self.vectors,0)
        right_snake.balls = right_ball
        UNITS['way'].snakes.insert(self.id + 1, right_snake)
        for i in range(len(UNITS['way'].snakes)):
            UNITS['way'].snakes[i].id = i