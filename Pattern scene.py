import pygame
from SETTINGS import MAIN_MENU_FONT

bg = pygame.image.load("Agnosia_assets/Agnosia_background_battleground.png")


def T(screen,current_scene,clock,all_scenes):
    def change(s):
        current_scene[0] = s
    # for variables

    while current_scene[0]==T:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                current_scene[0] = None
                return

        screen.fill((255,155,0))
        screen.blit(bg, (0, 0))
        #For drawing

        pygame.display.flip()
        clock.tick(30)