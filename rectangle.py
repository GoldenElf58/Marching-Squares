import pygame

from shape import Shape


class Rectangle(Shape):
    def __init__(self, x1: int, y1: int, x2: int, y2: int, color: tuple = (255, 0, 0), screen=None, width=3) -> None:
        self.x1: int = int(x1)
        self.y1: int = int(y1)
        self.x2: int = int(x2)
        self.y2: int = int(y2)
        self.color: tuple = color
        self.screen: pygame.Surface | None = screen
        self.width: int = int(width)

    def draw(self, screen: pygame.Surface | None = None) -> None:
        if screen is None:
            if self.screen is None:
                raise ValueError("screen is None")
            screen = self.screen
        pygame.draw.rect(screen, self.color, (self.x1, self.y1, self.x2, self.y2), width=self.width)
