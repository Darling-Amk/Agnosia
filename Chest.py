import pygame

import SETTINGS
from components import Button,draw_text
from SETTINGS import MAIN_MENU_FONT,MAIN_MENU_FONT_LOGO

from Classes import  Scene

class ChestScene(Scene):
    def __init__(self,screen,name,change,bg_image):
        super().__init__(screen,name,change,bg_image)

        self.btn4 = Button(300, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)

    def draw(self,player):
        self.screen.fill((255, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        card = player.deck[len(player.deck)-1]
        card.rect = card.image.get_rect(center=(1920/2, 1080/2))
        self.screen.blit(card.image, card.rect)
        self.btn4.draw(877, 925, "Continue", lambda: self.change("Map"))
        pygame.display.flip()


class RewardScene(Scene):
    def __init__(self,screen,name,change,bg_image):
        super().__init__(screen,name,change,bg_image)

        self.btn4 = Button(160, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)

    def draw(self,player, cards):
        startX = SETTINGS.WIDTH/2 -200
        startY = SETTINGS.HEIGHT/2
        self.screen.fill((255, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        for a in cards:  # 1920 - длина области, ширина будет 200
            a.rect = a.image.get_rect(center=(startX, startY))
            startX += 200
            self.screen.blit(a.image, a.rect)
        self.btn4.draw(877, 925, "Skip", lambda: self.change("Map"))
        pygame.display.flip()
