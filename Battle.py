import pygame
from components import Button, draw_text, ButtonImage
from SETTINGS import MAIN_MENU_FONT,MAIN_MENU_FONT_LOGO,BATTLE_HP_FONT, WIDTH, HEIGHT, MAP_FONT

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
        fire = pygame.image.load("Agnosia_assets/effect_icons/flame.png")
        self.fireIcon = pygame.transform.scale(fire, (40, 40))
        blind = pygame.image.load("Agnosia_assets/effect_icons/blind.png")
        self.blindIcon = pygame.transform.scale(blind, (40, 40))
        power = pygame.image.load("Agnosia_assets/effect_icons/power.png")
        self.powerIcon = pygame.transform.scale(power, (40, 40))
        disarm = pygame.image.load("Agnosia_assets/effect_icons/disarm.png")
        self.disarmIcon = pygame.transform.scale(disarm, (40, 40))
        weakness = pygame.image.load("Agnosia_assets/effect_icons/weakness.png")
        self.weaknessIcon = pygame.transform.scale(weakness, (40, 40))
        self.backBtn = Button(145, 80, None, (0, 0, 0), screen, MAIN_MENU_FONT)
        self.endTurnBtn = Button(300, 80, None, None, screen, BATTLE_HP_FONT)


    def draw(self, player, mobs):
        self.screen.fill((255, 0, 0))
        self.screen.blit(self.bg, (0, 0))

        # draw rect
        rect = pygame.Rect(0, 0, WIDTH, HEIGHT//12)
        pygame.draw.rect(self.screen, (27,27,27), (0, 0, WIDTH, HEIGHT//12))
        #pygame.draw.rect(self.screen, (27, 27, 27), (0, HEIGHT-HEIGHT//12, WIDTH, HEIGHT // 12))
        self.backBtn.draw(877, HEIGHT - HEIGHT // 12, "Back", lambda: self.change("Map"))
        # draw gear image button
        self.btnImg.draw(WIDTH-HEIGHT//12,0,lambda: self.change("Options"))
        self.endTurnBtn.draw(1578, 922,"", lambda: player.endTurn(mobs))

        #   draw characteristics
        draw_text(self.screen,f"{player.health}",WIDTH-1477,HEIGHT-202,BATTLE_HP_FONT,color=(32,158,0))
        draw_text(self.screen, f"{player.energy}", WIDTH-1530, HEIGHT -82, BATTLE_HP_FONT,
                  color=(255, 181, 36))
        draw_text(self.screen, f"{player.block}", WIDTH - 1500, HEIGHT -140, BATTLE_HP_FONT,
                  color=(1, 103, 255))
        draw_text(self.screen, f"Enemy H : {mobs.health}", WIDTH - 6 * WIDTH // 12, 0, MAP_FONT,
                  color=(255, 255, 255))
        draw_text(self.screen, f"Enemy B : {mobs.block}", WIDTH - 3 * WIDTH // 12, 0, MAP_FONT,
                  color=(255, 255, 255))
        self.screen.blit(player.image, player.rect)
        self.screen.blit(mobs.image, mobs.rect)
        pygame.draw.rect(self.screen, (27, 27, 27), (1518, 650, 205, 40))
        pygame.draw.rect(self.screen, (27, 27, 27), (198, 650, 205, 40))
        if player.effects["blind"]>0:
            self.screen.blit(self.blindIcon, (198, 650, 40, 40))
        if player.effects["disarm"]>0:
            self.screen.blit(self.disarmIcon, (239, 650, 40, 40))
        if player.effects["fire"]>0:
            self.screen.blit(self.fireIcon, (280, 650, 40, 40))
        if player.effects["power"]>0:
            self.screen.blit(self.powerIcon, (321, 650, 40, 40))
        if player.effects["weakness"]>0:
            self.screen.blit(self.weaknessIcon, (362, 650, 40, 40))
        if mobs.effects["blind"]>0:
            self.screen.blit(self.blindIcon, (1518, 650, 40, 40))
        if mobs.effects["disarm"]>0:
            self.screen.blit(self.disarmIcon, (1559, 650, 40, 40))
        if mobs.effects["fire"]>0:
            self.screen.blit(self.fireIcon, (1600, 650, 40, 40))
        if mobs.effects["power"]>0:
            self.screen.blit(self.powerIcon, (1641, 650, 40, 40))
        if mobs.effects["weakness"]>0:
            self.screen.blit(self.weaknessIcon, (1682, 650, 40, 40))
        for a in player.hand:
            self.screen.blit(a.image, a.rect)

        #   draw arts
        for i,a in enumerate(player.artifacts):
            self.screen.blit(self.art, (i*HEIGHT//12, 0))
        pygame.display.flip()

