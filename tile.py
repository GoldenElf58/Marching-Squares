import pygame

from line import Line
from lookup_tables import EDGE_TABLE
from rectangle import Rectangle


class Tile:
    def __init__(self, corners: int, row: int, column: int, screen: pygame.Surface,
                 x, y, side_length, font: pygame.font.Font = None, width=3, color=(255, 255, 255)) -> None:
        self.corners: int = corners
        self.row: int = row
        self.column: int = column
        self.screen: pygame.Surface = screen
        self.font: pygame.font.Font = font
        self.x: int = x
        self.y: int = y
        self.side_length: int = side_length
        self.color: tuple[int, int, int] = color
        self.width: int = width
        self.rect: Rectangle = Rectangle(self.x, self.y, self.side_length, self.side_length, color=self.color,
                                         screen=self.screen, width=self.width)

    def set_corners(self, corners: int) -> None:
        self.corners = corners

    def draw(self) -> None:
        self.rect.draw()
        # self.screen.blit(self.font.render(self.corners, True, (0, 100, 200)))

        for edges in EDGE_TABLE[self.corners]:
            x1, y1 = self.get_edge_midpoint(edges[0])
            x2, y2 = self.get_edge_midpoint(edges[1])
            line = Line(x1, y1, x2, y2, 1, screen=self.screen, color=self.color)
            line.draw()

        for corner in range(4):
            if 2 ** corner & self.corners == 1:
                pygame.draw.circle(self.screen, self.color, self.get_corner_location(corner), self.width * 3)

    def get_corner_location(self, corner: int) -> tuple[int, int]:
        match corner:
            case 0:
                x = self.x
                y = self.y
            case 1:
                x = self.x + self.side_length
                y = self.y
            case 2:
                x = self.x + self.side_length
                y = self.y + self.side_length
            case 3:
                x = self.x
                y = self.y + self.side_length
            case _:
                raise ValueError("Invalid corner")

        return x, y

    def get_edge_midpoint(self, edge: int) -> tuple[int, int]:
        match edge:
            case 0:
                x = self.x + self.side_length / 2
                y = self.y
            case 1:
                x = self.x + self.side_length
                y = self.y + self.side_length / 2
            case 2:
                x = self.x + self.side_length / 2
                y = self.y + self.side_length
            case 3:
                x = self.x
                y = self.y + self.side_length / 2
            case _:
                raise ValueError("Invalid edge")

        return x, y
