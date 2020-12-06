from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import random

#TODO(Jon) Need to Deck.shuffle() method. Seems to be failing in an edge case

"""deck Module: A simple deck of playing cards.

Card() maintains multiple string and integer properties for easy comparisons.
Deck() maintains a list of playing cards that can be shuffled, dealt and cut. 

    Typical Usage Example:

    d = Deck()                      #Constructor
    d.shuffle()                     #In-place custom deck shuffling method
    d.cut()                         #In-place spitting and reordering of deck
    peeked_card = d.peek(index)     #Copies card at index, does not change deck
    popped_card = d.deal_one()      #list pop

    for card in deck.deck: print(card.name)
    print(removed_card.suit)
    print(removed_card.name)
    peeked_card.rank >= removed_card.rank
"""

class Card():
    """Playing card

    Attributes:
        self.suit: a string of the card's suit
        self.rank: an integer of the card's rank
        self.value: an integer of the card's value
        self.rankname: a string of the card's rankname
        self.name: a string representation of the card
    """

    def __init__(self, suit, rank, value, rankname):
        self.suit = suit
        self.rank = rank
        self.value = value
        self.rankname = rankname
        self.name = f"{rankname} of {suit}"


class Deck():
    """Builds a standard 52-card deck of cards

    Private Variables:
        _ranks is a dictionary mapping rankname strings to integer rank values
        _suits is a list of strings indicating suits
        _values is a dictionary mapping rankname strings to special integer values
        _deck is a temporary list used to build self.deck attribute
    
    Public Attributes:
        self.deck: the list containing all playing cards

    Public Methods:
        deck.cut(pivot_index) swaps the lower and upper parts of a deck around a pivot
    """

    def __init__(self):
        _ranks = {'ace':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
            'nine':9,'ten':10,'jack':11,'queen':12,'king':13}
        _suits = ['hearts','diamonds','spades','clubs']
        _values = {'ace':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
            'nine':9,'ten':10,'jack':10,'queen':10,'king':10}
        _deck = []

        for suit in _suits:
            for rank in _ranks:
                _deck.append(Card(suit,_ranks[rank],_values[rank],rank))
        self.deck = _deck

    def cut(self,pivot):
        _low = []
        _hi = []
        try:
            self.deck[pivot]    #only to trigger exception for index out of bounds errors
            _low = self.deck[:pivot]
            _hi = self.deck[pivot:]
            _hi.extend(_low)
            self.deck = _hi      
        except ValueError:
            print("ERROR: Index out of range")

    def peek(self,index):
        try:
            card = self.deck[index]
        except ValueError:
            print("ERROR: Index out of range")
        return card
        
    def shuffle(self):
        random.shuffle(self.deck)
        for i in range(int(len(self.deck)/2)):
            self.cut(random.randint(0,len(self.deck)-1))
        random.shuffle(self.deck)
        for i in range(int(len(self.deck)/2)):
            self.cut(random.randint(0,len(self.deck)-1))
        random.shuffle(self.deck)

    def deal_one(self):
        if self.deck:
            return self.deck.pop()
        else:
            raise IndexError('ERROR: Deck is empty')