#!/usr/bin/env python
# -*- coding: utf-8 -*-


## Filnamn: solitaire.py
## 2016-10-03 Sokrates Lamprou
## IP1, Linköpings universitet
## Kurs: TDP002 (Eric Elfving)

"""
-------------Solitaire keystream--------------------------------
This program encrypt a deck of carda according to the solitaire algorithm developed by Bruce Schneider. 
----------------------------------------------------------------
"""

from deck import *
import random


def solitaire_keystream(length, deck):
    global stream
    stream = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,'G': 7,
         'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
         'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
         'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    
    output_string = ""
    
    while len(output_string) < length:
        
        # Joker A
        position = get_position(("A", "J"), deck)
        deck_length = len(deck) -1 
        if (position) == deck_length:
            change_position(1, ("A", "J"), deck)
        else:
            position += 2
            change_position(position, ("A", "J"), deck)

        #Joker B
        position = get_position(("B", "J"), deck)
        deck_length = len(deck)
        position += 1
        if (position) == deck_length:
            change_position(3, ("B", "J"), deck)
        elif (position) == (deck_length-1):
            change_position(2, ("B", "J"), deck)
        else:
            position += 3
            change_position(position, ("B", "J"), deck)

        #steg 4
        jokers_pos = find_joker_pos(deck)
        A = deck[0:jokers_pos[0]]
        B = deck[jokers_pos[0]:jokers_pos[1]]
        C = deck[jokers_pos[1]:28]

        deck = [i for i in C]
        deck += [i for i in B]
        deck += [i for i in A]
        #steg 5
        last_card = deck[-1][1]
        bottom_cards = deck[0:last_card]
        deck[0:last_card] = []
        last = deck[-1]
        deck.remove(last)
        
        for i in bottom_cards:
            deck.append(i)
        deck.append(last)
        #steg 6
        key = deck[0][1]
        stream_value = get_value_position(key, deck)
        
        for item,value in stream.items():
            if stream_value == value:
                output_string += item
            else:
                continue
    return output_string

def convert(message):
    """ Converts a message to small letters and replaces tokens that are not in the alphabet"""
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in message:
        if i.lower() not in alphabet:
            message = message.replace(i, "")
    return message.upper()
            

def int_convert(message):
    """ Converts a message to integers"""
    stream = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,'G': 7,
         'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
         'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
         'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    nums = []
    for letter in message:
        for k,v in stream.items():
            if letter == k:
                nums.append(v)
    return nums

def string_convert(message):
    """ Converts a message to strings"""
    stream = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,'G': 7,
         'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
         'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
         'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    strings = ""
    for num in message:
        for k,v in stream.items():
            if num == v:
                strings += k
    return strings
        

    
def summa(message1, message2):
    """ Add numbers from one message with the numbers
in the second message. If the sum of the numbers > 26, then 26 will be removed. """  
    listan = []
    for num, val in enumerate(message1):
        listan.append(message1[num]+message2[num])
    final = []
    for num in listan:
        if num > 26:
            final.append(num-26)
        else:
            final.append(num)
    return final

def decrypt_summa(message1, message2):
    """ Subtract the numbers from M1 from the nubmers
        in M2 and adds 26 if the numbers together in the messages is < 26."""
    listan = []
    for num, val in enumerate(message1):
        listan.append(message1[num]-message2[num])
    final = []
    for num in listan:
        if num < 1:
            final.append(num+26)
        else:
            final.append(num)
    return final

def solitaire_encrypt(message, deck_in):
    """ Encrypt a message """
    deck = deck_in.copy()
    deck = shuffle_cut(deck)

    #Steg 1
    message = convert(message)
    #Steg 2
    encrypt = solitaire_keystream(len(message), deck)
    #Steg 3
    message = int_convert(message)
    #Steg 4
    encrypt = int_convert(encrypt)
    #Steg 5
    total = summa(message, encrypt)
    total = string_convert(total)
    return total

def solitaire_decrypt(secret_message, deck_in):
    """ Decrypt a message """
    deck = deck_in.copy()
    deck = shuffle_cut(deck)
    
    #Steg 1
    secret_message = int_convert(secret_message)
    #Steg 2
    decrypt = solitaire_keystream(len(secret_message), deck)
    #Steg 3
    decrypt = int_convert(decrypt)
    #Steg 4
    final = decrypt_summa(secret_message, decrypt)


    final = string_convert(final)
    return final
    
