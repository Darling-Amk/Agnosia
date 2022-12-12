from enum import Enum
from random import shuffle
import pygame
import Cards


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
        self.effects = set()
        self.health = None

    def makeDamage(self,damage:int)->bool:
        self.health-=damage
        return self.health<=0

    def makeEffect(self,effect:Effect)->None:
        self.effects.add(effect)


class Player(Creature):
    def __init__(self):
        # Конструктор родителя
        super(Player, self).__init__()
        self.health = 100
        self.artifacts = []
        self.deck = []
        self.hand = []
        self.draw = []
        self.energy = 3
        self.image = pygame.transform.scale(pygame.image.load("Agnosia_assets/agnosia_gg.png").convert_alpha(), (205, 300))
        self.rect = self.image.get_rect(
            center=(300, 500))
        x = Cards.Attack()
        for a in range(4):
            self.deck.append(x)
            x = Cards.Attack()
        self.endTurn()

    def restart(self):
        self.artifacts = []
        self.deck = []
        self.hand = []
        self.draw = []
        self.energy = 3
        print("restarted player")

    def endTurn(self):
        start = 500
        self.energy = 3
        self.hand.clear()
        print(len(self.draw))
        for i in range(4):
            if len(self.draw) == 0:
                self.draw = self.deck.copy()
                shuffle(self.draw)
            self.hand.append(self.draw.pop())
        for a in self.hand:  # 1920 - длина области, ширина будет 200
            a.rect = a.image.get_rect(center=(start, 900))
            start += 200


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


class Monster(Creature, Event):
    def __init__(self):
        super(Monster, self).__init__()
        pygame.sprite.Sprite.__init__(self)

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
        