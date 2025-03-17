import pygame

from constants import EDGE_TABLE


class Tile:
    def __init__(self, corners: list[float], row: int, column: int, screen: pygame.Surface, x, y, *, width, height,
                 font: pygame.font.Font | None = None, stroke=2, color=(255, 255, 255), smooth=True, debug=False) -> None:
        self.corners: list[float] = corners
        self.row: int = row
        self.column: int = column
        self.screen: pygame.Surface = screen
        self.font: pygame.font.Font | None = font
        self.x: int = x
        self.y: int = y
        self.width: int = width  # x length
        self.height: int = height  # y length
        self.color: tuple[int, int, int] = color
        self.stroke: int = stroke
        self.smooth: bool = smooth
        self.debug: bool = debug
        self.show_gradient: bool = False
    
    def draw(self) -> None:
        if self.show_gradient:
            self.disp_gradient()
            return
        
        isovalue = 0.0  # Value to draw boundary line
        int_corners = self.calculate_int_corners()
        
        if self.debug:
            self.show_debug()

        for edges in EDGE_TABLE[int_corners]:
            if self.smooth:
                y1, x1 = self.get_edge_point_location(edges[0], isovalue)
                y2, x2 = self.get_edge_point_location(edges[1], isovalue)
            else:
                y1, x1 = self.get_edge_midpoint(edges[0])
                y2, x2 = self.get_edge_midpoint(edges[1])
            pygame.draw.line(self.screen, self.color, (x1, y1), (x2, y2), self.stroke)
    
    def calculate_int_corners(self) -> int:
        int_corners = 0
        for i, value in enumerate(self.corners):
            if value >= 0:
                int_corners |= 1 << i
        return int_corners
    
    def disp_gradient(self):
        y, x = self.get_corner_location(0)
        c = max(0, int(self.corners[0] * 255))
        pygame.draw.circle(self.screen, (c, c, c), (x, y), 7)
        # coords = (x - self.width, y - self.height, x + self.width, y + self.height)
        # pygame.draw.rect(self.screen, (c, c, c), (coords, 0)

    def show_debug(self) -> None:
        pygame.draw.rect(self.screen, (255, 10, 10), (self.x, self.y, self.x + self.width, self.y + self.height), 1)
        # coords = (self.x + self.width // 2, self.y + self.height // 2)
        # self.screen.blit(self.font.render(f"{int_corners}", True, (255, 255, 255)), coords)

    def get_edge_point_location(self, edge: int, isovalue: float = 0.0) -> tuple[float, float]:
        """
        Get the coordinates of a point on a tile edge, given its edge number.

        Args:
            edge (int): The edge number. 0 is the top, 1 is the right, 2 is the bottom, and 3 is the left.
            isovalue (float, optional): The value to find in the range [0.0, 1.0]. Defaults to 0.0.

        Returns:
            tuple[float, float]: The coordinates of the point on the edge.

        Raises:
            ValueError: If edge is not in [0, 1, 2, 3].
        """
        match edge:
            case 0:
                mu: float = Tile.calculate_multiplier(self.corners[0], self.corners[1], isovalue)
                x: float = self.x + self.width * mu
                y: float = self.y
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
        """
        Calculate a multiplier to move from `a` to `b` such that the value at the
        multiplier location is equal to `isovalue`.

        Args:
            a (float): The starting value.
            b (float): The ending value.
            isovalue (float, optional): The value to find in the range [a, b].
                Defaults to 0.0.

        Returns:
            float: A multiplier in the range [0.0, 1.0] such that
                `a + (b - a) * mu == isovalue`.
        """
        delta = b - a
        if delta == 0:
            return 0.5
        mu = (isovalue - a) / delta
        mu = max(0.0, min(1.0, mu))
        return mu
    
    def get_corner_location(self, corner: int) -> tuple[int, int]:
        """
        Get the coordinates of a corner of the tile.

        Args:
            corner (int): The corner number. 0 is the top-left, 1 is the top-right,
                2 is the bottom-right, and 3 is the bottom-left.

        Returns:
            tuple[int, int]: The coordinates of the corner.

        Raises:
            ValueError: If corner is not in [0, 1, 2, 3].
        """
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
    
    def get_edge_midpoint(self, edge: int) -> tuple[float, float]:
        """
        Get the coordinates of the midpoint of a tile edge.

        Args:
            edge (int): The edge number. 0 is the top, 1 is the right, 2 is the bottom, and 3 is the left.

        Returns:
            tuple[int, int]: The coordinates of the midpoint of the edge.

        Raises:
            ValueError: If edge is not in [0, 1, 2, 3].
        """
        match edge:
            case 0:
                x: float = self.x + self.width / 2
                y: float = self.y
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
