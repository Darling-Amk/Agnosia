from SETTINGS import *
import random
from datetime import datetime
#screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
from UserInterfaceClass import UserInterface
from Classes import Player, Goblin

random.seed(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
screen.set_colorkey((27,27,27))
screen.set_alpha(100)
clock = pygame.time.Clock()

player = Player()
player.artifacts = ["hui","pizda"]
dragged = pygame.sprite.Group()
items = pygame.sprite.Group()
mobs = Goblin(player)

UI = UserInterface(screen, player)
UI.restart.add(player.restart)
play = True

while play:
    scene = UI.draw(player, mobs)
    if scene == "Battle":
        mobs = UI.mobs
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            play = False
        if scene == "Battle":
            if player.makeDamage(0):
                player.restart()
                UI.changeScene("Menu")
            for a in player.hand:
                items.add(a)
            if e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if len(dragged) == 0:
                    pass
                    dragged.add(x for x in items if x.rect.collidepoint(e.pos))
                else:
                    dragged.empty()
                for b in items:
                    if len(dragged) == 0 and b.rect.colliderect(mobs.rect) and b.type == "Attack":
                        flag = b.play(player,mobs)
                        #if flag == 1:
                            #player.hand.remove(b)
                        if flag == 2:
                            UI.changeScene("Award")
                    if len(dragged) == 0 and b.rect.colliderect(player.rect) and (b.type == "Utility" or b.type == "Defend"):
                        flag = b.play(player,mobs)
            elif e.type == pygame.MOUSEMOTION:
                if len(dragged) > 0:
                    for a in dragged:
                        a.rect.move_ip(e.rel)
        elif scene == "CampUpgrade":
            for a in player.deck:
                if a.canBeUpgraded():
                    items.add(a)
            if e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for b in items:
                    if b.rect.collidepoint(e.pos):
                        b.upgrade(player)
                        UI.changeScene("Map")
        elif scene == "Award":
            for a in UI.mobs:
                items.add(a)
            if e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for b in items:
                    if b.rect.collidepoint(e.pos):
                        player.deck.append(b)
                        UI.changeScene("Map")





    if scene=="None":
        play = False
    items.empty()
    clock.tick(30)



pygame.quit()



