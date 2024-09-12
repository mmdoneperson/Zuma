import random
import time
import constants
from bonus import Bonus
class Generator:
    def __init__(self):
        self.timer = time.time()

    def update(self):
        if time.time() - self.timer >= 10:
            self.__set()
            self.timer = time.time()

    def __set(self):
        snakes = []
        for snake in constants.WAY.snakes:
            if len(snake.balls) != 0:
                snakes.append(snake)
        rand = random.randint(0, len(snakes) - 1)
        snake = snakes[rand]
        rand = random.randint(0, len(snake.balls) - 1)
        snake.balls[rand].bonus = Bonus()
