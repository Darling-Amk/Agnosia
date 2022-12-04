from Map import  MapScene
from  Options import OptionsScene
from  Menu import MainMenuScene

class UserInterface:
    def __init__(self,screen):
        self.screen = screen
        self.scenes = {"None":False}
        self.current_scene = "Menu"
        self.CreateMainMenu()
        self.CreateOptions()
        self.CreateMap()

    def changeScene(self,scene):
        self.current_scene = scene

    def draw(self,state={}):
        if self.current_scene:
            self.scenes[self.current_scene].draw(state)
        return bool(self.current_scene)

    def CreateMainMenu(self):
        self.scenes['Menu'] = MainMenuScene(screen=self.screen ,name="Menu",bg_image="Agnosia_assets/Agnosia_background_main_menu.png",change = self.changeScene)

    def CreateOptions(self):
        self.scenes['Options'] = OptionsScene(screen=self.screen ,name="Options",bg_image="Agnosia_assets/Agnosia_background_main_menu.png",change = self.changeScene)

    def CreateMap(self):
        self.scenes['Map'] = MapScene(screen=self.screen ,name="Map",bg_image="Agnosia_assets/Agnosia_background_map.png",change = self.changeScene)
