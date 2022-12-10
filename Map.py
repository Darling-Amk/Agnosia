import pygame
from components import Button,Node,Edge,ButtonImage,draw_text
from SETTINGS import MAIN_MENU_FONT,WIDTH,HEIGHT,MAP_FONT

from Classes import  Scene

# Когда добавят арты удалить

class MapScene(Scene):
    def __init__(self,screen,name,change,bg_image):



        # Когда будут арты удалить
        Art = pygame.image.load("Agnosia_assets/tmp_art.png")
        Art.set_colorkey((255, 255, 255))
        self.art = Art = pygame.transform.scale(Art, (HEIGHT//12, HEIGHT//12))


        super().__init__(screen,name,change,bg_image)

        # генератор графа
        self.btnImg = ButtonImage(screen,HEIGHT//12,HEIGHT//12,
                                  image="Agnosia_assets/Agnosia_interface_settings.png",
                                  image_hover="Agnosia_assets/Agnosia_interface_settings_hover.png"
                                  )
        self.btn = Button(200, 42, (0, 255, 0), (0, 0, 0), screen,font = MAIN_MENU_FONT )
        self.node1 = Node(size=30,color=(0, 128, 128), color_hover=(128, 0, 0),screen=screen,x=150,y=150)
        self.node2 = Node(size=30, color=(0, 128, 128), color_hover=(128, 0, 0), screen=screen,x=250,y=150)
        self.edge = Edge(screen,self.node1,self.node2,size =5,color=(255,255,255))


    def draw(self, player):
        self.screen.fill((255, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        # For drawing
        pygame.draw.rect(self.screen, (27,27,27), (0, 0, WIDTH, HEIGHT//12))
        pygame.draw.rect(self.screen, (27, 27, 27), (0, HEIGHT-HEIGHT//12, WIDTH, HEIGHT // 12))
        self.btnImg.draw(WIDTH-HEIGHT//12,0,lambda: self.change("Options"))

        draw_text(self.screen,f"Player Health : {player.health}",WIDTH//12,HEIGHT-HEIGHT//12,MAP_FONT,color=(255,255,255))
        draw_text(self.screen, f"Player Energy : {player.energy}", WIDTH-4*WIDTH // 12, HEIGHT - HEIGHT // 12, MAP_FONT,
                  color=(255, 255, 255))
        for i,a in enumerate(player.artifacts):
            self.screen.blit(self.art, (i*HEIGHT//12, 0))


        self.edge.draw()

        self.node1.draw("1", lambda: self.change("Battle"))
        self.node2.draw("2", lambda: print("hi"))


        pygame.display.flip()