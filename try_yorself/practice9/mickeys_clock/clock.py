import pygame
import math
import time

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

clock = pygame.time.Clock()
CENTER = (WIDTH // 2, HEIGHT // 2)

# Load and scale the Mickey clock image
bg_image = pygame.image.load("mickeyclock.jpeg")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

# Mickey's hand pivot point (center of his body, roughly)
HAND_PIVOT = (WIDTH // 2, HEIGHT // 2 - 20)  # slightly above center

# Hand lengths (tune to match image proportions)
MINUTE_LENGTH = 180   # Mickey's RIGHT hand → minute
SECOND_LENGTH = 160   # Mickey's LEFT hand  → second

# Colors
RED   = (220, 30, 30)
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)

def draw_mickey_hand(surface, color, angle_deg, length, width, is_right_hand):
    """
    Draw Mickey's arm as a gloved hand pointer.
    is_right_hand=True  → minute hand (points RIGHT side of clock)
    is_right_hand=False → second hand (points LEFT side of clock)
    angle_deg is clockwise from 12 o'clock.
    """
    angle_rad = math.radians(angle_deg - 90)
    tip_x = HAND_PIVOT[0] + length * math.cos(angle_rad)
    tip_y = HAND_PIVOT[1] + length * math.sin(angle_rad)

    # Draw arm line
    pygame.draw.line(surface, color, HAND_PIVOT, (int(tip_x), int(tip_y)), width)

    # Draw glove circle at tip
    glove_radius = width + 6
    pygame.draw.circle(surface, WHITE, (int(tip_x), int(tip_y)), glove_radius)
    pygame.draw.circle(surface, BLACK, (int(tip_x), int(tip_y)), glove_radius, 2)

    # Draw pointing finger line extending from glove
    finger_len = 20
    fx = tip_x + finger_len * math.cos(angle_rad)
    fy = tip_y + finger_len * math.sin(angle_rad)
    pygame.draw.line(surface, WHITE, (int(tip_x), int(tip_y)), (int(fx), int(fy)), 6)
    pygame.draw.circle(surface, WHITE, (int(fx), int(fy)), 5)
    pygame.draw.circle(surface, BLACK, (int(fx), int(fy)), 5, 2)

def get_hand_angles():
    now = time.localtime()
    seconds = now.tm_sec
    minutes = now.tm_min + seconds / 60
    hours   = now.tm_hour % 12 + minutes / 60

    hour_angle   = hours   * 30    # 360/12
    minute_angle = minutes * 6     # 360/60
    second_angle = seconds * 6     # 360/60

    return hour_angle, minute_angle, second_angle

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background image
    screen.blit(bg_image, (0, 0))

    hour_angle, minute_angle, second_angle = get_hand_angles()

    # Mickey's RIGHT hand = Minute hand (white/thick)
    draw_mickey_hand(screen, WHITE, minute_angle, MINUTE_LENGTH, width=8,
                     is_right_hand=True)

    # Mickey's LEFT hand = Second hand (red/thin)
    draw_mickey_hand(screen, RED,   second_angle, SECOND_LENGTH, width=4,
                     is_right_hand=False)

    # Center pivot dot
    pygame.draw.circle(screen, BLACK, HAND_PIVOT, 10)
    pygame.draw.circle(screen, WHITE, HAND_PIVOT, 6)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()