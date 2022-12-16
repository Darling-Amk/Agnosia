import sys
sys.path.insert(1,'Scenes')

import Cards
from Scenes.Map import  MapScene
from  Options import OptionsScene
from  Menu import MainMenuScene
from  Battle import BattleScene
from Camp import CampScene, CampUpgradeScene
from Chest import ChestScene, RewardScene
from Victory import VictoryScene


class UserInterface:
    def __init__(self,screen, player):
        self.player = player
        self.restart = set()
        self.screen = screen
        self.scenes = {}
        self.current_scene = "Menu"
        self.CreateMainMenu()
        self.CreateOptions()
        self.CreateMap()
        self.CreateBattle()
        self.CreateChest()
        self.CreateCamp()
        self.CreateCampUpgrade()
        self.CreateReward()
        self.CreateVictory()

    def changeScene(self,scene, monster = None):
        if scene[0:2]=="Re":
            scene = scene.replace('Re',"")

            for u in self.restart:
                u()
            self.CreateScene(scene)
        if scene=="Battle":
            self.mobs = monster
        if scene == "Award":
            self.mobs = Cards.getThreeCards()
        self.current_scene = scene

    def draw(self,state=None, mobs = None):
        if self.current_scene=="Battle" or self.current_scene=="Award":
            self.scenes[self.current_scene].draw(state, self.mobs)
        elif self.current_scene!="None":
            self.scenes[self.current_scene].draw(state)
        return self.current_scene



    def CreateScene(self,name):
        if name=="Menu":
            self.CreateMainMenu()
        if name=="Map":
            self.CreateMap()
        if name=="Options":
            self.CreateBattle()
        if name=="Menu":
            self.CreateOptions()

    def CreateMainMenu(self):
        self.scenes['Menu'] = MainMenuScene(screen=self.screen ,name="Menu",
                                            bg_image="Agnosia_assets/Agnosia_background_main_menu.png",change = self.changeScene)

    def CreateOptions(self):
        self.scenes['Options'] = OptionsScene(screen=self.screen ,name="Options",
                                              bg_image="Agnosia_assets/Agnosia_background_main_menu.png",change = self.changeScene)

    def CreateMap(self):
        self.scenes['Map'] = MapScene(screen=self.screen ,name="Map",
                                      bg_image="Agnosia_assets/Agnosia_background_map.png",change = self.changeScene, player=self.player)

    def CreateBattle(self):
        self.scenes['Battle'] = BattleScene(screen=self.screen, name="Battle",
                                      bg_image="Agnosia_assets/Agnosia_background_battleground2.png", change=self.changeScene)

    def CreateChest(self):
        self.scenes['Chest'] = ChestScene(screen=self.screen, name="Chest",
                                      bg_image="Agnosia_assets/Agnosia_background_chest.png", change=self.changeScene)

    def CreateCamp(self):
        self.scenes['Camp'] = CampScene(screen=self.screen, name="Camp",
                                      bg_image="Agnosia_assets/Agnosia_background_camp.png", change=self.changeScene)
    def CreateCampUpgrade(self):
        self.scenes['CampUpgrade'] = CampUpgradeScene(screen=self.screen, name="CampUpgrade",
                                      bg_image="Agnosia_assets/Agnosia_background_camp.png", change=self.changeScene)
    def CreateReward(self):
        self.scenes['Award'] = RewardScene(screen=self.screen, name="Award",
                                      bg_image="Agnosia_assets/Agnosia_background_rewards.png", change=self.changeScene)

    def CreateVictory(self):
        self.scenes['Victory'] = VictoryScene(screen=self.screen, name="Victory",
                                           bg_image="Agnosia_assets/Agnosia_qr.png",
                                           change=self.changeScene)