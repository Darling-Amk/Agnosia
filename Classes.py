from enum import Enum
from random import shuffle
import random
import pygame
import Cards
import random


class Scene:
    def __init__(self,screen,name,change,bg_image="Agnosia_assets/Agnosia_background_main_menu.png"):
        self.bg = pygame.image.load(bg_image)
        self.change = change
        self.name = name
        self.screen = screen
    def draw(self,state):
        pass

    @staticmethod
    def draw_text(surface, text, x, y, font, color=(255, 255, 255)):
        surface.blit(font.render(f'{text}', True, color), (x, y))

class Effect(Enum):
    weakness  = 1
    blind  = 2
    fire  = 3
    disarm  = 4
    power = 5


class Creature(pygame.sprite.Sprite):
    def __init__(self):
        super(pygame.sprite.Sprite, self).__init__()
        self.effects = {"weakness": 0, "blind": 0, "fire": 0, "disarm": 0, "power": 0}
        self.health = None
        self.healthMax = None
        self.block = None

    def makeDamage(self,damage:int, player)->bool:
        if damage == 0:
            pass
        elif self.block > damage:
            self.block-=damage
            player.addToLog(f"{type(self).__name__} got {damage} dealt to it's shield")
        elif self.block == 0:
            self.health-=damage
            player.addToLog(f"{type(self).__name__} got {damage} dealt to it")
        else:
            damage-=self.block
            self.block = 0
            self.health -= damage
            player.addToLog(f"{type(self).__name__} got it's shield broken and got {damage} dealt to it")
        return self.health<=0

    def heal(self,number:int,player):
        start = self.health
        self.health += number
        if self.health > self.healthMax:
            self.health = self.healthMax
        player.addToLog(f"{type(self).__name__} got healed for {self.health-start} health")

    def gainBlock(self, block:int, player):
        self.block += block
        player.addToLog(f"{type(self).__name__} got {block} block")

    def makeEffect(self,effect:str, length:int,player)->None:
        self.effects[effect] += length
        player.addToLog(f"{type(self).__name__} got effect:\"{effect}\"")


class Player(Creature):
    def __init__(self):
        # Конструктор родителя
        super(Player, self).__init__()
        self.healthMax = 100
        self.health = 100
        self.block = 0
        self.artifacts = []
        self.deck = []
        self.hand = []
        self.draw = []
        self.energyMax = 3
        self.energy = 3
        self.handNumber = 0
        self.log = []
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/agnosia_gg.png").convert_alpha(), (205, 300))
        self.rect = self.image.get_rect(
            center=(300, 500))
        x = Cards.Attack()
        for a in range(4):
            self.deck.append(x)
            x = Cards.Attack()
        x = Cards.Shield()
        for a in range(4):
            self.deck.append(x)
            x = Cards.Shield()
        x = Cards.UnexpectedMove()
        self.deck.append(x)


    def restart(self):
        self.artifacts = []
        self.deck = []
        self.hand = []
        self.draw = []
        self.healthMax = 100
        self.health = 100
        self.block = 0
        self.energyMax = 3
        self.energy = 3
        x = Cards.Attack()
        for a in range(4):
            self.deck.append(x)
            x = Cards.Attack()
        x = Cards.Shield()
        for a in range(4):
            self.deck.append(x)
            x = Cards.Shield()
        x = Cards.UnexpectedMove()
        self.deck.append(x)

    def endTurn(self, ok):
        self.energy = self.energyMax
        self.hand.clear()
        if self.effects["fire"]>0: # fire
            self.makeDamage(5, self)
        for eff in self.effects:
            if self.effects[eff]>0:
                self.effects[eff]-=1
        for i in range(4):
            if len(self.draw) == 0:
                self.draw = self.deck.copy()
                for j in self.hand:
                    if self.draw.__contains__(j):
                        self.draw.remove(j)
                shuffle(self.draw)
            self.hand.append(self.draw.pop())
        self.showHand(0)
        if(ok != 1):
            self.addToLog("--It's now monsters turn--")
            ok.turn()
            self.addToLog("--It's now players turn--")
        self.block = 0

    def rest(self):
        self.health += int(self.healthMax*0.3)
        if self.health > self.healthMax:
            self.health = self.healthMax

    def getRandomCard(self):
        card = Cards.getThreeCards()[0]
        self.deck.append(card)

    def gainEnergy(self,number:int):
        self.energy += number
        self.addToLog(f"{type(self).__name__} got {number} energy")

    def showHand(self, minNumber:int):
        if minNumber + 4 > len(self.hand):
            minNumber = 0
        if minNumber < 0:
            return
        start = 800
        counter = 0
        for a in self.hand:  # 1920 - длина области, ширина будет 200
            counter += 1
            if minNumber < counter <= minNumber + 4:
                if counter > len(self.hand):
                    break
                a.rect = a.image.get_rect(center=(start, 928))
                start += 150
            else:
                a.rect = a.image.get_rect(center=(start, -1000))
        self.handNumber = minNumber

    def addToLog(self, line:str):
        if len(self.log) > 7:
            self.log.pop(0)
        self.log.append(line)





class phase(Enum):
    beforeFight = 1
    beforeTurn = 2
    afterTurn = 3
    afterDamage = 4


class Artifact():
    def __init__(self,phase_type:phase):
        self._phase_type : phase = phase_type

    def getType(self)-> phase:
        return self._phase_type

    def use(self)->None:
        pass


