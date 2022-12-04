import pygame


def draw_text(surface,text,x,y,font,color=(255, 255, 255)):
    surface.blit(font.render(f'{text}', True, color), (x, y))

class Button:
    def __init__(self,w,h,c1,c2,display,font):
        self.display = display
        self.width = w
        self.height = h
        self.active_color = c2
        self.inactive_color = c1
        self.font = font
    def draw(self,x,y,text,command=None):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            if self.active_color:
                pygame.draw.rect( self.display,self.active_color,(x,y,self.width,self.height))
            if click[0]==1 and command is not None:
                command()
                pygame.time.delay(100)
        else:
            if self.inactive_color:
                pygame.draw.rect( self.display,self.inactive_color,(x,y,self.width,self.height))
        draw_text(self.display, text, x, y,self.font)
