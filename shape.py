from abc import abstractmethod

import pygame


class Shape:
    @abstractmethod
    def draw(self, screen: pygame.Surface | None = None) -> None: ...
