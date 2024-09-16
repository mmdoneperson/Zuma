import unittest
import constants
import random
import time
import pygame as pg
from ball import Ball
from counter import Counter
from snake import Snake
from way import Way
from pygame import Vector2
from status import Status
from score import Score
from bonus import Bonus
from frog import Frog
from activator_bonuses import Activator
from generator_bonuses import Generator

vectors = [Vector2(random.randint(1, 15),
                   random.randint(1, 15)).normalize() * 2 for i in range(3000)]


class TestZuma(unittest.TestCase):
    def __recovery_screen(self):
        pg.init()
        screen_info = pg.display.Info()
        WINDOW_WIDTH = screen_info.current_w
        WINDOW_HEIGHT = screen_info.current_h
        constants.screen = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

    def __create_snake(self):
        snake = Snake(vectors, 0)
        for i in range(5):
            ball = Ball(Vector2(0, 0))
            snake.balls.append(ball)
            ball.index_way = 0
            ball.update_direction(vectors[ball.index_way])
        return snake

    def test_counter(self):
        counter = Counter()
        numbers = []
        test_success = False
        for i in range(random.randint(100, 1000)):
            numbers.append(counter.get())
        for i in range(len(numbers) - 1):
            if numbers[i + 1] - numbers[i] != 1:
                break
        else:
            test_success = True
        self.assertEquals(test_success, True)

    def test_ball_update(self):
        ball = Ball(Vector2(0, 0))
        ball.update_direction(Vector2(10, 10))
        randint = random.randint(10, 100)
        for i in range(randint):
            ball.update()
        self.assertEquals(ball.center, Vector2(10, 10) * randint)

    def test_ball_draw(self):
        ball = Ball(Vector2(0, 0))
        ball.draw(Vector2(10, 10))
        self.assertEquals(ball.center, Vector2(10, 10))

    def test_ball_change_color(self):
        ball = Ball(Vector2(0, 0))
        self.assertIsNotNone(ball.color)
        color = ball.color
        for c in constants.COLORS:
            if c != color:
                ball.change_color(c)
                self.assertEquals(ball.color, c)
                color = c

    def test_snake_update_forward(self):
        snake = self.__create_snake()
        randint = random.randint(100, 500)
        for i in range(randint):
            snake.update()
        res = Vector2(0, 0)
        for i in range(randint):
            res += vectors[i]
        for ball in snake.balls:
            self.assertEqual(ball.center, res)

    def test_snake_update_back(self):
        constants.WAY = Way(vectors, Vector2(0, 0))
        snake = self.__create_snake()
        randint = random.randint(100, 290)
        index_in_vectors = random.randint(900, 950)
        for ball in snake.balls:
            ball.index_way = index_in_vectors
            ball.update_direction(vectors[index_in_vectors])
        snake.status = Status.Back
        for i in range(randint):
            snake.update()
        res = Vector2(0, 0)
        for i in range(randint):
            res += vectors[index_in_vectors - 1 - i] * -1
        for ball in snake.balls:
            self.assertEqual(ball.center, res)

    def test_snake_update_stop(self):
        snake = self.__create_snake()
        snake.status = Status.Stop
        for ball in snake.balls:
            ball.update_direction(Vector2(1000, 1000))
        randint = random.randint(100, 290)
        for i in range(randint):
            snake.update()
        for ball in snake.balls:
            self.assertEqual(ball.center, Vector2(0, 0))

    def test_snake_insert_ball_into_beginning(self):
        snake = self.__create_snake()
        rand_color = constants.COLORS[random.randint(0, 4)]
        length = len(snake.balls)
        snake.insert_ball_into_beginning(rand_color)
        self.assertEqual(len(snake.balls), length + 1)
        self.assertEqual(snake.balls[0].color, rand_color)

    def test_snake_insert_ball_middle(self):
        snake = self.__create_snake()
        for i in range(5):
            snake.balls[i].change_color(constants.COLORS[i])
        rand_color = constants.COLORS[random.randint(0, 4)]
        length = len(snake.balls)
        index = random.randint(0, len(snake.balls) - 1)
        snake.insert_ball_into_middle(index, rand_color)
        self.assertEqual(len(snake.balls), length + 1)
        self.assertEqual(snake.balls[index + 1].color, rand_color)

    def test_snake_remove_balls(self):
        constants.SCORE = Score(300)
        constants.ACTIVATOR = Activator()
        snake = self.__create_snake()
        rand_color = constants.COLORS[random.randint(0, 4)]
        for i in range(5):
            snake.balls[i].change_color(rand_color)
        snake.insert_ball_into_beginning(rand_color)
        self.assertEqual(len(snake.balls), 0)

    def test_generator_bonuses(self):
        constants.screen = FakeScreen()
        snake = self.__create_snake()
        constants.WAY = Way(vectors, Vector2(0, 0))
        constants.WAY.snakes[0] = snake
        generator = Generator()
        constants.GENERATOR = generator
        generator.sound = FakeMusic()
        pg.quit()
        timer = time.time()
        while time.time() - timer <= 10:
            pass
        for i in range(200):
            snake.update()
            generator.update()
        bonus = None
        for ball in snake.balls:
            if ball.bonus != None:
                bonus = ball.bonus
        self.__recovery_screen()
        self.assertIsNotNone(bonus)

    def test_bonus(self):
        constants.screen = FakeScreen()
        bonus = Bonus()
        center = Vector2(0, 0)
        randint = random.randint(1, 100)
        for i in range(randint):
            bonus.update(center)
            center += Vector2(1, 0)
        self.assertEqual(len(constants.screen.set), randint)
        self.__recovery_screen()

    def test_frog_swap(self):
        frog = Frog()
        color_spine = constants.COLORS[0]
        color_mouth = constants.COLORS[random.randint(1, 4)]
        frog.mouth.change_color(color_mouth)
        frog.spine.change_color(color_spine)
        frog.swap()
        self.assertEqual(frog.spine.color, color_mouth)
        self.assertEqual(frog.mouth.color, color_spine)

    def test_frog_fast_shoot(self):
        frog = Frog()
        randint = random.randint(800, 10 ** 4)
        for i in range(randint):
            frog.speed_up_shoot()
        self.assertEqual(frog.fast_shoot, randint * 5)

    def test_score(self):
        max_score = random.randint(1000, 100000)
        score = Score(max_score)
        _sum = 0
        for i in range(100):
            randint = random.randint(5, 9)
            _sum += randint
            score.add(randint)
            self.assertEqual(score.score, _sum)
            self.assertEqual(score.total_score, _sum)

    def test_way_count_colors_in_balls(self):
        way = Way(vectors, Vector2(0, 0))
        balls = []
        COUNTER_COLORS = dict()
        for color in constants.COLORS:
            COUNTER_COLORS[color] = 0
        randint = random.randint(10, 500)
        for i in range(randint):
            ball = Ball(Vector2(0, 0))
            balls.append(ball)
            COUNTER_COLORS[ball.color] += 1
        way.snakes[0].balls = balls
        way._Way__count_colors_in_balls()
        for color in constants.COLORS:
            self.assertEqual(constants.COUNTER_COLORS[color], COUNTER_COLORS[color])

    def test_way_spawn(self):
        constants.WAY = Way(vectors, Vector2(0, 0))
        length = len(constants.WAY.snakes[0].balls)
        for i in range(random.randint(30, 50)):
            constants.WAY.update()
        self.assertLess(length, len(constants.WAY.snakes[0].balls))

    def test_way_check_collision(self):
        way = Way(vectors, Vector2(0, 0))
        snake = self.__create_snake()
        for i in range(5):
            snake.balls[i].change_color(constants.COLORS[i])
        way.snakes[0] = snake
        ball = Ball(Vector2(0, 0))
        way.check_collision(ball)
        self.assertLess(5, len(way.snakes[0].balls))
        length = len(way.snakes[0].balls)
        ball = Ball(Vector2(520, 520))
        way.check_collision(ball)
        self.assertEqual(length, len(way.snakes[0].balls))

    def test_way_update(self):
        randint = random.randint(10, 100)
        way = Way(vectors, Vector2(0, 0))
        snakes = []
        center = Vector2(0, 0)
        centers = []
        for i in range(randint):
            snake = self.__create_snake()
            for ball in snake.balls:
                ball.center = center
            centers.append(center)
            center += Vector2(100, 100)
            snakes.append(snake)
        way.snakes = snakes
        for i in range(random.randint(100, 400)):
            way.update()
        for i, snake in enumerate(way.snakes):
            self.assertNotEqual(centers[i], snake.balls[0])

    def test_way_reverse(self):
        randint = random.randint(10, 100)
        way = Way(vectors, Vector2(0, 0))
        constants.WAY = way
        center = Vector2(0, 0)
        snakes = []
        for i in range(randint):
            snake = self.__create_snake()
            center += Vector2(100, 100)
            for ball in snake.balls:
                ball.center = center
                ball.index_way = 900
            snakes.append(snake)
        way.snakes = snakes
        for i in range(len(way.snakes)):
            way.snakes[i].id = i
        way.reverse()
        self.assertLess(0, way.reverse_count)
        for i in range(50):
            way.update()
        for snake in way.snakes:
            self.assertLessEqual(snake.balls[0].center.x, 0)
            self.assertLessEqual(snake.balls[0].center.y, 0)

    def test_way_stop(self):
        randint = random.randint(10, 100)
        way = Way(vectors, Vector2(0, 0))
        constants.WAY = way
        center = Vector2(0, 0)
        centers = []
        snakes = []
        count = 0
        for i in range(randint):
            snake = self.__create_snake()
            center += Vector2(100, 100)
            centers.append(center)
            for ball in snake.balls:
                ball.center = center
                ball.index_way = count
                count += 21
            snakes.append(snake)
        way.snakes = snakes
        for i in range(len(way.snakes)):
            way.snakes[i].id = i
        way.stop()
        self.assertLess(0, way.stop_count)
        for i in range(30):
            way.update()
        for i, snake in enumerate(way.snakes):
            self.assertEqual(snake.balls[0].center.x, centers[i].x)
            self.assertEqual(snake.balls[0].center.y, centers[i].y)


class FakeScreen:
    def __init__(self):
        self.set = set()

    def blit(self, a, b):
        a = str(a)
        b = str(b)
        pair = a, b
        self.set.add(pair)


class FakeMusic:
    def play(self):
        pass
