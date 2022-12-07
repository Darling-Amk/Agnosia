import random

import pygame
import sys
from random import shuffle
from Classes import Card
from Classes import Player


class Attack(Card):
    def __init__(self):
        super(Attack, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 1
        self.upgraded = False
        self._canBeUpgraded = True
        self.image = pygame.image.load("Agnosia_assets/front.png").convert_alpha()
        self.rect = self.image.get_rect(
            center=(random.randint(0, 2000), 900))

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
            "Agnosia_assets/Agnosia_map_boss2.png").convert_alpha()
        self.rect = self.image.get_rect(
            center=(1400, 500))

    def update(self, rel):
        self.rect.move_ip(rel)


sc = pygame.display.set_mode((W, H))
car1 = Car(0, 'car1.png')
x = Attack()
player = Player()
for a in range(4):
    player.deck.append(x)
    x = Attack()
player.endTurn()
drag = 0
monsterHP = 10
pygame.init()
font = pygame.font.Font("fonts/GrechenFuemen-Regular.ttf", 80)
img = font.render(str(player.energy)+'/3', True, (0, 0, 255))
img2 = font.render(str(monsterHP)+'/10', True, (255, 0, 0))
enm = Enemy(0, 'aboab')
dragged = pygame.sprite.Group()
items = pygame.sprite.Group()
print(x)
while 1:
    for a in player.hand:
        items.add(a)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if len(dragged) == 0:
                pass
                dragged.add(x for x in items if x.rect.collidepoint(i.pos))
            else:
                dragged.empty()
            for b in items:
                if len(dragged) == 0 and b.rect.colliderect(enm.rect):
                    player.energy -= 1
                    monsterHP -= 5
                    player.hand.remove(b)
                    img = font.render(str(player.energy) + '/3', True, (0, 0, 255))
                    img2 = font.render(str(monsterHP) + '/10', True, (255, 0, 0))
        elif i.type == pygame.MOUSEMOTION:
            if len(dragged) > 0:
                for a in dragged:
                    a.rect.move_ip(i.rel)

    sc.fill(WHITE)
    for a in items:
        sc.blit(a.image, a.rect)
    sc.blit(enm.image, enm.rect)
    sc.blit(img, (1500, 20))
    sc.blit(img2, (1500, 100))
    items.empty()
    pygame.display.update()
    pygame.time.delay(5)


