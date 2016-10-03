#!/usr/bin/env python
# -*- coding: utf-8 -*-


#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Filnamn: sokoban.py
## 2016-10-03s Sokrates Lamprou
## IP1, Linköpings universitet
## Kurs: TDP002 (Eric Elfving)

"""
------------- Card MODULE--------------------------------
Creates a card and methods for cards.
----------------------------------------------------------------
"""

def create_card(color, value):
    return (color, value)

def display_card(card):
    if card[0] == 1:
        display_card = str(card[1])+" "+ "of Hearts"
        return display_card
    elif card[0]==2:
        display_card = str(card[1])+" "+ "of Spades"
        return display_card

def get_suit(card):
    return card[0]

def get_value(card):
    return card[1]
