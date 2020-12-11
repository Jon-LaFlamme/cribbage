from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import names
import random

class player():
    """Player

    Attributes:
        self.name: a string of player's name
        self.record: a dictionary of wins, losses, etc.
        self.score: int of a player's current score.
        self.is_human: a boolean representation of sentience
        self.hand: a list of cards

    Methods:
        self.cut_deck(self,deck)                            Cuts deck in place
        self.display_hand(self,is_numbered)                 is_numbered True when input is required
        self.discard(self,num_discards)                     -> routes, to correct method, ret discards popped from self.hand 
        self.update_score(self)                             updates player score

        TODO(Jon):
        self.peg(self)

    """

    def __init__(self):
        self.name = 'DeLynn Colvert'
        self.record = {"wins": 0, "losses": 0}
        self.score = 0
        self.is_human = True
        self.hand = []

    def cut_deck(self,deck):
        if self.is_human:
            invalid = True
            while invalid:
                index = int(input(f'Select a number between 1 and {len(deck.deck)} to cut the deck: ')) - 1
                if index in range(0,len(deck.deck)):
                    invalid = False    
                else:
                    print('Invalid selection. Please try again.')
        else:
            index = random.randint(0,len(deck.deck)-1)
        deck.cut(index)
        
    def display_hand(self,is_numbered):
        i = 0
        for card in self.hand:
            if is_numbered:
                i += 1
                print(f'{i}) {card.name} ')
            else:
                print(f'|| {card.name} ')

    def discard(self,num_discards):
        if self.is_human:
            return self.user_discard(num_discards)
        else:
            if self.difficulty == 'easy':
                return self.auto_discard_easy(num_discards)
            elif self.difficulty == 'intermediate':
                return self.auto_discard_intermediate(num_discards)
            else:
                return self.auto_discard_difficult(num_discards)

    def update_score(self,num_points):
        if self.score + num_points > 121:
            self.score = 121
        else:
            self.score += num_points

class human(player):
    """human
    Attributes:
        self.name set with string argument

    Methods:
        self.user_discard(self,num_discards)                 -> ret discards poppedd from self.hand
    """
    def __init__(self, name = None):
        super().__init__()
        if name:
            self.name = name

        def user_discard(self,num_discards):
        discards = []
        indices= []
        while len(discards) < num_discards:     #supports 2 and 3-4 player discard rules with num_discards parameter
            invalid = True
            while invalid:
                index = int(input('Make your discard selection: ')) - 1
                if index in range(0,len(self.hand)-1) and index not in indices:
                    invalid = False
                    indices.append(index)
                    discards.append(self.hand[index])
                else:
                    print('Index Error: Please select a valid index.')
        for card in discards:
            self.hand.remove(card)
        return discards
        
class computer(player):
    """Player

    Methods:
        self.cut_deck(self,deck)                            Cuts deck in place
        self.auto_discard_easy(self,num_discards)            -> ret discards popped from self.hand
        self.auto_discard_intermediate(self,num_discards)    -> ret discards popped from self.hand
        self.auto_discard_difficult(self,num_discards)       -> ret discards popped from self.hand


        self.count(self)
        self.peg(self)                          
    """

    def __init__(self, difficulty):
        super().__init__()
        _difficulties = ['easy','intermediate','difficult']
        _gender = ['male','female']
        self.is_human = False
        self.name = f'{names.get_first_name(gender = random.choice(_gender))} (computer)'
        if difficulty in _difficulties:
            self.difficulty = difficulty
        else:
            self.difficulty = 'easy'

    def auto_discard_easy(self,num_discards):
        discards = []
        while len(discards) < num_discards:
            discards.append(self.hand.pop(random.randint(0,len(self.hand)-1)))
        return discards

    def auto_discard_intermediate(self,num_discards):
        #TODO(Jon) Develop intermediate selection algorithm. Till then redirect to easy
        #Intermediate selection algorithm to find optimal points for each hand
        return self.auto_discard_easy(num_discards)

    def auto_discard_difficult(self,num_discards):
        #TODO(Jon) Develop difficult selection algorithm. Till then redirect to easy
        #difficult selection algorithm to employ statistical learning to find optimal discards
        return self.auto_discard_easy(num_discards)

   

        

