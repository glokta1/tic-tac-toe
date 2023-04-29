import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

# colors
TURQUOISE = pygame.Color("#14bdac")
DARK_TURQUOISE = pygame.Color("#0da192")
COLOR1 = (84, 84, 84)
COLOR2 = (242, 235, 211)

# surfaces
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True


def draw_lines():
    # left vertical
    pygame.draw.line(
        screen,
        DARK_TURQUOISE,
        (SCREEN_WIDTH / 3, 0),
        (SCREEN_WIDTH / 3, SCREEN_HEIGHT),
        width=15,
    )

    # right vertical
    pygame.draw.line(
        screen,
        DARK_TURQUOISE,
        (2 * SCREEN_WIDTH / 3, 0),
        (2 * SCREEN_WIDTH / 3, SCREEN_HEIGHT),
        width=15,
    )

    # top horizontal
    pygame.draw.line(
        screen,
        DARK_TURQUOISE,
        (0, SCREEN_HEIGHT / 3),
        (SCREEN_WIDTH, SCREEN_HEIGHT / 3),
        width=15,
    )

    # bottom horizontal
    pygame.draw.line(
        screen,
        DARK_TURQUOISE,
        (0, 2 * SCREEN_HEIGHT / 3),
        (SCREEN_WIDTH, 2 * SCREEN_HEIGHT / 3),
        width=15,
    )


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(TURQUOISE)
    draw_lines()

    pygame.display.flip()
    clock.tick(60)
