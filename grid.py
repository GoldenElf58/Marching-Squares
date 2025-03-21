import pygame
from noise import pnoise3  # type: ignore

# from my_noise import perlin, permutation
from tile import Tile


class Grid:
    def __init__(self, columns: int, rows: int, screen: pygame.Surface, *, font, smooth=True, scale=10, debug=False,
                 show_gradient=False) -> None:
        self.columns: int = columns
        self.rows: int = rows
        self.screen: pygame.Surface = screen
        self.font = font
        self.height: int = screen.get_height()
        self.width: int = screen.get_width()
        self.scale: int = scale
        self.debug: bool = debug
        self.show_gradient: bool = show_gradient

        self.grid: list[list[Tile]] = []
        self.create_initialized_grid(smooth=smooth)
        self.set_corners(0)
    
    def set_smooth(self, smooth: bool) -> None:
        for row in self.grid:
            for tile in row:
                tile.smooth = smooth
    
    def set_debug(self, debug: bool) -> None:
        for row in self.grid:
            for tile in row:
                tile.debug = debug
    
    def set_show_gradient(self, show_gradient: bool) -> None:
        for row in self.grid:
            for tile in row:
                tile.show_gradient = show_gradient
    
    def set_scale(self, scale: int) -> None:
        self.scale = scale
    
    def draw(self) -> None:
        for row in self.grid:
            for tile in row:
                tile.draw()
    
    def set_corners(self, z) -> None:
        for i in range(self.rows + 1):
            for j in range(self.columns + 1):
                divisor = min(self.columns, self.rows)
                x = i / divisor * self.scale
                y = j / divisor * self.scale
                # val = perlin(x, y, z, permutation)
                val = pnoise3(x, y, z)
                if i < self.height and j < self.width:
                    self.grid[i][j].corners[0] = val
                if i > 0 and j < self.width:
                    self.grid[i - 1][j].corners[1] = val
                if i < self.height and j > 0:
                    self.grid[i][j - 1].corners[3] = val
                if i > 0 and j > 0:
                    self.grid[i - 1][j - 1].corners[2] = val
    
    def create_initialized_grid(self, smooth=True) -> None:
        self.grid = []
        for i in range(self.rows + 1):
            self.grid.append([])
            for j in range(self.columns + 1):
                self.grid[i].append(Tile([0, 0, 0, 0], i, j, self.screen, i * self.width / self.columns,
                                       j * self.height / self.rows, width=self.width / self.columns,
                                       height=self.height / self.rows, font=self.font, smooth=smooth, debug=self.debug,))
