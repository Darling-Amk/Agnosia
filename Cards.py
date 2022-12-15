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

def getThreeCards():
    allCards = [AttackUpgraded(), ShieldUpgraded(),UnexpectedMoveUpgraded(), Burning(), SharpBlade(),Shuriken(),EnBurst(),
                CounterStrike(), Infection(), Plague(), BrainOverflow()]
    first = random.randrange(0, len(allCards) - 2)
    second = random.randrange(first + 1, len(allCards) - 1)
    third = random.randrange(second + 1, len(allCards))
    return [allCards[first], allCards[second], allCards[third]]


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
                    try:
                        player.draw.remove(j)
                    except ValueError:
                        pass
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
        self._price = 2
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
        self.type = "Attack"
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
        super(SharpBlade, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 1
        self.damage = 9
        self.type = "Attack"
        self.upgraded = False
        self._canBeUpgraded = True
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/SharpSword.png").convert_alpha(), (148,234))
        self.rect = self.image.get_rect(
            center=(500, 800))

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self, player):
        a = SharpBladeUpgraded()
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
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/SharpSword+.png").convert_alpha(),
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

class Shuriken(Card):
    def __init__(self):
        super(Shuriken, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 2
        self.damage = 2
        self.type = "Attack"
        self.upgraded = False
        self._canBeUpgraded = True
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/Shuriken.png").convert_alpha(), (148,234))
        self.rect = self.image.get_rect(
            center=(500, 800))

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self, player):
        a = ShurikenUpgraded()
        player.deck.append(a)
        player.deck.remove(self)

    def play(self, player, monster):
        dmg = self.damage * len(player.hand)
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


