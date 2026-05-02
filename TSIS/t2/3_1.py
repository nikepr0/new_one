import pygame
import sys
from tools import flood_fill, draw_shape

pygame.init()


# SETUP

WIDTH, HEIGHT    = 1200, 700
TOOLBAR_HEIGHT   = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

# Two surfaces:
canvas  = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
preview = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT), pygame.SRCALPHA)
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()

# COLORS

BLACK  = (0,   0,   0)
WHITE  = (255, 255, 255)
RED    = (255, 0,   0)
GREEN  = (0,   200, 0)
BLUE   = (0,   0,   255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0,   128)
GRAY   = (200, 200, 200)
DARK   = (50,  50,  50)

PALETTE = [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE]




current_color = BLACK
current_tool  = "pencil"
brush_size    = 5




def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(
        min(x1, x2),
        min(y1, y2),
        abs(x1 - x2),
        abs(y1 - y2)
    )



font = pygame.font.SysFont(None, 22)

tools = ["pencil", "eraser", "rect", "circle", "square",
         "right_triangle", "equilateral_triangle", "rhombus", "fill", "line"]

def draw_toolbar():
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, TOOLBAR_HEIGHT))

    # colors
    for i, color in enumerate(PALETTE):
        x = 10 + i * 45
        pygame.draw.rect(screen, color, (x, 10, 35, 35))
        if color == current_color:
            pygame.draw.rect(screen, DARK, (x, 10, 35, 35), 3)

    # tools
    for i, tool in enumerate(tools):
        x = 380 + i * 90
        col = DARK if current_tool == tool else BLACK
        pygame.draw.rect(screen, WHITE, (x, 10, 80, 35))
        pygame.draw.rect(screen, col,   (x, 10, 80, 35), 2)
        text = font.render(tool.capitalize(), True, col)
        screen.blit(text, (x + 8, 20))

    # brush size indicator
    bx = 560 + len(tools) * 10
    pygame.draw.circle(screen, current_color, (750, 30), brush_size)
    size_text = font.render(f"Size: {brush_size}", True, BLACK)
    screen.blit(size_text, (770, 20))

def get_tool_click(x, y):
    for i, tool in enumerate(tools):
        tx = 380 + i * 90
        if tx <= x <= tx + 80 and 10 <= y <= 45:
            return tool
    return None


# MAIN LOOP

def main():
    global current_color, current_tool, brush_size

    running   = True
    drawing   = False
    last_pos  = None
    start_pos = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    brush_size = min(brush_size + 2, 50)
                if event.key == pygame.K_DOWN:
                    brush_size = max(brush_size - 2, 1)
                if event.key == pygame.K_1:   brush_size = 2
                if event.key == pygame.K_2:   brush_size = 5
                if event.key == pygame.K_3:   brush_size = 10
                if event.key == pygame.K_p:   current_tool = "pencil"
                if event.key == pygame.K_e:   current_tool = "eraser"
                if event.key == pygame.K_r:   current_tool = "rect"
                if event.key == pygame.K_o:   current_tool = "circle"
                if event.key == pygame.K_s:   current_tool = "square"
                if event.key == pygame.K_t:   current_tool = "right_triangle"
                if event.key == pygame.K_y:   current_tool = "equilateral_triangle"
                if event.key == pygame.K_h:   current_tool = "rhombus"
                if event.key == pygame.K_f:   current_tool = "fill"
                if event.key == pygame.K_l:   current_tool = "line"
                if event.key == pygame.K_c:   canvas.fill(WHITE)  

            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos

                if y < TOOLBAR_HEIGHT:
                    
                    for i, color in enumerate(PALETTE):
                        cx = 10 + i * 45
                        if cx <= x <= cx + 35 and 10 <= y <= 45:
                            current_color = color
                            current_tool  = "pencil"

                    
                    clicked = get_tool_click(x, y)
                    if clicked:
                        current_tool = clicked
                else:
                    canvas_y = y - TOOLBAR_HEIGHT
                    if current_tool == "fill":
                        flood_fill(canvas, x, canvas_y, current_color)
                    else:
                        drawing   = True
                        last_pos  = (x, canvas_y)
                        start_pos = (x, canvas_y)

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if drawing and start_pos:
                    x, y     = event.pos
                    canvas_y = y - TOOLBAR_HEIGHT

                    shape_tools = ["rect", "circle", "square",
                                   "right_triangle", "equilateral_triangle",
                                   "rhombus", "line"]

                    if current_tool in shape_tools:
                        if current_tool == "line":
                            pygame.draw.line(canvas, current_color,
                                start_pos, (x, canvas_y), brush_size)
                        else:
                            draw_shape(canvas, current_tool, start_pos,
                                (x, canvas_y), current_color, brush_size)

                drawing   = False
                last_pos  = None
                start_pos = None
                preview.fill((0, 0, 0, 0))

            
            if event.type == pygame.MOUSEMOTION and drawing:
                x, y     = event.pos
                canvas_y = y - TOOLBAR_HEIGHT

                if y > TOOLBAR_HEIGHT:
                    if current_tool == "pencil" and last_pos:
                        pygame.draw.line(canvas, current_color, last_pos, (x, canvas_y), brush_size)
                    elif current_tool == "eraser" and last_pos:
                        pygame.draw.line(canvas, WHITE, last_pos, (x, canvas_y), brush_size * 3)
                    
                    elif current_tool in ["rect", "circle", "square",
                                          "right_triangle", "equilateral_triangle",
                                          "rhombus"] and start_pos:
                        preview.fill((0, 0, 0, 0))
                        draw_shape(preview, current_tool, start_pos,
                            (x, canvas_y), current_color, brush_size)

                    elif current_tool == "line" and start_pos:
                        preview.fill((0, 0, 0, 0))
                        pygame.draw.line(preview, current_color,
                            start_pos, (x, canvas_y), brush_size)
                        
                    last_pos = (x, canvas_y)

        
        screen.blit(canvas,  (0, TOOLBAR_HEIGHT))
        screen.blit(preview, (0, TOOLBAR_HEIGHT))
        draw_toolbar()
        pygame.display.flip()
        clock.tick(60)

main()