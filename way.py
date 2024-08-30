from constants import *
from snake import Snake
from pygame import Vector2
from ball import Ball


class Way:
    def __init__(self, vectors, start):
        self.count = 0
        self.snakes = [Snake(vectors, 0)]
        self.vectors = vectors
        self.start = start

    def update(self):
        self.spawn()
        for snake in self.snakes:
            snake.update()

    def spawn(self):
        if self.count == 20:
            self.count = 0
            ball = Ball(Vector2(self.start), 40)
            ball.index_way = 0
            ball.update_direction(self.vectors[ball.index_way])
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
            DELS.append(ball)
            if len(colliders) == 1 and colliders[0] == 0:
                snake.kek(ball.color)
                break
            snake.insert(colliders[0], ball.color)
            break
