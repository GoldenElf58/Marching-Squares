import pygame

from constants import EDGE_TABLE


class Tile:
    def __init__(self, corners: list[float], row: int, column: int, screen: pygame.Surface, x, y, *, width, height,
                 font: pygame.font.Font = None, stroke=2, color=(255, 255, 255), smooth=True) -> None:
        self.corners: list[float] = corners
        self.row: int = row
        self.column: int = column
        self.screen: pygame.Surface = screen
        self.font: pygame.font.Font = font
        self.x: int = x
        self.y: int = y
        self.width: int = width  # x length
        self.height: int = height  # y length
        self.color: tuple[int, int, int] = color
        self.stroke: int = stroke
        self.smooth: bool = smooth
    
    def set_corners(self, corners: int) -> None:
        self.corners = corners
    
    def get_corners(self) -> list[float]:
        return self.corners
    
    def draw(self) -> None:
        isovalue = 0.0  # Value to draw boundary line
        int_corners = 0  # Corner locations in binary
        for i, value in enumerate(self.corners):
            if value >= isovalue:
                int_corners |= 1 << i
        
        for edges in EDGE_TABLE[int_corners]:
            if self.smooth:
                y1, x1 = self.get_edge_point_location(edges[0], isovalue)
                y2, x2 = self.get_edge_point_location(edges[1], isovalue)
            else:
                y1, x1 = self.get_edge_midpoint(edges[0])
                y2, x2 = self.get_edge_midpoint(edges[1])
            pygame.draw.line(self.screen, self.color, (x1, y1), (x2, y2), self.stroke)
    
    def get_edge_point_location(self, edge: int, isovalue: float = 0.0) -> tuple[float, float]:
        match edge:
            case 0:
                mu = Tile.calculate_multiplier(self.corners[0], self.corners[1], isovalue)
                x = self.x + self.width * mu
                y = self.y
            case 1:
                mu = Tile.calculate_multiplier(self.corners[1], self.corners[2], isovalue)
                x = self.x + self.width
                y = self.y + self.height * mu
            case 2:
                mu = Tile.calculate_multiplier(self.corners[2], self.corners[3], isovalue)
                x = self.x + self.width * (1 - mu)
                y = self.y + self.height
            case 3:
                mu = Tile.calculate_multiplier(self.corners[3], self.corners[0], isovalue)
                x = self.x
                y = self.y + self.height * (1 - mu)
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
                x = self.x + self.width
                y = self.y
            case 2:
                x = self.x + self.width
                y = self.y + self.height
            case 3:
                x = self.x
                y = self.y + self.height
            case _:
                raise ValueError("Invalid corner")
        
        return x, y
    
    def get_edge_midpoint(self, edge: int) -> tuple[int, int]:
        match edge:
            case 0:
                x = self.x + self.width / 2
                y = self.y
            case 1:
                x = self.x + self.width
                y = self.y + self.height / 2
            case 2:
                x = self.x + self.width / 2
                y = self.y + self.height
            case 3:
                x = self.x
                y = self.y + self.height / 2
            case _:
                raise ValueError("Invalid edge")
        
        return x, y
