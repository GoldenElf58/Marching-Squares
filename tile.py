from math import floor, ceil

import pygame

from constants import EDGE_TABLE
from rectangle import Rectangle


class Tile:
    def __init__(self, corners: list[float], row: int, column: int, screen: pygame.Surface,
                 x, y, side_length, font: pygame.font.Font = None, width=2, color=(255, 255, 255)) -> None:
        self.corners: list[float] = corners
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
                                         screen=self.screen, width=self.width / 2)

    def set_corners(self, corners: int) -> None:
        self.corners = corners

    def get_corners(self) -> list[float]:
        return self.corners

    def draw(self) -> None:
        # self.rect.draw()

        int_corners = sum([ceil(x) * 2 ** i for i, x in enumerate(self.corners)])
        # text = str(int_corners)
        # coordinates = (self.x + self.side_length / 2, self.y + self.side_length / 2)
        # self.screen.blit(self.font.render(text, True, (0, 100, 200)), coordinates)

        for edges in EDGE_TABLE[int_corners]:
            x1, y1 = self.get_edge_point_location(edges[0])
            x2, y2 = self.get_edge_point_location(edges[1])
            pygame.draw.line(self.screen, self.color, (x1, y1), (x2, y2), self.width)

        for corner in range(4):
            if 2 ** corner & int_corners == 1:
                self.screen.blit(self.font.render(str(round(self.corners[corner], 1)), True, (0, 100, 200)),
                                 self.get_corner_location(corner))
                # pygame.draw.circle(self.screen, (255, 0, 0), self.get_corner_location(corner), self.width * 2)

    def get_edge_point_location(self, edge: int) -> tuple[int, int]:
        match edge:
            case 0:
                x = self.x + self.side_length * Tile.calculate_multiplier(self.corners[0], self.corners[1])
                y = self.y
            case 1:
                x = self.x + self.side_length
                y = self.y + self.side_length * Tile.calculate_multiplier(self.corners[1], self.corners[2])
            case 2:
                x = self.x + self.side_length * Tile.calculate_multiplier(self.corners[3], self.corners[2])
                y = self.y + self.side_length
            case 3:
                x = self.x
                y = self.y + self.side_length * Tile.calculate_multiplier(self.corners[0], self.corners[3])
            case _:
                raise ValueError("Invalid edge")

        return x, y

    @staticmethod
    def calculate_multiplier(a, b) -> float:
        c = abs(b - a - 1)
        return c - floor(c)

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
