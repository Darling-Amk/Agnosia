import pygame
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
                #pygame.time.delay(100)
        else:
            if self.color:
                pygame.draw.rect( self.screen,self.color,(x,y,self.width,self.height))
        draw_text(self.screen, text, x, y,self.font)

class Node:
    def __init__(self,size,color,color_hover,screen,font):
        self.screen = screen
        self.size = size
        self.color = color
        self.color_hover = color_hover
        self.font = font
        self.isUsed = False

    def draw(self,x,y,text,command=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.size and y < mouse[1] < y + self.size:

            if click[0]==1 and command is not None and not self.isUsed:
                self.isUsed = True
                command()
                #pygame.time.delay(100)

            pygame.draw.circle(self.screen, self.color_hover,(x+self.size//2, y+self.size//2), self.size//2+5)

        else:
            ...

        pygame.draw.circle(self.screen, self.color,
                           (x+self.size//2, y+self.size//2),
                           self.size//2)
        draw_text(self.screen, text, x, y,self.font)

