from setting import *
import pygame as pg

class Button(pg.sprite.Sprite):
    def __init__(self, *args):
        screen, font_name, text, x, y = args
        pg.sprite.Sprite.__init__(self)
        self.screen = screen 
        self.font_name = font_name 
        self.text = text    
        self.x = x 
        self.y = y    

        self.image = pg.Surface((self.x, self.y))
        self.image = pg.transform.scale(self.image, (TEXT_POS_X, TEXT_POS_Y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def draw(self):
        pg.draw.rect(self.screen, YELLOW, (self.x, self.y, TEXT_POS_X, TEXT_POS_Y))
        
        font = pg.font.Font(self.font_name, TEXT_SIZE)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect()
        #text_rect.topleft = (self.x, self.y)
        text_rect.centerx = self.x+TEXT_POS_X/2
        text_rect.centery = self.y+TEXT_POS_Y/2
        self.screen.blit(text_surface, text_rect)
        return