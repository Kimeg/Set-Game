from setting import *
from _button import *
from _card import *
from _game import *

import pygame as pg
import time

class Manager:
    def __init__(self, screen, font_name):
        self.screen = screen 
        self.font_name = font_name 

        self.round = 1
        self.score = 0

        self.message = ""
        self.message_t0 = 0
        self.message_displayed = 0

        self.t0 = time.time()

        self.game = Game(screen, font_name)

    def update_status(self, _score=0):
        self.message_displayed = True 
        self.message_t0 = time.time()
        self.score += _score 
        return

    def _reset(self):
        self.game = Game(self.screen, self.font_name)
        self.game.generatePool()
        self.game.generateButtons()
        self.game.solve()
        return

    def reset_game(self):
        self._reset()
        self.round = 1
        self.score = 0
        self.t0 = time.time()
        return 

    def next_round(self):
        self._reset()
        self.score += 3 
        self.round += 1 
        return

    def play(self):
        self.reset_game()

        running = True
        while running:
            if self.message_displayed:
                if time.time()-self.message_t0>MESSAGE_DURATION:
                    self.message_displayed = False
                    self.message = ''

            for event in pg.event.get():
                if event.type==pg.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for card in self.game.cards:
                        if card.rect.collidepoint(x, y):
                            if card.index in self.game.choices:
                                self.game.choices.remove(card.index)
                                print(f'unselected {card.index}')
                            else:
                                self.game.choices.append(card.index)
                                print(f'selected {card.index}')

                    for button in self.game.buttons:
                        if button.rect.collidepoint(x, y):
                            if button.text==RESET_NAME:
                                self.reset_game()
                            elif button.text==NOSET_NAME:
                                self.game.noset_clicked = True 
                            elif button.text==EXIT_NAME:
                                running = False
                                break

                if event.type==pg.QUIT:
                    running = False
                    break

            if len(self.game.choices)==3:
                if self.game.isValidChoice():
                    self.game.correct.append([*self.game.choices])
                    self.message = f'correct choices : {self.game.choices}'
                    self.update_status(1)
                else:
                    self.message = f'Incorrect or duplicate choices : {self.game.choices}'
                    self.update_status(-1)
                self.game.choices = []

            if self.game.noset_clicked:
                if len(self.game.correct)==len(self.game.solution):
                    self.message = 'All combinations found!'
                    self.update_status()
                    self.next_round()
                else:
                    self.message = 'Not all combinations are found!'
                    self.game.noset_clicked = False
                    self.update_status(-1)

            self.game.draw(self.message, self.round, self.score, round(time.time()-self.t0, 2))
            pg.display.flip()
        pg.quit()
        return