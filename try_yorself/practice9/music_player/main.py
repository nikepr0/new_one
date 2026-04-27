import pygame as pp

pp.init()
m=['clock.mp3','2.mp3','3.mp3']
screen=pp.display.set_mode((1000,600))
pp.display.set_caption("Music Player")
d=True
s=0
pp.mixer.music.load(m[s])
pp.mixer.music.play(0)
while d:
    for event in pp.event.get():
            
        if event.type==pp.QUIT:
            d=False
        if event.type == pp.KEYDOWN and event.key == pp.K_s:
            pp.mixer.music.stop()
        if event.type == pp.KEYDOWN and event.key == pp.K_p:
            pp.mixer.music.play()
        if event.type == pp.KEYDOWN and event.key == pp.K_n:
            s = (s + 1) % len(m)      
            pp.mixer.music.load(m[s])
            pp.mixer.music.play()
        if event.type == pp.KEYDOWN and event.key == pp.K_b:
                s = (s - 1) % len(m)      
                pp.mixer.music.load(m[s])
                pp.mixer.music.play()
        if event.type == pp.KEYDOWN and event.key == pp.K_q:
            d=False
            
        pp.display.flip()
        screen.fill((0,0,0))
pp.quit()