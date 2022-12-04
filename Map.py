import pygame
from components import Button
from SETTINGS import MAIN_MENU_FONT

from Classes import  Scene

class MapScene(Scene):
    def __init__(self,screen,name,change,bg_image):
        super().__init__(screen,name,change,bg_image)
        self.btn = Button(200, 42, (0, 255, 0), (0, 0, 0), screen,font =MAIN_MENU_FONT )

    def draw(self,state):
        self.screen.fill((255, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        # For drawing
        self.btn.draw(830, 1000, "Back", lambda: self.change("Menu"))
        pygame.display.flip()