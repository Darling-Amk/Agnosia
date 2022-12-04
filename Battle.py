import pygame
from components import Button,draw_text
from SETTINGS import MAIN_MENU_FONT,MAIN_MENU_FONT_LOGO

from Classes import  Scene

class BattleScene(Scene):
    def __init__(self,screen,name,change,bg_image):
        super().__init__(screen,name,change,bg_image)


        self.btn4 = Button(145, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)

    def draw(self, state):
        self.screen.fill((255, 0, 0))
        self.screen.blit(self.bg, (0, 0))


        self.btn4.draw(877, 925, "Exit", lambda: self.change("None"))
        pygame.display.flip()

