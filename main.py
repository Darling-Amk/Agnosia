from SETTINGS import *
from UserInterfaceClass import UserInterface

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

UI = UserInterface(screen)
play = True
while play:
    play = UI.draw()
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            play = False


pygame.quit()



