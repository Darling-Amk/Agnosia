from SETTINGS import *
import time
from Menu import  MenuScene
from Map import MapScene
from Options import OptionsScene

from UserInterfaceClass import UserInterface

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
current_scene = [None]
all_scenes = {
    "Menu":MenuScene,
    "Map":MapScene,
    "Options":OptionsScene
}
current_scene[0] = MenuScene

UI = UserInterface(screen)
play = True
while play:
    play = UI.draw()
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            play = False



# while current_scene[0] is not None:
#     current_scene[0](screen,current_scene,clock,all_scenes)
#     time.sleep(.1)
#     print("Изменилась сцена")




pygame.quit()



