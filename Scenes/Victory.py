import pygame
from SETTINGS import MAIN_MENU_FONT,MAIN_MENU_FONT_LOGO
from components import Button

from Classes import  Scene


class VictoryScene(Scene):
    def __init__(self,screen,name,change,bg_image):
        super().__init__(screen,name,change,bg_image)
        self.btn = Button(190, 80, None, (0, 0, 0), screen, font=MAIN_MENU_FONT)

    def draw(self,state):
        self.screen.fill((255, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        # For drawing
        Scene.draw_text(self.screen, "Agnosia", 630, 247, MAIN_MENU_FONT_LOGO, color=(0, 0, 0))
        self.btn.draw(877, 925, "Back", lambda: self.change("Menu"))
        pygame.display.flip()