import pygame

from line import Line
from tile import Tile
from shape import Shape


class Grid:
    def __init__(self, length: int, width: int) -> None:
        self.length: int = length
        self.width: int = width
        self.grid: list[list[Tile]] = self.create_blank_grid()
        self.initialize_grid()

    def create_blank_grid(self) -> list[list[Tile]]:
        grid = []
        for i in range(self.length):
            grid.append([])
            for j in range(self.width):
                grid[i].append(None)
        return grid

    def initialize_grid(self) -> None:
        for row in self.grid:
            for tile in row:
                pass