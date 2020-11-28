from setting import *
import pygame as pg

class Card(pg.sprite.Sprite):
    def __init__(self, color, bg_color, shape):
        pg.sprite.Sprite.__init__(self)
        self.color = color
        self.bg_color = bg_color
        self.shape = shape 

    def __repr__(self):
        return f"{self.color} {self.bg_color} {self.shape}" 

    def initialize(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index 
        self.image = pg.Surface((x, y))
        self.image = pg.transform.scale(self.image, (H_SIZE, V_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)