from components import  Button
from  SETTINGS import  MAIN_MENU_FONT,MAIN_MENU_FONT_LOGO
import pygame

class Scene:
    def __init__(self,screen,name,bg_image=""):
        self.bg = pygame.image.load("Agnosia_assets/Agnosia_background_main_menu.png")
        self.name = name
        self.screen = screen
    def draw(self):
        pass

class MainMenu(Scene):

    def __init__(self,screen,name,bg_image=""):
        super. __init__(screen,name,bg_image)

        self.btn1 = Button(360, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)
        self.btn2 = Button(275, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)
        self.btn3 = Button(230, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)
        self.btn4 = Button(145, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)

    def draw(self):
        self.screen.fill((255, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        draw_text(self.screen, "Agnosia", 630, 247, MAIN_MENU_FONT_LOGO, color=(0, 0, 0))
        self.btn1.draw(764, 540, "New game", lambda: change(all_scenes["Map"]))
        self.btn2.draw(808, 667, "Tutorial", lambda: change(None))
        self.btn3.draw(808, 796, "Option", lambda: change(all_scenes["Options"]))
        self.btn4.draw(877, 925, "Exit", lambda: change(None))



class UserInterface:
    def __init__(self,screen):
        self.screen = screen
        self.scenes = {}
        self.current_scene = None

    def draw(self,state):
        self.scenes[self.current_scene].draw()

    def CreateMainMenu(self):
        self.scenes['Menu'] = Scene("Menu")

    def drawMainMenu(self):
