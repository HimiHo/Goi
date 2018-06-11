#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame import *
from player import *

WIN_WIDTH = 800
WIN_HEIGHT = 640
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

def main():
    
    pygame.init()
    hero = Player(55, 55)
    entities = pygame.sprite.Group()
    platforms = []
    entities.add(hero)
    level = [
       "-------------------------",
       "-                       -",
       "-                       -",
       "-                       -",
       "-            --         -",
       "-                       -",
       "--                      -",
       "-                       -",
       "-                   --- -",
       "-                       -",
       "-                       -",
       "-      ---              -",
       "-                       -",
       "-   -----------        -",
       "-                       -",
       "-                -      -",
       "-                   --  -",
       "-                       -",
       "-                       -",
       "-------------------------"]
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT),
                                     HWSURFACE|DOUBLEBUF|RESIZABLE)
    pygame.display.set_caption("Goi")
    up = down = left = right = False
    clock = pygame.time.Clock()
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color("#964B00"))

    while 1:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit("QUIT")
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit("QUIT")
            
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
                    
            
            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
        
        x=y=0
        for row in level:
            for col in row:
                if col == "-":
                    pf = Surface((PLATFORM_WIDTH,PLATFORM_HEIGHT))
                    pf.fill(Color(PLATFORM_COLOR)) 
                    screen.blit(pf,(x,y))  
                x += PLATFORM_WIDTH
            y += PLATFORM_HEIGHT
            x = 0

        screen.blit(bg, (0,0))
        hero.draw(screen)
        hero.update(up, down, left, right)
        pygame.display.update()
    
if __name__ == "__main__":
    main()
