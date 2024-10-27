import sys
import time

import pygame

from grid import Grid


def main():
    pygame.init()
    pygame.font.init()

    font: pygame.font.Font = pygame.font.Font(None, 12)
    screen_width, screen_height = 512, 512
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Marching Squares")
    clock: pygame.time.Clock = pygame.time.Clock()

    grid: Grid = Grid(64, 64, screen, font=font)
    print("Created grid")

    screen.fill((0, 0, 0))  # Black

    grid.draw()

    pygame.display.flip()
    print("Drawn")

    z = 0
    while True:
        z += .02
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))

        grid.set_corners(z)
        grid.draw()

        print(1 / dt)

        pygame.display.flip()


if __name__ == "__main__":
    main()
