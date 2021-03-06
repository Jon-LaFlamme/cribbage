from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import names
import random
import hand
import users

class Player():
    """Player

    Attributes:
        self.name: a string of player's name
        self.record: a dictionary of wins, losses, etc.
        self.score: int of a player's current score.
        self.is_human: a boolean representation of sentience
        self.cards: a list of cards

    Methods:
        self.cut_deck(self,deck)                            Cuts deck in place
        self.display_hand(self,is_numbered)                 is_numbered True when input is required
        self.discard(self,num_discards)                     -> routes, to correct method, ret discards popped from self.cards 
        self.update_score(self)                             updates player score

        TODO(Jon):
        self.peg(self)

    """

    def __init__(self):
        self.name = 'DeLynn Colvert'
        self.score = 0
        self.is_dealer = False
        self.cards = []
         
    def display_hand(self, is_numbered=False):
        i = 0
        for card in self.cards:
            if is_numbered:
                i += 1
                print(f'{i}) {card.name} ')
            else:
                print(f'|| {card.name} ')

    def can_peg(self, count):
        for card in self.cards:
            if card.value + count <= 31:
                return True 
        return False


class Human(Player):
    """human
    Attributes:
        self.name set with string argument

    Methods:
        self.user_discard(self,num_discards)                 -> ret discards poppedd from self.cards
    """
    def __init__(self, name=None, user=None):
        super().__init__()
        if user:
            self.name = user.name
            self.user = user
        else:
            self.name = name
            self.user = None

    def cut_deck(self, deck=None, for_first_deal=False):
        invalid = True
        while invalid:
            index = input(f'Select a number between 1 and {len(deck.deck)} to cut the deck: ')
            if index != '':
                index = int(index) - 1
            if index in range(0,len(deck.deck)):
                invalid = False    
            else:
                print('Invalid selection. Please try again.')
        if for_first_deal:
            return deck.deck.pop(index)
        else:
            deck.cut(index)

    def discard(self, num_discards=2):
        discards = []
        indices= []
        while len(discards) < num_discards:     #supports 2 and 3-4 player discard rules with num_discards parameter
            invalid = True
            self.display_hand(is_numbered=True)
            while invalid:
                index = input('Make your discard selection: ')
                if index != '':
                    index = int(index) - 1
                if index in range(0,len(self.cards)) and index not in indices:
                    invalid = False
                    indices.append(index)
                    discards.append(self.cards[index])
                else:
                    print('Index Error: Please select a valid index.')
        for card in discards:
            self.cards.remove(card)
        print(f'-------------{self.name}\'s hand ------------' )
        self.display_hand()
        print(f'-------------{self.name}\'s discards ------------' )
        for card in discards:
            print(card.name)
        return discards

    def peg_one(self, stack=[], count=None, turncard=None):
        invalid = True
        while invalid:
            self.display_hand(is_numbered=True)
            index = input(f'Select a card to peg:')
            if index != '':
                index = int(index) - 1
            if index in range(0, len(self.cards)) and self.cards[index].value + count <= 31:
                return self.cards[index]
            else:
                print('Invalid selection. Please try again.')
        

class Computer(Player):
    """Player

    Methods:
        self.cut_deck(self,deck)                            Cuts deck in place
        self.auto_discard_easy(self,num_discards)            -> ret discards popped from self.cards
        self.auto_discard_intermediate(self,num_discards)    -> ret discards popped from self.cards
        self.auto_discard_difficult(self,num_discards)       -> ret discards popped from self.cards


        self.count(self)
        self.peg(self)                          
    """

    def __init__(self, difficulty='easy'):
        super().__init__()
        _difficulties = ['easy','medium','hard']
        _gender = ['male','female']
        self.name = f'{names.get_first_name(gender=random.choice(_gender))} (computer)'
        if difficulty in _difficulties:
            self.difficulty = difficulty
        else:
            self.difficulty = 'easy'


    def cut_deck(self, deck=None, for_first_deal=False):
        index = random.randint(0,len(deck.deck)-1)
        if for_first_deal:
            return deck.deck.pop(index)
        else:
            deck.cut(index)

    def peg_one(self, stack, count, turncard):
        h = hand.Hand(self.cards, turncard=turncard)
        return h.peg_selection(stack, count)

    def discard(self, num_discards=2, is_dealer=False):
        discards = []
        if self.difficulty == 'easy':
            while len(discards) < num_discards:
                discards.append(self.cards.pop(random.randint(0,len(self.cards)-1)))   
        elif self.difficulty == 'medium':
            h = hand.Hand(self.cards)
            selects = h.optimize_by_points(num_discards=num_discards)
            for card in self.cards:
                if card not in selects:
                    discards.append(card)
            for card in discards:
                self.cards.remove(card)
        elif self.difficulty == 'hard':
            h = hand.Hand(self.cards)
            selects = h.optimize_statistically(is_dealer)
            for card in self.cards:
                if card not in selects:
                    discards.append(card)
            for card in discards:
                self.cards.remove(card)
        return discards

   

        

