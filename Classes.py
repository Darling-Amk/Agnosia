from abc import ABC, abstractmethod
import pygame

class Scene:
    def __init__(self,screen,name,change,bg_image="Agnosia_assets/Agnosia_background_main_menu.png"):
        self.bg = pygame.image.load(bg_image)
        self.change = change
        self.name = name
        self.screen = screen
    def draw(self,state):
        pass

    @staticmethod
    def draw_text(surface, text, x, y, font, color=(255, 255, 255)):
        surface.blit(font.render(f'{text}', True, color), (x, y))




class Card(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def getPrice(self):
        pass

    @abstractmethod
    def canBeUpgraded(self):
        pass