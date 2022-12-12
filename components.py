import pygame
from SETTINGS import MAIN_MENU_FONT

def draw_text(surface,text,x,y,font,color=(255, 255, 255)):
    surface.blit(font.render(f'{text}', True, color), (x, y))

class Button:
    def __init__(self,w,h,color,color_hover,screen,font):
        self.screen = screen
        self.width = w
        self.height = h
        self.color_hover = color_hover
        self.color = color
        self.font = font        

    def draw(self,x,y,text,command=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            if self.color_hover:
                pygame.draw.rect( self.screen,self.color_hover,(x,y,self.width,self.height))
            if click[0]==1 and command is not None:
                command()
                pygame.time.delay(100)
        else:
            if self.color:
                pygame.draw.rect( self.screen,self.color,(x,y,self.width,self.height))
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
    def __init__(self,screen,size,color,color_hover,x,y,color_used=(255,0,0)):
        self.x = x
        self.y = y
        self.screen = screen
        self.size = size
        self.color = color
        self.color_hover = color_hover
        self.isUsed = False
        self.color_used = color_used

    def draw(self,text,command=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.isUsed:
            pygame.draw.circle(self.screen, self.color_used, (self.x + self.size // 2, self.y + self.size // 2), self.size // 2 + 10)
        if self.x < mouse[0] < self.x + self.size and self.y < mouse[1] < self.y + self.size and not self.isUsed:

            if click[0]==1 and command is not None :
                self.isUsed = True
                command()


            pygame.draw.circle(self.screen, self.color_hover,(self.x+self.size//2, self.y+self.size//2), self.size//2+5)

        pygame.draw.circle(self.screen, self.color,
                           (self.x+self.size//2, self.y+self.size//2),
                           self.size//2)
        draw_text(self.screen, text, self.x, self.y,MAIN_MENU_FONT)

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
       pygame.draw.line(self.screen,
                        self.color_used if used else self.color,
                        [self.NodeIN.x + self.NodeIN.size // 2, self.NodeIN.y + self.NodeIN.size // 2],
                        [self.NodeOUT.x + self.NodeOUT.size // 2, self.NodeOUT.y + self.NodeOUT.size // 2],
                        self.size
                        )