class Event():
    def __init__(self):
        # Я хуй знает что он хотел этим сказать но надо переделать
        self.ui = None
    def launch(self, player:Player)->bool:
        pass




class Monster(Creature, Event):
    def __init__(self, player):
        super(Monster, self).__init__()
        pygame.sprite.Sprite.__init__(self)

    def turn(self)->None:
        pass

class Treasure(Event):
    def __init__(self, player):
        pass

class RandomEvent(Event):
    def __init__(self, player):
        pass

class Camp(Event):
    def __init__(self, player):
        pass

def chooseMonster(p):
    arr = [Goblin(p), Vampire(p), Phoenix(p), Dragon(p)]
    rnd = random.randrange(0, len(arr))
    return arr[rnd]

class Goblin(Monster):
    def __init__(self, player):
        # Конструктор родителя
        super(Goblin, self).__init__(player)
        self.health = 50
        self.healthMax = 50
        self.block = 0
        self.damage = 7
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/agnosia_monster4.png").convert_alpha(),
                                            (205, 300))
        self.rect = self.image.get_rect(
            center=(1620, 500))
        self.player = player


    def turn(self) -> None:
        dmg = self.damage
        if self.effects["weakness"]>0: #weakness
            dmg = int(dmg*0.75)
        if self.effects["power"]>0: #power
            dmg = int(dmg * 1.25)
        if self.effects["disarm"]>0: #disarm
            dmg = 0
        if self.effects["blind"]>0: #blind
            dmg = int(dmg*0.75)
        if self.effects["fire"]>0: # fire
            self.makeDamage(5,self.player)
        self.player.makeDamage(dmg, self.player)
        a = random.randint(0, 5)
        if a == 2:
            self.player.makeEffect("disarm", 1,self.player)
        self.heal(5,self.player)
        for eff in self.effects:
            if self.effects[eff]>0:
                self.effects[eff]-=1


class Vampire(Monster):
    def __init__(self, player):
        # Конструктор родителя
        super(Vampire, self).__init__(player)
        self.health = 20
        self.healthMax = 20
        self.block = 0
        self.damage = 7
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/agnosia_monster1.png").convert_alpha(),
                                            (205, 300))
        self.rect = self.image.get_rect(
            center=(1620, 500))
        self.player = player

    def turn(self) -> None:
        dmg = self.damage
        if self.effects["weakness"]>0: #weakness
            dmg = int(dmg*0.75)
        if self.effects["power"]>0: #power
            dmg = int(dmg * 1.25)
        if self.effects["disarm"]>0: #disarm
            dmg = 0
        if self.effects["blind"]>0: #blind
            dmg = int(dmg*0.75)
        if self.effects["fire"]>0: # fire
            self.makeDamage(5,self.player)
        self.player.makeDamage(dmg,self.player)
        self.player.makeEffect("blind", 1, self.player)
        self.heal(5,self.player)
        for eff in self.effects:
            if self.effects[eff]>0:
                self.effects[eff]-=1

class Phoenix(Monster):
    def __init__(self, player):
        # Конструктор родителя
        super(Phoenix, self).__init__(player)
        self.health = 30
        self.healthMax = 30
        self.block = 0
        self.damage =7
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/agnosia_monster2.png").convert_alpha(),
                                            (205, 300))
        self.rect = self.image.get_rect(
            center=(1620, 500))
        self.player = player

    def turn(self) -> None:
        dmg = self.damage
        if self.effects["weakness"]>0: #weakness
            dmg = int(dmg*0.75)
        if self.effects["power"]>0: #power
            dmg = int(dmg * 1.25)
        if self.effects["disarm"]>0: #disarm
            dmg = 0
        if self.effects["blind"]>0: #blind
            dmg = int(dmg*0.75)
        if self.effects["fire"]>0: # fire
            self.makeDamage(5,self.player)
        self.player.makeDamage(dmg,self.player)
        self.player.makeEffect("power", 1,self.player)
        self.makeEffect("fire", 2,self.player)
        for eff in self.effects:
            if self.effects[eff]>0:
                self.effects[eff]-=1


class Dragon(Monster):
    def __init__(self, player):
        # Конструктор родителя
        super(Dragon, self).__init__(player)
        self.health = 70
        self.healthMax = 70
        self.block = 0
        self.damage = 7
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/agnosia_monster3.png").convert_alpha(),
                                            (205, 300))
        self.rect = self.image.get_rect(
            center=(1620, 500))
        self.player = player

    def turn(self) -> None:
        dmg = self.damage
        if self.effects["weakness"]>0: #weakness
            dmg = int(dmg*0.75)
        if self.effects["power"]>0: #power
            dmg = int(dmg * 1.25)
        if self.effects["disarm"]>0: #disarm
            dmg = 0
        if self.effects["blind"]>0: #blind
            dmg = int(dmg*0.75)
        if self.effects["fire"]>0: # fire
            self.makeDamage(5,self.player)
        self.player.makeDamage(dmg,self.player)
        self.player.makeEffect("blind", 2,self.player)
        self.player.makeEffect("fire", 1,self.player)
        a = random.randint(0, 5)
        if a == 2:
            self.player.makeEffect("weakness", 1,self.player)
        for eff in self.effects:
            if self.effects[eff]>0:
                self.effects[eff]-=1
