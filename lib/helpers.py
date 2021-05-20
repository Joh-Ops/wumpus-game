"""
This module provides access to several useful constants and helper functions.
"""

import pygame

import config


class MultiplicableTuple(tuple):
    """A tuple, but when it is multiplied by an integer it multiplies all the items in it instead."""
    def __mul__(self, other):
        if isinstance(other, int):
            return MultiplicableTuple([item*other for item in self])
        else:
            raise TypeError(f"can't multiply sequence by non-int of type '{type(self).__name__}'")


class Direction:
    UP = MultiplicableTuple([0, -1])
    DOWN = MultiplicableTuple([0, 1])
    LEFT = MultiplicableTuple([-1, 0])
    RIGHT = MultiplicableTuple([1, 0])
    UP_DOWN_LEFT_RIGHT = [UP, DOWN, LEFT, RIGHT]


WINDOW_RECT = pygame.Rect(0, 0, config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
