import math

import pygame

import Cards
from Classes import Player

screen = pygame.display.set_mode((1920,1080))

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

