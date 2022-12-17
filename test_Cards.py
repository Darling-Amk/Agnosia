import math
import sys
sys.path.insert(1,'Scenes')

import pygame

import Cards
from Classes import Player, Goblin

screen = pygame.display.set_mode((1920,1080))

def test_Attack_play():
    player = Player()
    player.endTurn(1)
    monster = Goblin(player)
    card = Cards.Attack()
    player.hand.append(card)
    hp1 = monster.health
    card.play(player,monster)
    assert monster.health < hp1

def test_Shield_play():
    player = Player()
    player.endTurn(1)
    monster = Goblin(player)
    card = Cards.Shield()
    player.hand.append(card)
    block1 = player.block
    card.play(player, monster)
    assert player.block > block1

def test_EnBurst_play():
    player = Player()
    player.endTurn(1)
    monster = Goblin(player)
    card = Cards.EnBurst()
    player.hand.append(card)
    player.energy -=2
    en1 = player.energy
    card.play(player, monster)
    assert player.energy > en1

def test_CounterStrike_play():
    player = Player()
    player.endTurn(1)
    monster = Goblin(player)
    card = Cards.CounterStrike()
    card2 = Cards.Shield()
    card3 = Cards.Shield()
    player.hand.append(card)
    player.hand.append(card2)
    player.hand.append(card3)
    hp1 = monster.health = player.energy
    card2.play(player, monster)
    card3.play(player, monster)
    card.play(player, monster)
    assert monster.health + int(player.block/2) == hp1