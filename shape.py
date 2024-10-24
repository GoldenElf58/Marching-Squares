from abc import ABC, abstractmethod

import pygame


class Shape:
    @abstractmethod
    def draw(self, screen: pygame.Surface = None) -> None: ...
