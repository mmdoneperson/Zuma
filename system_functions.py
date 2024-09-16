import pygame as pg
import sys


def start_music(music_name):
    pg.mixer.music.load(music_name)
    pg.mixer.music.set_volume(0)
    pg.mixer.music.play(-1)


def pause_music():
    pg.mixer_music.pause()


def close_game():
    pg.quit()
    sys.exit()