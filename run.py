from manager import *
import pygame as pg

def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Set NoSet")
    font_name = pg.font.match_font('arial')

    manager = Manager(screen, font_name)
    manager.play()
    return

if __name__=="__main__":
    main()