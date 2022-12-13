import random
import pygame
import sys


class Card(pygame.sprite.Sprite):
    def __init__(self):
        super(pygame.sprite.Sprite, self).__init__()
        self._price = None
        self.upgraded = False
        self._canBeUpgraded = False

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self, player):
        pass

    def play(self, player, creature):
        pass


class Attack(Card):
    def __init__(self):
        super(Attack, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 1
        self.damage = 5
        self.upgraded = False
        self._canBeUpgraded = True
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/Strike.png").convert_alpha(), (148,234))
        self.rect = self.image.get_rect(
            center=(500, 900))

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self, player):
        a = AttackUpgraded()
        player.cards.add(a)
        player.cards.remove(self)

    def play(self, player, monster):
        dmg = self.damage
        if player.effects["weakness"]>0: #weakness
            dmg = int(dmg*0.75)
        if player.effects["power"]>0: #power
            dmg = int(dmg * 1.25)
        if player.effects["disarm"]>0: #disarm
            dmg = 0
        if player.effects["blind"]>0: #blind
            dmg = int(dmg*0.75)
        if player.energy >= self._price:
            player.energy -= self._price
            tmp = monster.makeDamage(dmg)
            if tmp:
                return 2
            return 1
        return 0


class AttackUpgraded(Card):
    def __init__(self):
        super(AttackUpgraded, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 1
        self.upgraded = True
        self._canBeUpgraded = False
        self.damage = 8
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/Strike+.png").convert_alpha(),
                                            (148, 234))
        self.rect = self.image.get_rect(
            center=(500, 900))

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self):
        pass

    def play(self, player, monster):
        dmg = self.damage
        if player.effects["weakness"]>0: #weakness
            dmg = int(dmg*0.75)
        if player.effects["power"]>0: #power
            dmg = int(dmg * 1.25)
        if player.effects["disarm"]>0: #disarm
            dmg = 0
        if player.effects["blind"]>0: #blind
            dmg = int(dmg*0.75)
        if player.energy >= self._price:
            player.energy -= self._price
            tmp = monster.makeDamage(dmg)
            if tmp:
                return 2
            return 1
        return 0



