import pygame
from components import Button,draw_text
from SETTINGS import MAIN_MENU_FONT,MAIN_MENU_FONT_LOGO

from Classes import  Scene

class CampScene(Scene):
    def __init__(self,screen,name,change,bg_image):
        super().__init__(screen,name,change,bg_image)
        self.flag = 0
        self.restBtn = Button(360, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)
        self.upgradeBtn = Button(360, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)
        self.continueBtn = Button(360, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)

    def draw(self,player):
        self.screen.fill((255, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        self.restBtn.draw(1000, 540, "Rest", lambda: (player.rest() and False) or self.change("Map"))
        self.upgradeBtn.draw(1000, 667, "Upgrade", lambda: self.change("Map"))
        pygame.display.flip()

