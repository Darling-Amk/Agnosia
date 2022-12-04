import pygame
from SETTINGS import MAIN_MENU_FONT,MAIN_MENU_FONT_LOGO
from components import Button,draw_text

bg = pygame.image.load("Agnosia_assets/Agnosia_background_main_menu.png")


def OptionsScene(screen,current_scene,clock,all_scenes):
    def change(s):
        current_scene[0] = s
    # for variables
    btn = Button(190, 80, None, (0, 0, 0), screen, font=MAIN_MENU_FONT)
    while current_scene[0]==OptionsScene:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                current_scene[0] = None
                return
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                current_scene[0] = None
                return

        screen.fill((255,155,0))
        screen.blit(bg, (0, 0))
        #For drawing
        draw_text(screen, "Agnosia", 630, 247, MAIN_MENU_FONT_LOGO, color=(0, 0, 0))

        btn.draw(877, 925, "Back", lambda: change(all_scenes["Menu"]))
        pygame.display.flip()
        clock.tick(30)