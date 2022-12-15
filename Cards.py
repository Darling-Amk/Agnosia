import random
import pygame
import sys
from random import shuffle

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
        self.type = "Attack"
        self.upgraded = False
        self._canBeUpgraded = True
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/Strike.png").convert_alpha(), (148,234))
        self.rect = self.image.get_rect(
            center=(500, 800))

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self, player):
        a = AttackUpgraded()
        player.deck.append(a)
        player.deck.remove(self)

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
            player.hand.remove(self)
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
        self.type = "Attack"
        self.upgraded = True
        self._canBeUpgraded = False
        self.damage = 8
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/Strike+.png").convert_alpha(),
                                            (148, 234))
        self.rect = self.image.get_rect(
            center=(500, 800))

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
            player.hand.remove(self)
            tmp = monster.makeDamage(dmg)
            if tmp:
                return 2
            return 1
        return 0

class Shield(Card):
    def __init__(self):
        super(Shield, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 1
        self.block = 5
        self.type = "Defend"
        self.upgraded = False
        self._canBeUpgraded = True
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/Shield.png").convert_alpha(), (148,234))
        self.rect = self.image.get_rect(
            center=(500, 800))

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self, player):
        a = ShieldUpgraded()
        player.deck.append(a)
        player.deck.remove(self)

    def play(self, player, monster):
        if player.energy >= self._price:
            player.energy -= self._price
            player.hand.remove(self)
            player.block += self.block
            return 1
        return 0


class ShieldUpgraded(Card):
    def __init__(self):
        super(ShieldUpgraded, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 1
        self.type = "Defend"
        self.upgraded = True
        self._canBeUpgraded = False
        self.block = 8
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/Shield+.png").convert_alpha(),
                                            (148, 234))
        self.rect = self.image.get_rect(
            center=(500, 800))

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self):
        pass

    def play(self, player, monster):
        if player.energy >= self._price:
            player.energy -= self._price
            player.hand.remove(self)
            player.block += self.block
            return 1
        return 0


class UnexpectedMove(Card):
    def __init__(self):
        super(UnexpectedMove, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 0
        self.type = "Utility"
        self.upgraded = False
        self._canBeUpgraded = True
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/UnexpectedMove.png").convert_alpha(), (148,234))
        self.rect = self.image.get_rect(
            center=(500, 800))

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self, player):
        a = UnexpectedMoveUpgraded()
        player.deck.append(a)
        player.deck.remove(self)

    def play(self, player, monster):
        start = 800
        for i in range(2):
            if len(player.draw) == 0:
                player.draw = player.deck.copy()
                for j in player.hand:
                    player.draw.remove(j)
                shuffle(player.draw)
            player.hand.append(player.draw.pop())

        player.hand.remove(self)
        for a in player.hand:  # 1920 - длина области, ширина будет 200
            a.rect = a.image.get_rect(center=(start, 941))
            start += 150
        return 1

class UnexpectedMoveUpgraded(Card):
    def __init__(self):
        super(UnexpectedMoveUpgraded, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 0
        self.damage = 2
        self.type = "Utility"
        self.upgraded = True
        self._canBeUpgraded = False
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/UnexpectedMove+.png").convert_alpha(),
                                            (148, 234))
        self.rect = self.image.get_rect(
            center=(500, 800))

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self):
        pass

    def play(self, player, monster):
        dmg = self.damage
        if player.effects["weakness"] > 0:  # weakness
            dmg = int(dmg * 0.75)
        if player.effects["power"] > 0:  # power
            dmg = int(dmg * 1.25)
        if player.effects["disarm"] > 0:  # disarm
            dmg = 0
        if player.effects["blind"] > 0:  # blind
            dmg = int(dmg * 0.75)
        if player.energy >= self._price:
            player.energy -= self._price
            tmp = monster.makeDamage(dmg)
            if tmp:
                return 2
        start = 800
        for i in range(2):
            if len(player.draw) == 0:
                player.draw = player.deck.copy()
                for j in player.hand:
                    player.draw.remove(j)
                shuffle(player.draw)
            player.hand.append(player.draw.pop())

        player.hand.remove(self)
        for a in player.hand:  # 1920 - длина области, ширина будет 200
            a.rect = a.image.get_rect(center=(start, 941))
            start += 150
        return 1

class Burning(Card):
    def __init__(self):
        super(Burning, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 1
        self.type = "Attack"
        self.upgraded = False
        self._canBeUpgraded = True
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/Burn.png").convert_alpha(), (148,234))
        self.rect = self.image.get_rect(
            center=(500, 800))

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self, player):
        a = BurningUpgraded()
        player.deck.append(a)
        player.deck.remove(self)

    def play(self, player, monster):
        if player.energy >= self._price:
            player.energy -= self._price
            player.hand.remove(self)
            monster.makeEffect("fire", 3)
            return 1
        return 0


class BurningUpgraded(Card):
    def __init__(self):
        super(BurningUpgraded, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 2
        self.upgraded = True
        self._canBeUpgraded = False
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/Burn+.png").convert_alpha(),
                                            (148, 234))
        self.rect = self.image.get_rect(
            center=(500, 800))

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self):
        pass

    def play(self, player, monster):
        if player.energy >= self._price:
            player.energy -= self._price
            player.hand.remove(self)
            monster.makeEffect("fire", 5)

            return 1
        return 0

class SharpBlade(Card):
    def __init__(self):
        super(Attack, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 1
        self.damage = 9
        self.type = "Attack"
        self.upgraded = False
        self._canBeUpgraded = True
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/Strike.png").convert_alpha(), (148,234))
        self.rect = self.image.get_rect(
            center=(500, 800))

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self, player):
        a = AttackUpgraded()
        player.deck.append(a)
        player.deck.remove(self)

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
            player.hand.remove(self)
            tmp = monster.makeDamage(dmg)
            cmp = player.makeDamage(2)
            if cmp:
                return 0
            if tmp:
                return 2
            return 1
        return 0


class SharpBladeUpgraded(Card):
    def __init__(self):
        super(SharpBladeUpgraded, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 1
        self.type = "Attack"
        self.upgraded = True
        self._canBeUpgraded = False
        self.damage = 12
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/Strike+.png").convert_alpha(),
                                            (148, 234))
        self.rect = self.image.get_rect(
            center=(500, 800))

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
            player.hand.remove(self)
            tmp = monster.makeDamage(dmg)
            cmp = player.makeDamage(2)
            if cmp:
                return 0
            if tmp:
                return 2
            return 1
        return 0