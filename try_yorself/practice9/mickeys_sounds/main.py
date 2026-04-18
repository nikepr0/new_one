import pygame as pg

pg.mixer.music.load('clock.mp3')
pg.mixer.music.play(-1)

d=True
while d:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            d=False
        pg.display.flip()
pg.quit()