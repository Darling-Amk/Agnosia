import pygame
from components import Button,draw_text
from SETTINGS import MAIN_MENU_FONT,MAIN_MENU_FONT_LOGO

from Classes import  Scene

class CampScene(Scene):
    def __init__(self,screen,name,change,bg_image):
        super().__init__(screen,name,change,bg_image)
        self.restBtn = Button(360, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)
        self.upgradeBtn = Button(360, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)
        self.continueBtn = Button(360, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)

    def draw(self,player):
        self.screen.fill((255, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        self.restBtn.draw(1000, 540, "Rest", lambda: (player.rest() and False) or self.change("Map"))
        self.upgradeBtn.draw(1000, 667, "Upgrade", lambda: self.change("CampUpgrade"))
        pygame.display.flip()

class CampUpgradeScene(Scene):
    def __init__(self,screen,name,change,bg_image):
        super().__init__(screen,name,change,bg_image)
        self.continueBtn = Button(360, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)

    def draw(self,player):
        self.screen.fill((255, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        startX = 900
        startY = 125
        for a in player.deck:  # 1920 - длина области, ширина будет 200
            if startX > 1800:
                startX = 900
                startY += 250
            if a.canBeUpgraded():
                a.rect = a.image.get_rect(center=(startX, startY))
                self.screen.blit(a.image, a.rect)
            startX += 200
        pygame.display.flip()

