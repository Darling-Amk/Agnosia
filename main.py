from SETTINGS import *
from UserInterfaceClass import UserInterface
from Classes import Player, Goblin

screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.set_colorkey((27,27,27))
screen.set_alpha(100)
clock = pygame.time.Clock()

player = Player()
player.artifacts = ["hui","pizda"]
dragged = pygame.sprite.Group()
monsterHP = 10
items = pygame.sprite.Group()
mobs = Goblin(player)

UI = UserInterface(screen, player)
#UI.restart.add(player.restart)
play = True

while play:
    scene = UI.draw(player, mobs)
    if scene =="Battle":
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
                    if len(dragged) == 0 and b.rect.colliderect(mobs.rect):
                        flag = b.play(player,mobs)
                        if flag == 1:
                            player.hand.remove(b)
                        elif flag == 2:
                            UI.changeScene("Map")
            elif e.type == pygame.MOUSEMOTION:
                if len(dragged) > 0:
                    for a in dragged:
                        a.rect.move_ip(e.rel)
    if scene=="None":
        play = False
    items.empty()
    clock.tick(30)



pygame.quit()



