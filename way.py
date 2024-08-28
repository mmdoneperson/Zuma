from ball import Ball
from pygame import Vector2
from constants import *

class Way:
    def __init__(self):
        self.begin_point = Vector2(100, 100)
        self.vectors = []
        self.count = 0
        self.balls = []
        for i in range(400):
            self.vectors.append(Vector2(2, 0))
        for i in range(700):
            self.vectors.append(Vector2(0, 2))

    def update(self):
        if self.count == 20:
            self.count = 0
            ball = Ball(Vector2(self.begin_point), 40)
            ball.index_way = 0
            ball.update_direction(self.vectors[ball.index_way])
            self.balls.append(ball)

        for ball in self.balls:
            if ball.index_way + 1 == len(self.vectors):
                continue
            ball.update()
            ball.index_way += 1
            ball.update_direction(self.vectors[ball.index_way])

        self.count += 1

    def check_collision(self, ball):
        colliders = []
        for i in range(len(self.balls)):
            if ball.rect.colliderect(self.balls[i].rect):
                colliders.append(i)
        if len(colliders) == 0:
            return
        ball.is_shoot = False
        DELS.append(ball)
        if len(colliders) == 1 and colliders[0] == 0:
            self.kek(ball.color)
            return
        self.insert(colliders[0], ball.color)

    def kek(self, color):
        sum_vectors = Vector2(0, 0)
        for i in range(self.balls[0].index_way, min(1000, self.balls[0].index_way + 20)):
            sum_vectors += self.vectors[i]

        new_ball = Ball(self.balls[0].center + sum_vectors)
        new_ball.index_way = self.balls[0].index_way + 20
        new_ball.update_direction(self.vectors[new_ball.index_way])
        new_ball.change_color(color)
        self.balls.insert(0, new_ball)


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
