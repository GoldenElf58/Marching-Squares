import pygame

from shape import Shape


class Line(Shape):
    def __init__(self, x1: int, y1: int, x2: int, y2: int, width: int, color: tuple = (255, 0, 0), screen=None) -> None:
        self.x1: int = x1
        self.y1: int = y1
        self.x2: int = x2
        self.y2: int = y2
        self.width: int = width
        self.color: tuple = color
        self.screen: pygame.Surface | None = screen

    def draw(self, screen: pygame.Surface = None) -> None:
        if screen is None:
            if self.screen is None:
                raise ValueError("screen is None")
            screen = self.screen
        pygame.draw.line(screen, self.color, (self.x1, self.y1), (self.x2, self.y2), self.width)
