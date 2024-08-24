import pygame as pg
class Frog:
    def __init__(self, screen):
        self.screen = screen
        self.sprite_image = pg.image.load("player.png")

    def update(self):
        new_sprite_image = pg.transform.scale(self.sprite_image,(500, 500))
        frog_rect = new_sprite_image.get_rect()
        frog_rect.topleft = (225, 225)
        self.screen.blit(new_sprite_image, frog_rect)
        #pg.draw.rect(self.screen, [0, 255, 0], [225, 225, 25, 25])


        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("Нажата левая кнопка мыши")
                elif event.button == 3:
                    print("Нажата правая кнопка мыши")
            a = pg.mouse.get_pos()
            print(a)
