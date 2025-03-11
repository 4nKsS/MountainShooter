#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, Entity_SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= Entity_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
