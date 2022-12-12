import pygame

import Classes
from components import Button,Node,Edge,ButtonImage,draw_text
from SETTINGS import MAIN_MENU_FONT,WIDTH,HEIGHT,MAP_FONT
from GraphTest import generateGraph
from GraphTest import generateEvents
from Classes import  Scene

# Когда добавят арты удалить

class MapScene(Scene):    
    def __init__(self,screen,name,change,bg_image, player):        
        super().__init__(screen, name, change, bg_image)
        self.player = player
        # Когда будут арты удалить
        Art = pygame.image.load("Agnosia_assets/tmp_art.png")
        Art.set_colorkey((255, 255, 255))
        self.art  = pygame.transform.scale(Art, (HEIGHT//12, HEIGHT//12))
        self.createGraph()
        # генератор графа
        self.btnImg = ButtonImage(screen,HEIGHT//12,HEIGHT//12,
                                  image="Agnosia_assets/Agnosia_interface_settings.png",
                                  image_hover="Agnosia_assets/Agnosia_interface_settings_hover.png"
                                  )
        self.btn = Button(200, 42, (0, 255, 0), (0, 0, 0), screen,font = MAIN_MENU_FONT )        

    def createGraph(self):
        self.Graph = generateGraph()
        self.events = generateEvents(self.Graph, self.player)
        self.nodes = {}
        self.edges = {}

        for node in self.Graph:
            if node == "In":
                self.nodes[node] = Node(size=30, color=(0, 128, 128), color_hover=(128, 0, 0), screen=self.screen,
                                        x=WIDTH//12, y=6*HEIGHT//12)
                continue
            elif node == "Out":
                self.nodes[node] = Node(size=30, color=(0, 128, 128), color_hover=(128, 0, 0), screen=self.screen,
                                        x=WIDTH-WIDTH//12, y=6*HEIGHT//12)
                continue


            self.nodes[node] = Node(size=30, color=(0, 128, 128), color_hover=(128, 0, 0), screen=self.screen,
                                    x= 3*WIDTH//12+ ((node - 1) // 5)* 2 * WIDTH//12,
                                    y=self.getYForNode(node))

        for u in self.Graph:
            for  v in self.Graph[u]:
                u_, v_ = u,v
                if type(u)==type(v):
                    u_,v_ = max(u,v),min(u,v)
                if (u_,v_) in self.edges:continue
                self.edges[(u_,v_)] = Edge(self.screen, self.nodes[u_], self.nodes[v_], size=5, color=(255, 255, 255))

    def getYForNode(self,v):
        count = 0
        for u in self.Graph:
            if u in ("In","Out"):continue

            if (v-1)//5 == (u-1)//5:
                count+=1
        if count==1:
            return 6*HEIGHT//12
        if count==2:
            return 6 * HEIGHT // 12 + (HEIGHT // 12) * (-1 if v%2==0 else 1)
        if count == 3:
            if v % 3==2:
                return 6 * HEIGHT // 12
            return 6 * HEIGHT // 12 + (2* HEIGHT // 12) * (-1 if (v % 3 == 1) else 1)

        if count==4:
            if v%4 in (1,2):
                return (6 * HEIGHT // 12 ) - (v%4* 2*HEIGHT // 12)
            else:
                return 6 * HEIGHT // 12 + (2*HEIGHT // 12) * ((v+ 1) % 2 + 1)

        return 2*HEIGHT//12 + ((v - 1) % count) *2*HEIGHT//12


    def draw(self, player):
        self.screen.fill((255, 0, 0))
        self.screen.blit(self.bg, (0, 0))

        # draw rect
        pygame.draw.rect(self.screen, (27,27,27), (0, 0, WIDTH, HEIGHT//12))
        pygame.draw.rect(self.screen, (27, 27, 27), (0, HEIGHT-HEIGHT//12, WIDTH, HEIGHT // 12))

        # draw gear image button
        self.btnImg.draw(WIDTH-HEIGHT//12,0,lambda: self.change("Options"))

        #   draw characteristics
        draw_text(self.screen,f"Player Health : {player.health}",WIDTH//12,HEIGHT-HEIGHT//12,MAP_FONT,color=(255,255,255))
        draw_text(self.screen, f"Player Energy : {player.energy}", WIDTH-4*WIDTH // 12, HEIGHT - HEIGHT // 12, MAP_FONT,
                  color=(255, 255, 255))

        #   draw arts
        for i,a in enumerate(player.artifacts):
            self.screen.blit(self.art, (i*HEIGHT//12, 0))

        #   draw edges
        [self.edges[edge].draw() for edge in self.edges]

        #   draw nodes
        for node in self.nodes:
            if type(self.events[node]) is Classes.Dragon or type(self.events[node]) is Classes.Vampire or type(self.events[node]) is Classes.Goblin or type(self.events[node]) is Classes.Phoenix:
                self.nodes[node].draw(str(node),lambda: self.change("Battle", self.events[node]))
                player.endTurn(1)
            else: self.nodes[node].draw(str(node), lambda: print(node))

        pygame.display.flip()