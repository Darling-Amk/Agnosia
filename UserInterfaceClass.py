from components import  Button
from  SETTINGS import  MAIN_MENU_FONT,MAIN_MENU_FONT_LOGO
import pygame

class Scene:
    def __init__(self,screen,name,change,bg_image="Agnosia_assets/Agnosia_background_main_menu.png"):
        self.bg = pygame.image.load(bg_image)
        self.change = change
        self.name = name
        self.screen = screen
    def draw(self):
        pass

    @staticmethod
    def draw_text(surface, text, x, y, font, color=(255, 255, 255)):
        surface.blit(font.render(f'{text}', True, color), (x, y))

class MainMenu(Scene):
    def __init__(self,screen,name,change,bg_image):
        super().__init__(screen,name,change,bg_image)

        self.btn1 = Button(360, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)
        self.btn2 = Button(275, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)
        self.btn3 = Button(230, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)
        self.btn4 = Button(145, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)

    def draw(self):
        self.screen.fill((255, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        Scene.draw_text(self.screen, "Agnosia", 630, 247, MAIN_MENU_FONT_LOGO, color=(0, 0, 0))
        self.btn1.draw(764, 540, "New game", lambda: self.change("Map"))
        self.btn2.draw(808, 667, "Tutorial", lambda: self.change("None"))
        self.btn3.draw(808, 796, "Option", lambda: self.change("Options"))
        self.btn4.draw(877, 925, "Exit", lambda: self.change("None"))
        print("Menu draw!")
        pygame.display.flip()

class Options(Scene):
    def __init__(self,screen,name,change,bg_image):
        super().__init__(screen,name,change,bg_image)
        self.btn = Button(190, 80, None, (0, 0, 0), screen, font=MAIN_MENU_FONT)

    def draw(self):
        self.screen.fill((255, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        # For drawing
        Scene.draw_text(self.screen, "Agnosia", 630, 247, MAIN_MENU_FONT_LOGO, color=(0, 0, 0))
        self.btn.draw(877, 925, "Back", lambda: self.change("Menu"))
        pygame.display.flip()


class UserInterface:
    def __init__(self,screen):
        self.screen = screen
        self.scenes = {"None":False}
        self.current_scene = "Menu"
        self.CreateMainMenu()
        self.CreateOptions()

    def change(self,scene):
        self.current_scene = scene

    def draw(self,state={}):
        if self.current_scene:
            print(self.current_scene)
            self.scenes[self.current_scene].draw()

        return bool(self.current_scene)

    def CreateMainMenu(self):
        self.scenes['Menu'] = MainMenu(
            screen=self.screen ,
            name="Menu",
            bg_image="Agnosia_assets/Agnosia_background_main_menu.png",
            change = self.change
        )
    def CreateOptions(self):
        self.scenes['Options'] = Options(
            screen=self.screen ,
            name="Options",
            bg_image="Agnosia_assets/Agnosia_background_main_menu.png",
            change = self.change
        )

