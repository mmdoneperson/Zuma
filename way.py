from ball import Ball
from pygame import Vector2
from constants import *

class Way:
    def __init__(self):
        self.begin_point = Vector2(100, 100)
        self.vectors = []
        self.count = 0
        for i in range(1000):
            self.vectors.append(Vector2(2, 0))

    def update(self):
        if self.count == 20:
            self.count = 0
            ball = Ball(Vector2(self.begin_point), 40)
            ball.index_way = 0
            ball.update_direction(self.vectors[ball.index_way])
            BALLS.append(ball)

        for ball in BALLS:
            if ball.index_way + 1 == len(self.vectors):
                continue
            ball.update()
            ball.index_way += 1
            ball.update_direction(self.vectors[ball.index_way])

        self.count += 1

    def indert(self, index, color):
        pass