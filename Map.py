import pygame
from components import Button,Node,Edge
from SETTINGS import MAIN_MENU_FONT

from Classes import  Scene

class MapScene(Scene):
    def __init__(self,screen,name,change,bg_image):
        super().__init__(screen,name,change,bg_image)
        self.btn = Button(200, 42, (0, 255, 0), (0, 0, 0), screen,font =MAIN_MENU_FONT )
        self.node1 = Node(size=30,color=(0, 128, 128), color_hover=(128, 0, 0),screen=screen,x=150,y=150)
        self.node2 = Node(size=30, color=(0, 128, 128), color_hover=(128, 0, 0), screen=screen,x=250,y=150)
        self.edge = Edge(screen,self.node1,self.node2,size =5,color=(255,255,255))


    def draw(self, state):
        self.screen.fill((255, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        # For drawing
        self.btn.draw(830, 1000, "Back", lambda: self.change("Menu"))

        self.edge.draw()

        self.node1.draw("1", lambda: self.change("Battle"))
        self.node2.draw("2", lambda: print("hi"))


        pygame.display.flip()