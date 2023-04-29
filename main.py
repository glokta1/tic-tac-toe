import pygame
import sys
import numpy as np

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SQUARE_LENGTH = SCREEN_WIDTH / 3

pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

# colors
TURQUOISE = pygame.Color("#14bdac")
DARK_TURQUOISE = pygame.Color("#0da192")
COLOR1 = (84, 84, 84)
COLOR2 = (242, 235, 211)

# surfaces
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# board
board = np.zeros((3, 3))


def draw_board():
    screen.fill(TURQUOISE)
    draw_lines()

    for row in range(3):
        for col in range(3):
            # if board[row][col] == 1:
            #     # draw_cross()
            if board[row][col] == 2:
                pygame.draw.circle(
                    screen,
                    COLOR2,
                    (
                        col * (SQUARE_LENGTH) + SQUARE_LENGTH / 2,
                        row * (SQUARE_LENGTH) + SQUARE_LENGTH / 2,
                    ),
                    SQUARE_LENGTH / 2.5,
                    10,
                )


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


def mark_square(row, col, player):
    board[row][col] = player


def is_available(row, col):
    return board[row][col] == 0


# maps pygame's screen coordinates to board coordinates
def pygame_to_board(pgX, pgY):
    return int(pgY // (SQUARE_LENGTH)), int(pgX // (SQUARE_LENGTH))


PLAYER1 = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pgX, pgY = pygame.mouse.get_pos()
            boardX, boardY = pygame_to_board(pgX, pgY)
            print(boardX, boardY)
            if is_available(boardX, boardY):
                if PLAYER1:
                    mark_square(boardX, boardY, 1)
                    PLAYER1 = False
                else:
                    mark_square(boardX, boardY, 2)
                    PLAYER1 = True

    draw_board()
    # pygame.draw.circle(
    #     screen,
    #     COLOR2,
    #     (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
    #     SCREEN_WIDTH / 7,
    #     15,
    # )

    pygame.display.flip()
    clock.tick(60)
