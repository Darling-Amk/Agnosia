import pygame
from SETTINGS import MAIN_MENU_FONT
import Classes
import time
monsters = [
    pygame.image.load("Agnosia_assets/Agnosia_map_monster_missed.png").convert_alpha(),
    pygame.image.load("Agnosia_assets/Agnosia_map_monster.png").convert_alpha(),
    pygame.image.load("Agnosia_assets/Agnosia_map_monster_visited.png").convert_alpha(),
]
rand = [
    pygame.image.load("Agnosia_assets/Agnosia_random_event_missed.png").convert_alpha(),
    pygame.image.load("Agnosia_assets/Agnosia_random_event.png").convert_alpha(),
    pygame.image.load("Agnosia_assets/Agnosia_random_event_visited.png").convert_alpha(),
]
camp = [
    pygame.image.load("Agnosia_assets/Agnosia_map_campfire_missed.png").convert_alpha(),
    pygame.image.load("Agnosia_assets/Agnosia_map_campfire.png").convert_alpha(),
    pygame.image.load("Agnosia_assets/Agnosia_map_campfire_visited.png").convert_alpha(),
]
treasure= [
    pygame.image.load("Agnosia_assets/Agnosia_map_chest_missed.png").convert_alpha(),
    pygame.image.load("Agnosia_assets/Agnosia_map_chest.png").convert_alpha(),
    pygame.image.load("Agnosia_assets/Agnosia_map_chest_visited.png").convert_alpha(),
]
boss = [
    pygame.image.load("Agnosia_assets/Agnosia_map_boss.png").convert_alpha(),
    pygame.image.load("Agnosia_assets/Agnosia_map_boss.png").convert_alpha(),
    pygame.image.load("Agnosia_assets/Agnosia_map_boss_visited.png").convert_alpha(),
]

def draw_text(surface,text,x,y,font,color=(255, 255, 255)):
    surface.blit(font.render(f'{text}', True, color), (x, y))

class Button:
    def __init__(self,w,h,color,color_hover,screen,font):
        self.last = time.time()-2
        self.screen = screen
        self.width = w
        self.height = h
        self.color_hover = color_hover
        self.color = color
        self.font = font        

    def draw(self,x,y,text,command=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        f = self.last+1< time.time()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            if self.color_hover:
                pygame.draw.rect( self.screen,self.color_hover,(x,y,self.width,self.height))
            if click[0]==1 and command is not None and f:
                self.last = time.time()
                command()
                pygame.time.delay(300)

        else:
            if self.color :
                pygame.draw.rect( self.screen,self.color,(x,y,self.width,self.height))

        if not f:
            pygame.draw.rect(self.screen, (100, 100, 100), (x - 10, y - 10, self.width + 20, self.height + 20))

        draw_text(self.screen, text, x, y,self.font)

class ButtonImage:
    def __init__(self,screen,w,h,image,image_hover=None):
        self.img_hover = image if image_hover == None else image_hover
        self.img_hover = pygame.image.load(self.img_hover)

        self.img = pygame.image.load(image)
        self.img.set_colorkey((255, 255, 255))
        self.img = pygame.transform.scale(self.img, (w, h))

        self.img_hover.set_colorkey((255, 255, 255))
        self.img_hover = pygame.transform.scale(self.img_hover, (w, h))
        self.screen = screen
        self.width = w
        self.height = h



    def draw(self,x,y,command=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()


        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            if click[0]==1 and command is not None:

                command()
                pygame.time.delay(100)
            self.screen.blit(self.img_hover, (x, y))
        else:
            self.screen.blit(self.img,(x,y))


class Node:
    def __init__(self,screen,size,color,color_hover,x,y,color_used=(255,0,0),type_room=None):
        print(type_room)
        self.type_arr = monsters
        if type(type_room) is Classes.Camp:
            self.type_arr = camp
        if type(type_room) is Classes.Treasure:
            self.type_arr = treasure
        if type(type_room) is Classes.RandomEvent:
            self.type_arr = rand
        self.size = size * 5
        self.x = x-self.size//2
        self.y = y-self.size//2
        self.screen = screen

        self.color = color
        self.color_hover = color_hover
        self.isUsed = False
        self.color_used = color_used
        self.isGray = False

    def draw(self,name,Graph,nodes,command=None):
        if name == ("Out"):
            self.type_arr = boss
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        canGo = name=="In"
        for u in Graph:
            if nodes[u].isUsed and name in Graph[u]:
                canGo = True
        if name not in ("In","Out"):
            for u in Graph:
                if u in (name,"In","Out"):continue
                if name//5 == u//5 and nodes[u].isUsed:
                    canGo = False
                    self.isGray = True
        if self.isUsed:
            self.screen.blit(pygame.transform.scale(self.type_arr[2],(self.size,self.size)),(self.x , self.y ))
            #pygame.draw.circle(self.screen, self.color_used, (self.x + self.size // 2, self.y + self.size // 2), self.size // 2 + 10)

        if self.x < mouse[0] < self.x + self.size and self.y < mouse[1] < self.y + self.size and not self.isUsed and canGo:
            if click[0]==1 and command is not None :
                self.isUsed = True
                command()

            pygame.draw.circle(self.screen, self.color_hover,(self.x+self.size//2, self.y+self.size//2), self.size//2+5)
        if not self.isGray:
            self.screen.blit(pygame.transform.scale(self.type_arr[1], (self.size, self.size)), (self.x, self.y))
            # pygame.draw.circle(self.screen, self.color,
            #                    (self.x+self.size//2, self.y+self.size//2),
            #                    self.size//2)
            #draw_text(self.screen, str(name), self.x, self.y,MAIN_MENU_FONT)
        else:
            # pygame.draw.circle(self.screen, (25,25,25),
            #                    (self.x + self.size // 2, self.y + self.size // 2),
            #                    self.size // 2)
            self.screen.blit(pygame.transform.scale(self.type_arr[0], (self.size, self.size)), (self.x, self.y))

class Edge:
    def __init__(self,screen,NodeIN :Node ,NodeOUT :Node ,size,color,color_used=(255,0,0)):
        self.screen = screen
        self.size = size
        self.color = color
        self.NodeIN = NodeIN
        self.NodeOUT = NodeOUT
        self.color_used = color_used

    def draw(self):
       used = self.NodeIN.isUsed & self.NodeOUT.isUsed
       gray = self.NodeIN.isGray | self.NodeOUT.isGray

       if gray:
           pygame.draw.line(self.screen,
                            (100,100,100),
                            [self.NodeIN.x + self.NodeIN.size // 2, self.NodeIN.y + self.NodeIN.size // 2],
                            [self.NodeOUT.x + self.NodeOUT.size // 2, self.NodeOUT.y + self.NodeOUT.size // 2],
                            self.size
                            )

       else:
           pygame.draw.line(self.screen,
                            self.color_used if used else self.color,
                            [self.NodeIN.x + self.NodeIN.size // 2, self.NodeIN.y + self.NodeIN.size // 2],
                            [self.NodeOUT.x + self.NodeOUT.size // 2, self.NodeOUT.y + self.NodeOUT.size // 2],
                            self.size
                            )



