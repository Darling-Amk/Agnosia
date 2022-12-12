import pygame
from components import Button, draw_text, ButtonImage
from SETTINGS import MAIN_MENU_FONT,MAIN_MENU_FONT_LOGO, WIDTH, HEIGHT, MAP_FONT

from Classes import  Scene

class BattleScene(Scene):
    def __init__(self,screen,name,change,bg_image):
        super().__init__(screen,name,change,bg_image)
        Art = pygame.image.load("Agnosia_assets/tmp_art.png")
        Art.set_colorkey((255, 255, 255))
        self.art = pygame.transform.scale(Art, (HEIGHT // 12, HEIGHT // 12))
        self.btnImg = ButtonImage(screen,HEIGHT//12,HEIGHT//12,
                                  image="Agnosia_assets/Agnosia_interface_settings.png",
                                  image_hover="Agnosia_assets/Agnosia_interface_settings_hover.png"
                                  )
        self.btn4 = Button(145, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)
        self.btn5 = Button(360, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)


    def draw(self, player, mobs):
        self.screen.fill((255, 0, 0))
        self.screen.blit(self.bg, (0, 0))

        # draw rect
        rect = pygame.Rect(0, 0, WIDTH, HEIGHT//12)
        pygame.draw.rect(self.screen, (27,27,27), (0, 0, WIDTH, HEIGHT//12))
        pygame.draw.rect(self.screen, (27, 27, 27), (0, HEIGHT-HEIGHT//12, WIDTH, HEIGHT // 12))
        self.btn4.draw(877, HEIGHT - HEIGHT // 12, "Back", lambda: self.change("Map"))
        # draw gear image button
        self.btnImg.draw(WIDTH-HEIGHT//12,0,lambda: self.change("Options"))
        self.btn5.draw(WIDTH-3*WIDTH // 12, HEIGHT-HEIGHT//12, "End Turn", lambda: player.endTurn())

        #   draw characteristics
        draw_text(self.screen,f"Health : {player.health}",WIDTH//24,HEIGHT-HEIGHT//12,MAP_FONT,color=(255,255,255))
        draw_text(self.screen, f"Energy : {player.energy}", WIDTH-9*WIDTH // 12, HEIGHT - HEIGHT // 12, MAP_FONT,
                  color=(255, 255, 255))
        draw_text(self.screen, f"Enemy Health : {mobs.health}", WIDTH - 6 * WIDTH // 12, 0, MAP_FONT,
                  color=(255, 255, 255))
        self.screen.blit(player.image, player.rect)
        self.screen.blit(mobs.image, mobs.rect)
        for a in player.hand:
            self.screen.blit(a.image, a.rect)

        #   draw arts
        for i,a in enumerate(player.artifacts):
            self.screen.blit(self.art, (i*HEIGHT//12, 0))
        pygame.display.flip()

