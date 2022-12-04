import pygame
from components import Button,draw_text
from SETTINGS import MAIN_MENU_FONT,MAIN_MENU_FONT_LOGO

from Classes import  Scene

class MainMenuScene(Scene):
    def __init__(self,screen,name,change,bg_image):
        super().__init__(screen,name,change,bg_image)

        self.btn1 = Button(360, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)
        self.btn2 = Button(275, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)
        self.btn3 = Button(230, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)
        self.btn4 = Button(145, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)

    def draw(self,state):
        self.screen.fill((255, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        Scene.draw_text(self.screen, "Agnosia", 630, 247, MAIN_MENU_FONT_LOGO, color=(0, 0, 0))
        self.btn1.draw(764, 540, "New game", lambda: self.change("Map"))
        self.btn2.draw(808, 667, "Tutorial", lambda: self.change("None"))
        self.btn3.draw(808, 796, "Option", lambda: self.change("Options"))
        self.btn4.draw(877, 925, "Exit", lambda: self.change("None"))
        print("Menu draw!")
        pygame.display.flip()

