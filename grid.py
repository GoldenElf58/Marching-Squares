from math import ceil

import pygame
from noise import pnoise3

from tile import Tile


class Grid:
    def __init__(self, columns: int, rows: int, screen: pygame.Surface, *, font) -> None:
        self.columns: int = columns
        self.rows: int = rows
        self.screen: pygame.Surface = screen
        self.font = font
        self.length: int = screen.get_width()
        self.width: int = screen.get_height()

        self.grid: list[list[Tile]] = self.create_empty_grid()
        self.initialize_grid()
        self.set_corners(0)

    def draw(self) -> None:
        for row in self.grid:
            for tile in row:
                tile.draw()

    def set_corners(self, z) -> None:
        for i in range(self.length + 1):
            for j in range(self.width + 1):
                x = i / self.width / self.columns * 6400
                y = j / self.length / self.rows * 6400
                val = pnoise3(x, y, z)
                # val = round(perlin(x, y, permutation))
                if i < self.length and j < self.width:
                    self.grid[i][j].corners[0] = val
                if i > 0 and j < self.width:
                    self.grid[i - 1][j].corners[1] = val
                if i < self.length and j > 0:
                    self.grid[i][j - 1].corners[3] = val
                if i > 0 and j > 0:
                    self.grid[i - 1][j - 1].corners[2] = val

    def create_empty_grid(self) -> list[list[Tile]]:
        grid = []
        for i in range(self.length):
            grid.append([])
            for j in range(self.width):
                grid[i].append(None)
        return grid

    def initialize_grid(self) -> None:
        for i, row in enumerate(self.grid):
            for j, tile in enumerate(row):
                self.grid[i][j] = Tile([0, 0, 0, 0], i, j, self.screen, i * self.width / self.columns,
                                       j * self.length / self.rows,
                                       self.width / self.columns, font=self.font)
