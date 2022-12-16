import math
import pytest
import pygame

import Cards
from Classes import Player,Goblin

screen = pygame.display.set_mode((1920,1080))
# Тест 1 (Сдача руки) (позитивный) [unit]
def test_end_turn_shuffles_hand():
    player = Player()
    player.endTurn(1)
    hand1 = player.hand.copy()
    player.endTurn(1)
    hand2 = player.hand.copy()
    player.endTurn(1)
    hand3 = player.hand.copy()
    a=[]
    b=[]
    c=[]
    for i in hand1:
        a.append(type(i).__name__)
    for i in hand2:
        b.append(type(i).__name__)
    for i in hand3:
        c.append(type(i).__name__)
    a.sort()
    b.sort()
    c.sort()
    assert (a == b and b == c) is False

def test_end_turn_gives_new_cards():
    player = Player()
    newCard = Cards.Burning()
    player.deck.append(newCard)
    handsToGet = math.ceil(len(player.deck)/4)
    a = []
    for i in range(handsToGet):
        player.endTurn(1)
        for card in player.hand:
            a.append(type(card).__name__)
    assert a.__contains__(type(newCard).__name__)

# Тест 2 (Связность графа) (позитивный) [unit] 
from GraphTest import generateGraph
from GraphTest import generateEvents
was = dict()
def dfs(v, g):
    was[v] = 1
    for i in g[v]:
        if not (i in was):
            dfs(v)

def graph_test():
    g = generateGraph()
    dfs("In", g)
    for i in g:
        assert(i in was) is True
    assert("Out" in was) is True
    g1 = generateGraph()
    assert(g1 == g) is False
    e = generateEvents(g, Player())    
    lst = Monster()
    for i in e:
        if i != lst:
            ok = 1
    assert(ok == 1) is True

# Тест 3 (Восполнение энергии) (позитивный) [unit]
def test_end_turn_energy_recovery():
    player = Player()
    player.energy = 0
    player.endTurn(1)
    assert player.energy==player.energyMax

# Тест 4 ("Лагерь": отдых) (позитивный) [unit]
def test_treat_after_camp():
    player = Player()
    player.health = 1
    player.rest()
    player.endTurn(1)
    assert player.health == 1 + int(player.healthMax * 0.3)

# Тест 9 ("Лагерь": отдых) (негативный) [unit]
def test_not_over_treat_after_camp():
    player = Player()
    player.health -= 1
    player.rest()
    player.endTurn(1)
    assert player.health <= player.healthMax

# Тест 3 (Монстр наносит урон) (позитивный) [unit]
def test_monster_damage_player():
    player = Player()
    safe_health = player.health
    monster = Goblin(player)
    player.endTurn(monster)
    assert player.health < safe_health
# Тест 6 (Тест эффекта огня: смерть) (позитивный) [unit]
def test_monster_death_after_fatal_player_damage():
    player = Player()
    monster = Goblin(player)
    monster.health = 1
    monster.makeEffect("fire",2,player)
    player.endTurn(monster)
    assert monster.health <= 0

# Тест 7 (Тест эффекта разоружения) (позитивный) [unit]
def test_no_damage_after_effect():
    player = Player()
    safe_health = player.health
    monster = Goblin(player)
    monster.makeEffect("disarm",1,player)
    player.endTurn(monster)
    assert safe_health == player.health