class ShurikenUpgraded(Card):
    def __init__(self):
        super(ShurikenUpgraded, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 1
        self.type = "Attack"
        self.upgraded = True
        self._canBeUpgraded = False
        self.damage = 3
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/Shuriken+.png").convert_alpha(),
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
        dmg = self.damage * len(player.hand)
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

class EnBurst(Card):
    def __init__(self):
        super(EnBurst, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 0
        self.energy = 1
        self.type = "Utility"
        self.upgraded = False
        self._canBeUpgraded = True
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/EnBurst.png").convert_alpha(), (148,234))
        self.rect = self.image.get_rect(
            center=(500, 800))

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self, player):
        a = EnBurstUpgraded()
        player.deck.append(a)
        player.deck.remove(self)

    def play(self, player, monster):
        player.hand.remove(self)
        player.energy += self.energy
        return 1


class EnBurstUpgraded(Card):
    def __init__(self):
        super(EnBurstUpgraded, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 0
        self.energy = 2
        self.type = "Utility"
        self.upgraded = True
        self._canBeUpgraded = False
        self.block = 8
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/EnBurst+.png").convert_alpha(),
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
        player.hand.remove(self)
        player.energy += self.energy
        return 1


class CounterStrike(Card):
    def __init__(self):
        super(CounterStrike, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 0
        self.damage = 0
        self.type = "Attack"
        self.upgraded = False
        self._canBeUpgraded = True
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/CounterStrike.png").convert_alpha(), (148,234))
        self.rect = self.image.get_rect(
            center=(500, 800))

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self, player):
        a = CounterStrikeUpgraded()
        player.deck.append(a)
        player.deck.remove(self)

    def play(self, player, monster):
        dmg = int(player.block/2)
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


class CounterStrikeUpgraded(Card):
    def __init__(self):
        super(CounterStrikeUpgraded, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 0
        self.type = "Attack"
        self.upgraded = True
        self._canBeUpgraded = False
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/CounterStrike+.png").convert_alpha(),
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
        player.block += 5
        dmg = int(player.block/2)
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

class Infection(Card):
    def __init__(self):
        super(Infection, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 2
        self.type = "Attack"
        self.upgraded = False
        self._canBeUpgraded = True
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/Infection.png").convert_alpha(), (148,234))
        self.rect = self.image.get_rect(
            center=(500, 800))

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self, player):
        a = InfectionUpgraded()
        player.deck.append(a)
        player.deck.remove(self)

    def play(self, player, monster):
        if player.energy >= self._price:
            player.energy -= self._price
            player.hand.remove(self)
            monster.makeEffect("fire", 2)
            monster.makeEffect("disarm", 1)
            monster.makeEffect("blind", 2)
            monster.makeEffect("weakness", 2)
            return 1
        return 0


class InfectionUpgraded(Card):
    def __init__(self):
        super(InfectionUpgraded, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 1
        self.type = "Attack"
        self.upgraded = True
        self._canBeUpgraded = False
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/Infection+.png").convert_alpha(),
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
            monster.makeEffect("fire", 2)
            monster.makeEffect("disarm", 1)
            monster.makeEffect("blind", 2)
            monster.makeEffect("weakness", 2)
            return 1
        return 0

class Plague(Card):
    def __init__(self):
        super(Plague, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 2
        self.type = "Attack"
        self.upgraded = False
        self._canBeUpgraded = True
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/Plague.png").convert_alpha(), (148,234))
        self.rect = self.image.get_rect(
            center=(500, 800))

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self, player):
        a = PlagueUpgraded()
        player.deck.append(a)
        player.deck.remove(self)

    def play(self, player, monster):
        dmg = 0
        if player.energy >= self._price:
            player.energy -= self._price
            player.hand.remove(self)
            if monster.effects["weakness"] > 0:  # weakness
                dmg += 5
            if monster.effects["fire"] > 0:  # power
                dmg += 5
            if monster.effects["disarm"] > 0:  # disarm
                dmg += 5
            if monster.effects["blind"] > 0:  # blind
                dmg += 5
            tmp = monster.makeDamage(dmg)
            if tmp:
                return 2
            return 1
        return 0


class PlagueUpgraded(Card):
    def __init__(self):
        super(PlagueUpgraded, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 2
        self.type = "Attack"
        self.upgraded = True
        self._canBeUpgraded = False
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/Plague+.png").convert_alpha(),
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
        dmg = 0
        if player.energy >= self._price:
            player.energy -= self._price
            player.hand.remove(self)
            if monster.effects["weakness"] > 0:  # weakness
                dmg += 8
            if monster.effects["fire"] > 0:  # power
                dmg += 8
            if monster.effects["disarm"] > 0:  # disarm
                dmg += 8
            if monster.effects["blind"] > 0:  # blind
                dmg += 8
            tmp = monster.makeDamage(dmg)
            if tmp:
                return 2
            return 1
        return 0

class BrainOverflow(Card):
    def __init__(self):
        super(BrainOverflow, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 1
        self.type = "Utility"
        self.upgraded = False
        self._canBeUpgraded = True
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/BrainOverflow.png").convert_alpha(), (148,234))
        self.rect = self.image.get_rect(
            center=(500, 800))

    def getPrice(self) -> int:
        return self._price

    def canBeUpgraded(self) -> bool:
        return self._canBeUpgraded

    def upgrade(self, player):
        a = BrainOverflowUpgraded()
        player.deck.append(a)
        player.deck.remove(self)

    def play(self, player, monster):
        start = 800
        cards = getThreeCards()

        for i in cards:
            player.hand.append(i)

        player.hand.remove(self)
        for a in player.hand:  # 1920 - длина области, ширина будет 200
            a.rect = a.image.get_rect(center=(start, 941))
            start += 150
        return 1

class BrainOverflowUpgraded(Card):
    def __init__(self):
        super(BrainOverflowUpgraded, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self._price = 0
        self.type = "Utility"
        self.upgraded = True
        self._canBeUpgraded = False
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/Cards/BrainOverflow+.png").convert_alpha(),
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
        start = 800
        cards = getThreeCards()

        for i in cards:
            player.hand.append(i)

        player.hand.remove(self)
        for a in player.hand:  # 1920 - длина области, ширина будет 200
            a.rect = a.image.get_rect(center=(start, 941))
            start += 150
        return 1
