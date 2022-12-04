import pygame
from components import Button,draw_text
from SETTINGS import MAIN_MENU_FONT,MAIN_MENU_FONT_LOGO

bg = pygame.image.load("Agnosia_assets/Agnosia_background_main_menu.png")


def MenuScene(screen,current_scene,clock,all_scenes):
    def change(s):
        current_scene[0] = s
        return

    btn1 = Button(360, 80, None, (0,0,0), screen,MAIN_MENU_FONT)
    btn2 = Button(275, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)
    btn3 = Button(230, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)
    btn4 = Button(145, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)

    while current_scene[0]==MenuScene:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                current_scene[0] = None
                return

            if e.type == pygame.KEYDOWN and e.key == pygame.K_m:
                current_scene[0] = all_scenes["Map"]
                return

        screen.fill((255,0,0))
        screen.blit(bg, (0,0))
        draw_text(screen,"Agnosia",630,247,MAIN_MENU_FONT_LOGO,color=(0,0,0))
        btn1.draw(764, 540, "New game", lambda :change(all_scenes["Map"]))
        btn2.draw(808, 667, "Tutorial", lambda: change(None))
        btn3.draw(808, 796, "Option", lambda: change(all_scenes["Options"]))
        btn4.draw(877, 925, "Exit", lambda: change(None))
        pygame.display.flip()
        clock.tick(30)