

class Tile:
    def __init__(self, corners: tuple[int, int, int, int], row: int, column: int) -> None:
        self.corners: tuple[int, int, int, int] = corners
        self.row: int = row
        self.column: int = column
