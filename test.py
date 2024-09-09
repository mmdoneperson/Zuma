from ball import Ball
from pygame import Vector2
import constants
import pygame as pg
from status import Status


def recover_indexes():
    for i in range(len(constants.WAY.snakes)):
        constants.WAY.snakes[i].id = i


class Snake:
    def __init__(self, vectors, id):
        self.vectors = vectors
        self.balls = []
        self.id = id
        self.status = Status.Forward
        self.sound_remove_balls = pg.mixer.Sound(r"sounds\endoflevelpop1.ogg")
        self.sound_insert_ball = pg.mixer.Sound(r"sounds\ballclick2.ogg")

    def update(self):
        if len(self.balls) == 0:
            return
        if self.status == Status.Forward:
            self.__forward()
        if self.status == Status.Stop:
            self.__stop()
        if self.status == Status.Back:
            self.__back()

    def __forward(self):
        for ball in self.balls:
            if ball.index_way + 1 == len(self.vectors):
                if not constants.WAY.is_end:
                    constants.WAY.end_level()
                continue
            ball.update_direction(self.vectors[ball.index_way])
            ball.update()
            ball.index_way += 1
        if self.id == 0:
            return
        snake = constants.WAY.snakes[self.id - 1]
        if len(snake.balls) == 0:
            return
        if self.balls[0].color == snake.balls[-1].color:
            snake.status = Status.Back
            self.status = Status.Stop
            return
        difference = abs(self.balls[0].index_way - snake.balls[-1].index_way)
        if difference <= 20:
            snake.status = Status.Forward
            for i in range(20 - difference):
                snake.update()
            snake.balls = snake.balls + self.balls
            constants.WAY.snakes.pop(self.id)
        recover_indexes()

    def __stop(self):
        if self.id != 0 and constants.WAY.snakes[self.id - 1].status == Status.Stop:
            snake = constants.WAY.snakes[self.id - 1]
            difference = abs(snake.balls[-1].index_way - self.balls[0].index_way)
            if difference <= 20:
                snake.status = Status.Forward
                for i in range(20 - difference):
                    snake.update()
                snake.status = Status.Stop
                snake.balls = snake.balls + self.balls
                constants.WAY.snakes.pop(self.id)
                recover_indexes()
                return
        for ball in self.balls:
            ball.update_direction(Vector2(0, 0))
            ball.update()

    def __back(self):
        if self.id != len(constants.WAY.snakes) - 1:
            if constants.WAY.snakes[self.id + 1].status == Status.Forward:
                self.status = Status.Stop
                return
        for i in range(3):
            for i, ball in enumerate(self.balls):
                if ball.index_way - 1 == -1:
                    self.balls.pop(i)
                    if len(self.balls) == 0:
                        constants.WAY.snakes.pop(self.id)
                    continue
                ball.update_direction(-1 * self.vectors[ball.index_way - 1])
                ball.update()
                ball.index_way -= 1
            if constants.WAY.reverse_count > 0 or len(constants.WAY.snakes) == self.id + 1:
                return
            difference = abs(self.balls[-1].index_way - constants.WAY.snakes[self.id + 1].balls[0].index_way)
            if difference <= 20:
                self.status = Status.Forward
                for i in range(20 - difference):
                    self.update()
                index = len(self.balls) - 1
                self.balls = self.balls + constants.WAY.snakes[self.id + 1].balls
                constants.WAY.snakes.pop(self.id + 1)
                recover_indexes()
                self.status = Status.Stop
                snakes = constants.WAY.snakes
                for i in range(len(snakes) - 1, -1, -1):
                    if snakes[i].status == Status.Forward:
                        break
                    if snakes[i].status == Status.Stop:
                        snakes[i].status = Status.Forward
                        break
                self.remove_balls(index)
                break

    def insert_ball_into_beginning(self, color):
        self.insert_ball(None,
                         self.balls[0].index_way + 20,
                         0,
                         color,
                         lambda index, old_color: color)
        # self.sound_insert_ball.play()
        # sum_vectors = self.calculate_sum_vectors()
        #
        # new_ball = Ball(self.balls[0].center + sum_vectors)
        # new_ball.index_way = self.balls[0].index_way + 20
        # new_ball.update_direction(self.vectors[new_ball.index_way])
        # new_ball.change_color(color)
        #
        # self.balls.insert(0, new_ball)
        # self.remove_balls(0)

    def insert_ball_into_middle(self, index, color):
        self.insert_ball(index,
                         min(self.balls[0].index_way + 20,
                             len(self.vectors) - 1),
                         index + 1,
                         color,
                         self.repainting)
        # self.sound_insert_ball.play()
        # sum_vectors = self.calculate_sum_vectors()
        #
        # cur_color = color
        # for i in range(index, -1, -1):
        #     temp = self.balls[i].color
        #     self.balls[i].change_color(cur_color)
        #     cur_color = temp
        #
        # new_ball = Ball(self.balls[0].center + sum_vectors)
        # new_ball.index_way = min(self.balls[0].index_way + 20, len(self.vectors) - 1)
        # new_ball.update_direction(self.vectors[new_ball.index_way])
        # new_ball.change_color(cur_color)
        #
        # self.balls.insert(0, new_ball)
        # self.remove_balls(index + 1)

    def insert_ball(self,
                    index_for_repainting,
                    index_way,
                    remove_index,
                    color,
                    repainting):

        self.sound_insert_ball.play()
        sum_vectors = self.calculate_sum_vectors()
        cur_color = repainting(index_for_repainting, color)

        new_ball = Ball(self.balls[0].center + sum_vectors)
        new_ball.index_way = index_way
        new_ball.update_direction(self.vectors[new_ball.index_way])
        new_ball.change_color(cur_color)

        self.balls.insert(0, new_ball)
        self.remove_balls(remove_index)


    def repainting(self, index, color):
        cur_color = color
        for i in range(index, -1, -1):
            temp = self.balls[i].color
            self.balls[i].change_color(cur_color)
            cur_color = temp
        return cur_color

    def calculate_sum_vectors(self):
        sum_vectors = Vector2(0, 0)
        for i in range(self.balls[0].index_way,
                       min(self.balls[0].index_way + 20,
                           len(self.vectors))):
            sum_vectors += self.vectors[i]
        return sum_vectors


    def remove_balls(self, index):
        color = self.balls[index].color
        indexes = self.__find_matching_color_balls(index, color)

        if len(indexes) <= 2:
            return

        indexes.sort(reverse=True)
        self.sound_remove_balls.play()

        if self.__is_last_ball_in_snake(indexes):
            self.balls = self.balls[:indexes[-1]]
            if len(constants.WAY.snakes) != 1:
                return
            self.status = Status.Stop
            constants.WAY.snakes.append(Snake(constants.WAY.vectors, 1))
            return

        if self.__is_first_ball_in_snake(indexes):
            self.balls = self.balls[indexes[0] + 1:]
            return

        self.split(indexes)

    def __find_matching_color_balls(self, index, color):
        indexes = [index]
        for direction in (-1, 1):
            i = index + direction
            while 0 <= i < len(self.balls):
                if self.balls[i].color == color:
                    indexes.append(i)
                    i += direction
                else:
                    break
        return indexes

    def __is_last_ball_in_snake(self, indexes):
        return indexes[0] == len(self.balls) - 1

    def __is_first_ball_in_snake(self, indexes):
        return indexes[-1] == 0

    def split(self, indexes):
        new_ball, cur_ball = self.__split_balls(indexes)
        new_snake = self.__create_new_snake(new_ball)

        self.balls = cur_ball
        constants.WAY.snakes.insert_ball_into_middle(self.id + 1, new_snake)
        recover_indexes()

        self.__check_and_update_status(new_snake, cur_ball, new_ball, indexes)

    # Новый метод для разделения шаров
    def __split_balls(self, indexes):
        new_ball = self.balls[indexes[0] + 1:]
        cur_ball = self.balls[0: indexes[-1]]
        return new_ball, cur_ball

    # Новый метод для создания новой змеи
    def __create_new_snake(self, new_ball):
        new_snake = Snake(self.vectors, 0)
        new_snake.balls = new_ball
        return new_snake

    # Новый метод для проверки и обновления статуса змей
    def __check_and_update_status(self, new_snake, cur_ball, new_ball, indexes):
        if new_ball[0].color == cur_ball[-1].color:
            self.status = Status.Back
            new_snake.status = Status.Stop
            constants.SCORE.add(len(indexes))
            return

        if self.status == Status.Stop:
            new_snake.status = Status.Stop

        self.status = Status.Stop
        constants.SCORE.add(len(indexes))

