from setting import *
from _button import *
from _card import *

import pygame as pg
import numpy as np
import random

class Game:
    def __init__(self, screen, font_name):
        self.screen = screen
        self.font_name = font_name 
        self.cards = pg.sprite.Group() 
        self.buttons = pg.sprite.Group() 
        self.choices = []
        self.correct = []
        self.solution = []
        self.noset_clicked = False 
        return

    def generatePool(self):
        all_cards = [Card(COLORS[i], BG_COLORS[j], SHAPES[k]) for i in range(3) for j in range(3) for k in range(3)]
        cards = random.sample(all_cards, 9)

        count = 0
        for i in range(3):
            for j in range(3):
                card = cards[count]
                card.initialize(G_OFFSET_X + j*OFFSET, G_OFFSET_Y + i*OFFSET, count)
                self.cards.add(card)
                count += 1
        return 

    def generateButtons(self):
        self.buttons.add(Button(self.screen, self.font_name, RESET_NAME, RESET_POS[0], RESET_POS[1]))
        self.buttons.add(Button(self.screen, self.font_name, NOSET_NAME, NOSET_POS[0], NOSET_POS[1]))
        self.buttons.add(Button(self.screen, self.font_name, EXIT_NAME, EXIT_POS[0], EXIT_POS[1]))
        return

    def isDuplicateChoice(self):
        for cor in self.correct:
            count = 0
            for choice in self.choices:
                if choice in cor:
                    count += 1
            if count==3:
                return True
        return False

    def isValidChoice(self):
        if self.isDuplicateChoice():
            print(f'Duplicate choices : {self.choices}')
            return False

        for sol in self.solution:
            count = 0
            for choice in self.choices:
                if choice in sol:
                    count += 1
            if count==3:
                return True
        return False

    def solve(self):
        for i, card_1 in enumerate(self.cards):
            for j, card_2 in enumerate(self.cards):
                for k, card_3 in enumerate(self.cards):
                    if not (len(set([i,j,k]))==3 and i<j and j<k and i<k):
                        continue

                    score_1 = 0; score_2 = 0; penalty = 0

                    shape_group = set([card_1.shape, card_2.shape, card_3.shape]) 
                    color_group = set([card_1.color, card_2.color, card_3.color]) 
                    bg_color_group = set([card_1.bg_color, card_2.bg_color, card_3.bg_color]) 

                    groups = [shape_group, color_group, bg_color_group]
                    for group in groups:
                        if len(group)==1: score_1 += 1
                        elif len(group)==2: penalty += 1
                        elif len(group)==3: score_2 += 1

                    if (score_1 > 0 and penalty == 0) or score_2 == 3:
                        self.solution.append([i,j,k])
        return

    def draw(self, *args):
        message, _round, score, _time = args
        self.screen.fill(BLACK)
        
        pg.draw.rect(self.screen, (150,150,150), (G_OFFSET_X-int(H_SIZE/2), G_OFFSET_Y-int(V_SIZE/2), (H_SIZE+OFFSET)*2, (H_SIZE+OFFSET)*2))
        for card in self.cards:
            if card.index in self.choices:
                pg.draw.rect(self.screen, SELECT_COLOR, (card.x-SHRINKER, card.y-SHRINKER, H_SIZE+2*SHRINKER, V_SIZE+2*SHRINKER))

            pg.draw.rect(self.screen, CM[card.bg_color], (card.x, card.y, H_SIZE, V_SIZE))
            if card.shape == "rect":
                pg.draw.rect(self.screen, CM[card.color], (card.x+SHRINKER, card.y+SHRINKER, H_SIZE-2*SHRINKER, V_SIZE-2*SHRINKER))
            elif card.shape == "circle":
                pg.draw.circle(self.screen, CM[card.color], (card.x+int(H_SIZE/2), card.y+int(V_SIZE/2)), RADIUS)
            elif card.shape == "triangle":
                pg.draw.polygon(self.screen, CM[card.color], [(card.x+(H_SIZE/2), card.y+SHRINKER), (card.x+SHRINKER, card.y+V_SIZE-SHRINKER), (card.x+H_SIZE-SHRINKER, card.y+V_SIZE-SHRINKER)])

        if self.correct:
            pg.draw.rect(self.screen, (150,150,150), (G_MINI_OFFSET-MINI_H_SIZE, MINI_Y-MINI_V_SIZE, 4*len(self.correct)*MINI_H_SIZE+MINI_H_SIZE, 3*MINI_V_SIZE))
        for i, group in enumerate(self.correct):
            for j, index in enumerate(group):
                for k, c in enumerate(self.cards):
                    if k==index:
                        card = c 
                        break
                x = G_MINI_OFFSET+i*MINI_OFFSET+j*MINI_H_SIZE
                pg.draw.rect(self.screen, CM[card.bg_color], (x, MINI_Y, MINI_H_SIZE, MINI_V_SIZE))
                if card.shape == "rect": 
                    pg.draw.rect(self.screen, CM[card.color], (x+MINI_SHRINKER, MINI_Y+MINI_SHRINKER, MINI_H_SIZE-2*MINI_SHRINKER, MINI_V_SIZE-2*MINI_SHRINKER))
                elif card.shape == "circle":
                    pg.draw.circle(self.screen, CM[card.color], (x+int(MINI_H_SIZE/2), MINI_Y+int(MINI_V_SIZE/2)), MINI_RADIUS)
                elif card.shape == "triangle":
                    pg.draw.polygon(self.screen, CM[card.color], [(x+(MINI_H_SIZE/2), MINI_Y+MINI_SHRINKER), (x+MINI_SHRINKER, MINI_Y+MINI_V_SIZE-MINI_SHRINKER), (x+MINI_H_SIZE-MINI_SHRINKER, MINI_Y+MINI_V_SIZE-MINI_SHRINKER)])

        for button in self.buttons:
            button.draw()

        self.draw_text(message, MESSAGE_POS)
        self.draw_text(f"SCORE : {str(score)}", SCORE_POS)
        self.draw_text(f"ROUND : {str(_round)}", ROUND_POS)
        self.draw_text(f"Time Elapsed : {str(_time)}", TIME_POS)
        return

    def draw_text(self, text, pos):
        x, y = pos
        font = pg.font.Font(self.font_name, TEXT_SIZE)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        self.screen.blit(text_surface, text_rect)
        return