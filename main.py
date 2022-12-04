from SETTINGS import *
import time
from Menu import  MenuScene
from Map import MapScene
from Options import OptionsScene
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
current_scene = [None]
all_scenes = {
    "Menu":MenuScene,
    "Map":MapScene,
    "Options":OptionsScene
}
current_scene[0] = MenuScene

while current_scene[0] is not None:
    current_scene[0](screen,current_scene,clock,all_scenes)
    time.sleep(.1)
    print("Изменилась сцена")

pygame.quit()



