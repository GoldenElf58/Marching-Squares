import pygame
import sys

from line import Line
from rectangle import Rectangle
from shape import Shape


def main():
    pygame.init()

    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Square and Line Display")

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)

    square: Rectangle = Rectangle(200, 200, 300, 300, red, screen)
    line: Line = Line(100, 100, 700, 500, 5, green, screen)

    shapes: list[Shape] = [square, line]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(black)

        for shape in shapes:
            shape.draw()

        pygame.display.flip()


if __name__ == "__main__":
    main()
