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

    grid: Grid = Grid(32, 32, screen, font=font)
    print("Created grid")

    screen.fill((0, 0, 0))  # Black

    grid.draw()

    pygame.display.flip()
    print("Drawn")

    z = 1
    while True:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))

        ta = time.perf_counter()
        grid.set_corners(z)
        ta = time.perf_counter() - ta

        tb = time.perf_counter()
        grid.draw()
        tb = time.perf_counter() - tb
        print(f'{ta:.2f}, {tb:.2f}')

        pygame.display.flip()
        z += dt * .1


if __name__ == "__main__":
    main()
