from SETTINGS import *
from UserInterfaceClass import UserInterface

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

UI = UserInterface(screen)
play = True

while play:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            play = False
    scene = UI.draw()

    if scene == "battle":
        pass
    if scene=="None":
        play = False
    clock.tick(30)



pygame.quit()



