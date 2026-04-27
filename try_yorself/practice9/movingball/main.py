import pygame as pg

pg.init()
WIDTH, HEIGHT = 400, 400


class Ball(pg.sprite.Sprite):
            def __init__(self):
                super().__init__()                                      # required
                self.image = pg.Surface((50, 50))
                self.image.fill((0, 0, 0))  # Make black transparent
                pg.draw.circle(self.image, (255, 50, 50), (25, 25), 25)
                self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

            def update(self):
                
                keys = pg.key.get_pressed()
                if keys[pg.K_LEFT]:  self.rect.move_ip(-5, 0)
                if keys[pg.K_RIGHT]: self.rect.move_ip(5, 0)
                if keys[pg.K_UP]:    self.rect.move_ip(0, -5)
                if keys[pg.K_DOWN]:  self.rect.move_ip(0, 5)

screen=pg.display.set_mode((900,500))
pg.display.set_caption("Moving Ball")

d=True
fps=pg.time.Clock()

ball = Ball()

all_sprites = pg.sprite.Group()
all_sprites.add(ball)


while d:
    pg.draw.circle(screen , (255, 67, 67) ,(50,50), 25)
    for ee in pg.event.get():
        if ee.type==pg.QUIT:
            d=False
            
    all_sprites.update()        

    screen.fill("black")
    all_sprites.draw(screen)
            
    pg.display.flip()
    screen.fill((255,255,255))
    fps.tick(500)
pg.quit()