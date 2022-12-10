from SETTINGS import *
from UserInterfaceClass import UserInterface
from  Classes import Player
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

player = Player()
player.artifacts = ["hui","pizda"]

UI = UserInterface(screen)
#UI.restart.add(player.restart) 
play = True

player.health = 15
while play:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            play = False
    scene = UI.draw(player)

    if scene=="None":
        play = False
    clock.tick(30)



pygame.quit()



