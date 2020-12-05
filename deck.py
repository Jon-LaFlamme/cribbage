from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import random

"""A simple deck of playing cards.

Card() maintains multiple string and integer properties for easy comparisons.
Deck() maintains a list of playing cards that can be shuffled, dealt and cut. 

    Typical Usage Example:

    d = Deck()
    d.shuffle() 
    d.cut()
    peeked_card = d.peek(index)
    removed_card = d.deal_one()

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

    Local Variables:
        _ranks is a dictionary mapping rankname strings to integer rank values
        _suits is a list of strings indicating suits
        _values is a dictionary mapping rankname strings to special integer values
    
    Attributes:
        self.deck: the list containing all playing cards

    Methods:
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
        _low_list = []
        _hi_list = []
        try:
             _low_list = self.deck[0:pivot]
             _hi_list = self.deck[pivot:len(self.deck)-1]
             self.deck = _hi_list.extend(_low_list)
        except ValueError:
            print("ERROR: Index out of range")

    def peek(self,index):
        try:
            card = self.deck[index]
        except ValueError:
            print("ERROR: Index out of range")
        return card
        
    def shuffle(self):
        print(len(self.deck))
        self.cut(random.randint(0,len(self.deck)-1))
        self.cut(random.randint(0,len(self.deck)-1))
        self.cut(random.randint(0,len(self.deck)-1))
        random.shuffle(self.deck)
        self.cut(random.randint(0,len(self.deck)-1))
        self.cut(random.randint(0,len(self.deck)-1))
        self.cut(random.randint(0,len(self.deck)-1))
        random.shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop()



def test_deck_constructor():        #Test1 52-card Deck constructor validation
    print("---------  TEST Deck Constructor -------------\n")
    deck = Deck()
    print(f'- Length of deck is: {len(deck.deck)}\n')
    for card in deck.deck:
        print(f'- {card.name}')

def test_deck_shuffle():            #test deck.shuffle() method, dependency on deck.cut() method
    print("---------  TEST Deck Shuffle -------------")
    deck = Deck()                   #expected output should appear sufficiently randomized, with minimal clustering
    deck.shuffle()
    for card in deck.deck:
        print(card.name)

def test_card_properties():            #Test2 Card property validation
    print("---------  TEST Card Properties -------------")
    deck = Deck()                      #expected face card values = 10, expected ranks 1-13
    for card in deck.deck:
        print(f'Card name: {str(card.name)},   Card value: {str(card.value)},   Card rank: {str(card.rank)}')



if __name__ == "__main__":
    """ This is executed when run from the command line """
    #test_deck_constructor()
    #test_card_properties()
    test_deck_shuffle()

