
import pygame, sys, time
from pygame.locals import *
from pygame.sprite import *

pygame.init()

class Lamp(Sprite):
    def __init__(self, id, createX, createY, dimX, dimY, color, high_color, is_high=False):
        Sprite.__init__(self)
        self.id = id
        self.rect=pygame.Rect(createX, createY, dimX, dimY)
        self.simple_color=pygame.image.load(color)
        self.high_color=pygame.image.load(high_color)
        self.is_high = is_high

    def draw(self, surf):
        if self.is_high :
            surf.blit(self.high_color, self.rect)
        else:
            surf.blit(self.simple_color, self.rect)

    def make_highlight(self):
        self.is_high=True

    def make_simple(self):
        self.is_high=False





