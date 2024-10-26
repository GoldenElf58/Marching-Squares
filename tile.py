from math import ceil
# from random import random

import matplotlib.pyplot as plt
import pygame

from constants import EDGE_TABLE
# from rectangle import Rectangle


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
        # self.rect: Rectangle = Rectangle(self.x, self.y, self.side_length, self.side_length, color=self.color,
        #                                  screen=self.screen, width=self.width / 2)

    def set_corners(self, corners: int) -> None:
        self.corners = corners

    def get_corners(self) -> list[float]:
        return self.corners

    def draw(self) -> None:
        isovalue = 0.0  # Set your isovalue
        int_corners = 0
        for i, value in enumerate(self.corners):
            if value >= isovalue:
                int_corners |= 1 << i

        for edges in EDGE_TABLE[int_corners]:
            x1, y1 = self.get_edge_point_location(edges[0])
            x2, y2 = self.get_edge_point_location(edges[1])
            plt.plot([x1, x2], [y1, y2], color="black")
            # pygame.draw.line(self.screen, self.color, (x1, y1), (x2, y2), self.width)

    def get_edge_point_location(self, edge: int) -> tuple[float, float]:
        isovalue = 0.0  # Use your actual isovalue

        match edge:
            case 0:
                mu = Tile.calculate_multiplier(self.corners[0], self.corners[1], isovalue)
                x = self.x + self.side_length * mu
                y = self.y
            case 1:
                mu = Tile.calculate_multiplier(self.corners[1], self.corners[2], isovalue)
                x = self.x + self.side_length
                y = self.y + self.side_length * mu
            case 2:
                mu = Tile.calculate_multiplier(self.corners[2], self.corners[3], isovalue)
                x = self.x + self.side_length * (1 - mu)
                y = self.y + self.side_length
            case 3:
                mu = Tile.calculate_multiplier(self.corners[3], self.corners[0], isovalue)
                x = self.x
                y = self.y + self.side_length * (1 - mu)
            case _:
                raise ValueError("Invalid edge")

        return x, y

    @staticmethod
    def calculate_multiplier(a: float, b: float, isovalue: float = 0.0) -> float:
        delta = b - a
        if delta == 0:
            return 0.5
        mu = (isovalue - a) / delta
        mu = max(0.0, min(1.0, mu))
        return mu

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
