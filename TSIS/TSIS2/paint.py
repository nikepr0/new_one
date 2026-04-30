import pygame
import sys
import datetime
from tools import flood_fill, draw_shape

pygame.init()

WIDTH, HEIGHT = 1000, 650
SIDEBAR_WIDTH = 220

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint (Structured)")

canvas = pygame.Surface((WIDTH - SIDEBAR_WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()

# COLORS
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (200,200,200)
DARK = (150,150,150)

palette = [
    (0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),
    (255,255,0),(255,0,255),(0,255,255),
    (128,0,0),(0,128,0),(0,0,128),
    (255,128,0),(128,0,255),(0,128,128)
]

current_color = BLACK
current_tool = "pencil"
brush_size = 3
current_tab = "tools"

drawing = False
start_pos = None
last_pos = None

font = pygame.font.SysFont(None, 22)
text_font = pygame.font.SysFont(None, 28)

text_mode = False
text_input = ""
text_pos = (0,0)

# UNDO
undo_stack = [canvas.copy()]
redo_stack = []

def save_state():
    undo_stack.append(canvas.copy())
    redo_stack.clear()

# BUTTON
class Button:
    def __init__(self,x,y,w,h,text,value):
        self.rect = pygame.Rect(x,y,w,h)
        self.text = text
        self.value = value

    def draw(self,active=False):
        color = DARK if active else GRAY
        pygame.draw.rect(screen,color,self.rect)
        pygame.draw.rect(screen,BLACK,self.rect,2)
        txt = font.render(self.text,True,BLACK)
        screen.blit(txt,(self.rect.x+5,self.rect.y+5))

    def clicked(self,pos):
        return self.rect.collidepoint(pos)

# UI
tabs = [
    Button(0,0,220,40,"TOOLS","tools"),
    Button(0,40,220,40,"SHAPES","shapes"),
    Button(0,80,220,40,"COLORS","colors"),
]

tools_btns = [
    Button(10,140,200,40,"Pencil","pencil"),
    Button(10,190,200,40,"Line","line"),
    Button(10,240,200,40,"Eraser","eraser"),
    Button(10,290,200,40,"Fill","fill"),
    Button(10,340,200,40,"Text","text"),
    Button(10,390,200,40,"Picker","picker"),
    Button(10,440,200,40,"Clear","clear"),
]

shapes_btns = [
    Button(10,140,200,40,"Rectangle","rect"),
    Button(10,190,200,40,"Circle","circle"),
    Button(10,240,200,40,"Square","square"),
    Button(10,290,200,40,"Right Tri","right_triangle"),
    Button(10,340,200,40,"Eq Tri","equilateral_triangle"),
    Button(10,390,200,40,"Rhombus","rhombus"),
]

sizes = [
    Button(10,500,60,40,"S",4),
    Button(80,500,60,40,"M",8),
    Button(150,500,60,40,"L",16),
]

undo_btn = Button(10,560,90,40,"Undo","undo")
redo_btn = Button(120,560,90,40,"Redo","redo")

preview = canvas.copy()

# LOOP
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            for t in tabs:
                if t.clicked(event.pos):
                    current_tab = t.value

            for b in tools_btns:
                if current_tab=="tools" and b.clicked(event.pos):
                    current_tool = b.value

            for b in shapes_btns:
                if current_tab=="shapes" and b.clicked(event.pos):
                    current_tool = b.value

            for b in sizes:
                if b.clicked(event.pos):
                    brush_size = b.value

            if undo_btn.clicked(event.pos) and undo_stack:
                redo_stack.append(canvas.copy())
                canvas = undo_stack.pop()

            if redo_btn.clicked(event.pos) and redo_stack:
                undo_stack.append(canvas.copy())
                canvas = redo_stack.pop()

            if current_tab=="colors":
                for i,c in enumerate(palette):
                    x = 10 + (i%4)*50
                    y = 140 + (i//4)*50
                    if pygame.Rect(x,y,40,40).collidepoint(event.pos):
                        current_color = c

            if event.pos[0] > SIDEBAR_WIDTH:
                drawing = True
                start_pos = (event.pos[0]-SIDEBAR_WIDTH,event.pos[1])
                last_pos = start_pos

                if current_tool=="fill":
                    flood_fill(canvas,*start_pos,current_color)
                    save_state()

                elif current_tool=="picker":
                    current_color = canvas.get_at(start_pos)

                elif current_tool=="clear":
                    canvas.fill(WHITE)
                    save_state()

                elif current_tool=="text":
                    text_mode = True
                    text_input = ""
                    text_pos = start_pos

        if event.type == pygame.MOUSEBUTTONUP:
            if drawing and current_tool in ["rect","circle","square","right_triangle","equilateral_triangle","rhombus","line"]:
                end=(event.pos[0]-SIDEBAR_WIDTH,event.pos[1])
                if current_tool=="line":
                    pygame.draw.line(canvas,current_color,start_pos,end,brush_size)
                else:
                    draw_shape(canvas,current_tool,start_pos,end,current_color,brush_size)
                save_state()
            drawing=False

        if event.type == pygame.MOUSEMOTION and drawing:
            pos=(event.pos[0]-SIDEBAR_WIDTH,event.pos[1])

            if current_tool=="pencil":
                pygame.draw.line(canvas,current_color,last_pos,pos,brush_size)
                last_pos=pos

            elif current_tool=="eraser":
                pygame.draw.line(canvas,WHITE,last_pos,pos,brush_size)
                last_pos=pos

            elif current_tool in ["rect","circle","square","right_triangle","equilateral_triangle","rhombus","line"]:
                preview=canvas.copy()
                if current_tool=="line":
                    pygame.draw.line(preview,current_color,start_pos,pos,brush_size)
                else:
                    draw_shape(preview,current_tool,start_pos,pos,current_color,brush_size)

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                name=datetime.datetime.now().strftime("paint_%H%M%S.png")
                pygame.image.save(canvas,name)

            if text_mode:
                if event.key == pygame.K_RETURN:
                    txt = text_font.render(text_input, True, current_color)
                    canvas.blit(txt, text_pos)
                    text_mode = False
                    save_state()
                elif event.key == pygame.K_ESCAPE:
                    text_mode = False
                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    if event.unicode.isprintable():
                        text_input += event.unicode

    # DRAW
    screen.fill((230,230,230))
    pygame.draw.rect(screen,(210,210,210),(0,0,SIDEBAR_WIDTH,HEIGHT))

    for t in tabs:
        t.draw(current_tab==t.value)

    if current_tab=="tools":
        for b in tools_btns:
            b.draw(current_tool==b.value)

    elif current_tab=="shapes":
        for b in shapes_btns:
            b.draw(current_tool==b.value)

    elif current_tab=="colors":
        for i,c in enumerate(palette):
            x = 10 + (i%4)*50
            y = 140 + (i//4)*50
            pygame.draw.rect(screen,c,(x,y,40,40))
            pygame.draw.rect(screen,BLACK,(x,y,40,40),2)

    for b in sizes:
        b.draw(brush_size==b.value)

    undo_btn.draw()
    redo_btn.draw()

    if drawing and current_tool in ["rect","circle","square","right_triangle","equilateral_triangle","rhombus","line"]:
        screen.blit(preview,(SIDEBAR_WIDTH,0))
    else:
        screen.blit(canvas,(SIDEBAR_WIDTH,0))

    if text_mode:
        temp = canvas.copy()
        txt = text_font.render(text_input, True, current_color)
        temp.blit(txt, text_pos)
        screen.blit(temp, (SIDEBAR_WIDTH, 0))

    pygame.display.flip()
    clock.tick(60)