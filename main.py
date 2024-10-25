import pygame
import sys

from grid import Grid


def main():
    pygame.init()
    pygame.font.init()

    font: pygame.font.Font = pygame.font.Font(None, 24)
    screen_width, screen_height = 600, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Marching Squares")

    grid: Grid = Grid(10, 10, screen, font=font)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # Black

        grid.draw()

        pygame.display.flip()


if __name__ == "__main__":
    main()
