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
        self.init = False
        self.rects = []

    def update(self):
        self.spawn()
        for snake in self.snakes:
            snake.update()

    def spawn(self):
        if self.count >= 20:
            if len(self.snakes[-1].balls) > 0 and self.snakes[-1].balls[-1].index_way < 20:
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
            DELS.append(ball)
            if len(colliders) == 1 and colliders[0] == 0:
                snake.kek(ball.color)
                break
            snake.insert(colliders[0], ball.color)
            break

    def draw_road(self):
        if not self.init:
            start = Vector2(self.start)
            coord = [start.x - 20, start.y - 20, 0, 0]
            vect = self.vectors[0]
            count = 0
            index = 0
            next_vect = self.vectors[index]
            while index < len(self.vectors):
                new_start = Vector2(start)
                while vect == next_vect and index < len(self.vectors):
                    new_start += next_vect
                    next_vect = self.vectors[index]
                    count += 1
                    index += 1
                count += 20
                coord[2] = max(abs(count * vect.x), 40)
                coord[3] = max(abs(count * vect.y), 40)
                if new_start.x < start.x or new_start.y < start.y:
                    coord[0] = new_start.x - 20
                    coord[1] = new_start.y - 20
                self.rects.append(coord)
                start = Vector2(new_start)
                coord = list(coord)
                coord[0] = start.x - 20
                coord[1] = start.y - 20
                vect = next_vect
                count = 0
            self.init = True
        brown = (202, 153, 51)
        for rect in self.rects:
            pg.draw.rect(screen, brown, rect)






