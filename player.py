#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *

MOVE_SPEED = 2
WIDTH = 32
HEIGHT = 40
COLOR = "#888888"

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
        self.image.set_colorkey(Color(COLOR))

    def update(self, up, down, left, right):
        if up:
            self.yvel = -MOVE_SPEED

        if down:
            self.yvel = MOVE_SPEED

        if left:
            self.xvel = -MOVE_SPEED

        if right:
            self.xvel = MOVE_SPEED

        self.rect.y += self.yvel
        self.rect.x += self.xvel
            
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))
    
'''
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):

                if xvel > 0 :
                    self.rect.right = p.rect.left

                if xvel < 0:
                    self.rect.left = p.rect.right

                if yvel > 0:
                    self.rect.bottom = p.rect.top

                if yvel < 0:
                    self.rect.top = p.rect.bottom
'''