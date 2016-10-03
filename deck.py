#!/usr/bin/env python
# -*- coding: utf-8 -*-


## Filnamn: deck.py
## 2016-10-02 Sokrates Lamprou
## IP1, Linköpings universitet
## Kurs: TDP002 (Eric Elfving)

"""
-------------DECK MODULE----------------------------------------
Creates a deck of cards and methods that interact with the deck.
----------------------------------------------------------------
"""

import random
from card import *

def create_deck():
    global deck
    deck = [create_card(1, i) for i in range(1,14)]
    deck += [create_card(2, i) for i in range(14,27)]
    deck.append(("A", "J"))
    deck.append(("B","J"))
    return deck


def create_shuffled_deck():
    global deck
    deck = [(1,i) for i in range(1,14)]
    deck += [(2,i) for i in range(14,27)]
    shuffle=[]
    for i in deck:
        shuffle.insert(random.randint(1,27), i)
    return shuffle

def pick_card(deck):
    return random.choice(deck)

def insert_card(card, deck, position):
    if position == 1:
        position = 0
    else:
        position -= 1
    deck.insert(position,card)
    cards = ['deck', deck]
    return cards

def shuffle_cut(deck, value=1000):
    random.seed(value)
    random.shuffle(deck)
    shuffle = []
    shuffle = [i for i in deck[13:28]]
    shuffle += [i for i in deck[0:13]]
    return shuffle

def remove_card(position, deck):
    if position == 1:
        position = 0
    else:
        position -= 1
    deck.pop(position)
    return deck

def change_position(position, card, deck):

    for i in deck:
        if i == card:
            deck.remove(card)
    if position == 0:
        position = 0
    if position == 1:
        position = 0
    else:
        position -= 1
    deck.insert(position, card)
    return deck

def get_position(card, deck):
    position = 0
    if card not in deck:
        print("Error message: Card not in deck")
    for i in deck:
        if i == card:
            return position
        else:
            position += 1

def find_joker_pos(deck):
    positions = []
    count = 0
    for card in deck:
        if card[0] == "A" and card[1] =="J":
            count +=1
            positions.append(count)
        elif card[0] == "B" and card[1] =="J":
            count +=1
            positions.append(count)
        else:
            count += 1
    positions[0] -= 1
    return positions

def get_value_position(position, deck):
    count = 0
    for i in deck:
        if position == count:
            return i[1]
        else:
            count += 1
