import pygame
import sys
from random import randint
from Classes import Card


class Attack(Card):
    def __init__(self):
        self._price = 1
        self.upgraded = False
        self._canBeUpgraded = True

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self, player):
        a = AttackUpgraded()
        player.cards.add(a)
        player.cards.remove(self)

    def play(self, player, monster):
        if player.energy >= self._price:
            player.energy -= self._price
            monster.makeDamage(5)


class AttackUpgraded(Card):
    def __init__(self):
        self._price = 1
        self.upgraded = True
        self._canBeUpgraded = False

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self):
        pass

    def play(self, player, monster):
        if player.energy >= self._price:
            player.energy -= self._price
            monster.makeDamage(8)


W = 1920
H = 1080
WHITE = (255, 255, 255)


class Car(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            "Agnosia_assets/front.png").convert_alpha()
        self.rect = self.image.get_rect(
            center=(500, 900))

    def update(self, rel):
        self.rect.move_ip(rel)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            "Agnosia_assets/Agnosia_map_boss.png").convert_alpha()
        self.rect = self.image.get_rect(
            center=(1400, 500))

    def update(self, rel):
        self.rect.move_ip(rel)


sc = pygame.display.set_mode((W, H))
# координата x будет случайна
car1 = Car(0, 'car1.png')
drag=0
energy=3
monsterHP = 10
pygame.init()
font = pygame.font.Font("fonts/GrechenFuemen-Regular.ttf", 80)
img = font.render(str(energy)+'/3', True, (0,0,255))
img2 = font.render(str(monsterHP)+'/10', True, (255,0,0))
enm = Enemy(0,'aboab')
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if car1.rect.collidepoint(pos):
                drag = 1-drag
                if drag == 0 and car1.rect.colliderect(enm.rect):
                    energy-=1
                    monsterHP-=5
                    img = font.render(str(energy) + '/3', True, (0, 0, 255))
                    img2 = font.render(str(monsterHP) + '/10', True, (255, 0, 0))
        elif i.type == pygame.MOUSEMOTION:
            if drag:
                car1.update(i.rel)

    sc.fill(WHITE)
    sc.blit(car1.image, car1.rect)
    sc.blit(enm.image, enm.rect)
    sc.blit(img, (1500, 20))
    sc.blit(img2, (1500, 100))
    pygame.display.update()
    pygame.time.delay(5)

    # машинка ездит сверху вниз
    #if car1.rect.y < H:
        #car1.rect.y += 2
    #else:
        #car1.rect.y = 0

