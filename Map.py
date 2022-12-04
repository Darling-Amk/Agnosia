import pygame
from components import Button
from SETTINGS import MAIN_MENU_FONT

bg = pygame.image.load("Agnosia_assets/Agnosia_background_map.png")

def MapScene(screen,current_scene,clock,all_scenes):
    def change(s):
        current_scene[0] = s
        return

    btn = Button(200, 42, (0, 255, 0), (0, 0, 0), screen,font =MAIN_MENU_FONT )
    while current_scene[0]==MapScene:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                current_scene[0] = None
                return

            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                current_scene[0] = None
                return

        screen.fill((255,155,0))
        screen.blit(bg, (0, 0))



        btn.draw(830, 1000, "Back", lambda: change(all_scenes["Menu"]))
        pygame.display.flip()
        clock.tick(30)