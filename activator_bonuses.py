import constants
import pygame as pg

class Activator:
    def __init__(self):
        self.bonuses = []
        self.bombs = []

    def append(self, bonus):
        self.bonuses.append(bonus)

    def update(self):
        for bonus in self.bonuses:
            if bonus == 'reverse':
                if constants.WAY.stop_count > 0:
                    constants.WAY.stop_count = 0
                    constants.WAY.reverse(constants.WAY.statuses)
                else:
                    constants.WAY.reverse()
            if bonus == 'pause':
                if constants.WAY.reverse_count > 0:
                    constants.WAY.reverse_count = 0
                    constants.WAY.stop(constants.WAY.statuses)
                else:
                    constants.WAY.stop()
            if bonus == 'speed':
                constants.FROG.speed_up_shoot()
        self.bonuses.clear()

    def activate_bomb(self, is_begin_or_end = True):
        radius_explosion = 100
        red = (255, 0, 0)
        if is_begin_or_end:
            bomb = self.bombs[0]
            pg.draw.circle(constants.screen,
                           red, (bomb.x, bomb.y), radius_explosion)
            for snake in constants.WAY.snakes:
                indexes = []
                is_added_index_in_indexes = False
                for i, ball in enumerate(snake.balls):
                    if (ball.center - bomb).length() < radius_explosion + constants.radius_ball:
                        indexes.append(i)
                        if i == len(snake.balls) - 1:
                            self.kek(snake, indexes)
                            is_added_index_in_indexes = False
                        else:
                            is_added_index_in_indexes = True
                    else:
                        if is_added_index_in_indexes:
                            self.kek(snake, indexes)
                            # print(indexes)
                            # indexes.sort(reverse=True)
                            # if indexes[-1] == 0 and indexes[0] == len(snake.balls) - 1:
                            #     constants.WAY.snakes.pop(snake.id)
                            #     for i in range(len(constants.WAY.snakes)):
                            #         constants.WAY.snakes[i].id = i
                            # else:
                            #     if indexes[-1] == 0:
                            #         snake.balls = snake.balls[indexes[0] + 1:]
                            #     else:
                            #         snake.balls = snake.balls[:indexes[-1]]
                            # is_added_index_in_indexes = False
                            break
                # if len(indexes) == 0:
                #     continue
                # indexes.sort(reverse=True)
                # snake.split(indexes)
            self.bombs.clear()
        else:
            bomb = self.bombs[0]
            pg.draw.circle(constants.screen,
                           red, (bomb.x, bomb.y), radius_explosion)
            for snake in constants.WAY.snakes:
                indexes = []
                is_added_index_in_indexes = False
                for i, ball in enumerate(snake.balls):
                    if (ball.center - bomb).length() < radius_explosion + constants.radius_ball:
                        indexes.append(i)
                        is_added_index_in_indexes = True
                    else:
                        if is_added_index_in_indexes:
                            indexes.sort(reverse=True)
                            snake.split(indexes)
                            indexes = []
                            break
                # if len(indexes) == 0:
                #     continue
                # indexes.sort(reverse=True)
                # snake.split(indexes)
            self.bombs.clear()


    def kek(self, snake, indexes):
        indexes.sort(reverse=True)
        if indexes[-1] == 0 and indexes[0] == len(snake.balls) - 1:
            constants.WAY.snakes.pop(snake.id)
            for i in range(len(constants.WAY.snakes)):
                constants.WAY.snakes[i].id = i
        else:
            if indexes[-1] == 0:
                snake.balls = snake.balls[indexes[0] + 1:]
            elif indexes[0] == len(snake.balls) - 1:
                snake.balls = snake.balls[:indexes[-1]]
            else:
                snake.split(indexes)