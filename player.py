#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *

MOVE_SPEED = 2
WIDTH = 32
HEIGHT = 32
COLOR = "#ff0000"

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.startX = x
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)

    def update(self, up, down, left, right):
        if up:
            self.yvel = -MOVE_SPEED

        if down:
            self.yvel = MOVE_SPEED

        if left:
            self.xvel = -MOVE_SPEED

        if right:
            self.xvel = MOVE_SPEED

        if not(up or down):
            self.yvel = 0

        if not(left or right):
            self.xvel = 0

        self.rect.y += self.yvel
        self.rect.x += self.xvel

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))
