import pygame

pygame.init()

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(
        min(x1, x2),
        min(y1, y2),
        abs(x1 - x2),
        abs(y1 - y2)
    )
    

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

LMBpressed = False
THICKNESS = 3
startX = startY = 0
currX  = currY  = 0

screen.fill("white")

color   = (0, 0, 0)
radius  = 5
drawing = False

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            startX, startY = event.pos
        
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                currX, currY = event.pos
                pygame.draw.rect(
                    screen, "red",
                    calculate_rect(startX, startY, currX, currY),
                    THICKNESS
                )
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            currX, currY = event.pos
            pygame.draw.rect(
                screen, "red",
                calculate_rect(startX, startY, currX, currY),
                THICKNESS
            )

            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  color = (255, 0, 0)
            if event.key == pygame.K_g:  color = (0, 255, 0)
            if event.key == pygame.K_b:  color = (0, 0, 255)
            if event.key == pygame.K_k:  color = (0, 0, 0)
            if event.key == pygame.K_e:  color = (255, 255, 255)  # eraser
            if event.key == pygame.K_c:  screen.fill("white")     # clear
            if event.key == pygame.K_UP:   radius = min(radius + 2, 50)
            if event.key == pygame.K_DOWN: radius = max(radius - 2, 1)
            
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)
            if event.key == pygame.K_c:
                screen.fill("black")


    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, color, mouse_pos, radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

