import pygame

pygame.init()

def flood_fill(surface, x, y, new_color):
    target = surface.get_at((x, y))
    if target == new_color:
        return

    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if surface.get_at((x, y)) == target:
            surface.set_at((x, y), new_color)

            if x > 0:
                stack.append((x - 1, y))
            if x < surface.get_width() - 1:
                stack.append((x + 1, y))
            if y > 0:
                stack.append((x, y - 1))
            if y < surface.get_height() - 1:
                stack.append((x, y + 1))



def draw_shape(surface, tool, start, end, color, size):
    x1, y1 = start
    x2, y2 = end

    rect = pygame.Rect(min(x1, x2), min(y1, y2),
                       abs(x1 - x2), abs(y1 - y2))

    if tool == "rect":
        pygame.draw.rect(surface, color, rect, size)

    elif tool == "circle":
        pygame.draw.ellipse(surface, color, rect, size)

    elif tool == "square":
        s = min(rect.w, rect.h)
        pygame.draw.rect(surface, color, (rect.x, rect.y, s, s), size)

    elif tool == "right_triangle":
        pygame.draw.polygon(surface, color, [
            (x1, y2), (x1, y1), (x2, y2)
        ], size)

    elif tool == "equilateral_triangle":
        mid = (x1 + x2) // 2
        pygame.draw.polygon(surface, color, [
            (mid, y1), (x1, y2), (x2, y2)
        ], size)

    elif tool == "rhombus":
        pygame.draw.polygon(surface, color, [
            ((x1 + x2) // 2, y1),
            (x2, (y1 + y2) // 2),
            ((x1 + x2) // 2, y2),
            (x1, (y1 + y2) // 2)
        ], size)