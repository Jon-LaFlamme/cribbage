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
                if index in range(0,len(deck.deck)-1):
                    invalid = False    
                else:
                    print('Invalid selection. Please try again.')
        else:
            index = random.randint(0,len(deck.deck))
        deck.cut(index)
        


    def display_hand(self,is_numbered):
        i = 0
        for card in self.hand:
            if is_numbered:
                i += 1
                print(f'{i}) {card.name} ')
            else:
                print(f'|| {card.name} ')

    def user_input(self):
        discards = []
        indices= []
        while len(self.hand) - len(indices) > 4:
            invalid = True
            while invalid:
                index = int(input('Make your discard selection: ')) - 1
                if index in range(0,len(self.hand)):
                    invalid = False
                    indices.append(index)
                else:
                    raise('Index Error: Please select a valid index.')
        for index in indices:
            discards.append(self.hand[index])
        for card in discards:
            self.hand.remove(card)
        return discards

    def auto_discard_easy(self):
        discards = []
        while len(self.hand) > 4:
            discards.append(self.hand.pop(random.randint(0,3)))
        return discards

    def auto_discard_intermediate(self):
        #TODO(Jon) Develop intermediate selection algorithm. Till then redirect to easy
        return self.auto_discard_easy()

    def auto_discard_difficult(self):
        #TODO(Jon) Develop difficult selection algorithm. Till then redirect to easy
        return self.auto_discard_easy()

    def auto_input(self):
        if self.difficulty == 'easy':
            return self.auto_discard_easy()
        elif self.difficulty == 'intermediate':
            return self.auto_discard_intermediate()
        else:
            return self.auto_discard_difficult()

    def discard(self):
        if self.is_human:
            return self.user_input()
        else:
            return self.auto_input()

class human(player):
    """human
    Attributes:
        self.name set with string argument
    """
    def __init__(self, name = None):
        super().__init__()
        if name:
            self.name = name
        
class computer(player):

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

   

        

