from enum import Enum
from random import shuffle
import pygame


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


class Effect(Enum):
    weakness  = 1
    blind  = 2
    fire  = 3
    disarm  = 4
    power = 5


class Creature():
    def __init__(self):
        self.effects = set()
        self.health  = None

    def makeDamage(self,damage:int)->bool:
        self.health-=damage
        return self.health<=0

    def makeEffect(self,effect:Effect)->None:
        self.effects.add(effect)


class Player(Creature):
    def __init__(self):
        # Конструктор родителя
        super(Player, self).__init__()
        self.artifacts = []
        self.deck = []
        self.hand = []
        self.draw = []
        self.energy = 3

    def restart(self):
        self.artifacts = []
        self.deck = []
        self.hand = []
        self.draw = []
        self.energy = 3
        print("hio")

    def endTurn(self):
        self.energy = 3
        self.hand.clear()
        if len(self.draw) == 0:
            self.draw = self.deck
            shuffle(self.draw)
        for i in range(4):
            self.hand.append(self.draw.pop())


class phase(Enum):
    beforeFight = 1
    beforeTurn = 2
    afterTurn = 3
    afterDamage = 4


class Artifact():
    def __init__(self,phase_type:phase):
        self._phase_type : phase = phase_type

    def  getType(self)-> phase:
        return self._phase_type

    def use(self)->None:
        pass


class Event():
    def __init__(self):
        # Я хуй знает что он хотел этим сказать но надо переделать
        self.ui = None
    def launch(self, player:Player)->bool:
        pass


class Monster(Creature,Event):
    def __init__(self):
        super(Monster, self).__init__()

    def turn(self)->None:
        pass

class Treasure(Event):
    def __init__(self):
        pass

class RandomEvent(Event):
    def __init__(self):
        pass

class Camp(Event):
    def __init__(self):
        pass
        