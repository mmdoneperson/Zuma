from ball import Ball
from pygame import Vector2
from constants import *

class Way:
    def __init__(self):
        self.begin_point = Vector2(100, 100)
        self.vectors = []
        self.count = 0
        self.balls = []
        for i in range(1000):
            self.vectors.append(Vector2(2, 0))

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
        for b in self.balls:
            colliders.append(b.rect)
        index = ball.rect.collidelist(colliders)
        if index == -1:
            return
        ball.is_shoot = False
        print(index)
        self.insert(index, ball)

    def insert(self, index, ball):
        sum_vectors = Vector2(0, 0)
        for i in range(self.balls[0].index_way, min(1000, self.balls[0].index_way + 20)):
            sum_vectors += self.vectors[i]
        new_ball = Ball(self.balls[0].center + sum_vectors)
        new_ball.index_way = self.balls[1].index_way + 20
        new_ball.update_direction(self.vectors[new_ball.index_way])
        self.balls.insert(index, new_ball)



