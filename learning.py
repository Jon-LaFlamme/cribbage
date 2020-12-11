import deck
import players
import hand
from itertools import combinations

suits = ['clubs','diamonds','hearts','spades']
values = {'ace':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
            'nine':9,'ten':10,'jack':10,'queen':10,'king':10}

#template: {"hand_id": 
#               {"times_played":int,
#                "times_dealer":int,
#                "neg_peg_pts_cum":-int,
#                "pos_peg_pts_cum":int,
#                "hand_points_cum":int, 
#                "neg_crib_pts_cum":-int,
#                "pos_crib_pts_cum"+int}, 
#           ... }
#notes: averages for different stats can be computed at runtime based on the situation
# TODO(Jon) Optional: Make 'insane' difficulty, which stores the performance of each hand against every other hand
# TODO(Jon) Optional: Also with 'insane' difficulty, store id as turncard_rank + played_cards_concatenated as rank_id_string
#           Computer can loop through each card in hand to find matching ids and select best option
#           Example: {"jacacetwothrfou": 3}
#expected about 50,000 unique IDs after many iterations.


performance_by_hand = {}
dealer_performance_by_hand = {}


# First map a value from 1-52 for each card in the deck. (eg {'acc':1,'acd':2,'ach':3,'acs':4,'twc':5, ....})
i = 1
id_ranks = {}
for value in values.keys():
    for suit in suits:
        id_ranks[suit[:2] + suit[0]] = i
        i += 1

# This function takes a hand as input and based on id_ranks, creates and returns a correcly oredered unique hand id as a string
# This resolves the issue of redundant permutations of the same combination of cards in a hand
def hand_id(hand):
    ids = {}
    for card in hand:
        ids[card.id] = id_ranks[card.id]
    ordered_hand_id = sorted(ids.items(), key=lambda x: x[1])
    return f'{ordered_hand_id[0][0]}{ordered_hand_id[1][0]}{ordered_hand_id[2][0]}{ordered_hand_id[3][0]}'

#strategy is one of maximization of points and is blind to other bot's cards with zero statistical adjustments
def peg_logic(hand_playing,stack,count,turncard):
    h = hand.Hand(hand_playing,turncard)
    return h.peg_selection(stack,count,turncard)

def can_play(hand,count):
    for card in hand:
        if card.value + count <= 31:
            return True
    return False

def peg_sequence(is_dealer_p1,turncard,p1,p2):
    hand1 = p1.hand.copy()
    hand2 = p2.hand.copy()
    while hand1 or hand2:
        count = 0
        stack = []
        p1_turn = True
        while count <= 31 and (can_play(hand1,count) or can_play(hand2,count)):
            if p1_turn and can_play(hand1,count):
                choice = peg_logic(hand1,stack,count,turncard)
                count += choice.value
                stack.append(choice)
                hand1.remove(choice)
                p1_turn = False
            if can_play(hand2,count):
                choice = peg_logic(hand2,stack,count,turncard)
                count += choice.value
                stack.append(choice)
                hand2.remove(choice)
                p1_turn = True
            


                








p1 = players.computer('difficult')
p2 = players.computer('difficult')
num_rounds = 10
d = deck.Deck()
d.shuffle()
is_dealer_p1 = True

for round in range(num_rounds):
    hand1 = []
    hand2 = []
    for card in range(6):
        hand1.append(d.deal_one())
        hand2.append(d.deal_one())
    p1_options = list(combinations(hand1,4))
    p2_options = list(combinations(hand2,4))
    p1.cut_deck(d)
    turncard = d.deck[0]
    for p1_hand,p2_hand in zip(p1_options,p2_options):
        crib = []
        p1.hand = p1_hand
        p2.hand = p2_hand
        #extract the crib
        for card in hand1:
            if card not in p1.hand:
                crib.append(card)
        for card in hand2:
            if card not in p2.hand:
                crib.append(card)
        #TODO(Jon) Create the following gameplay sequences
        peg_sequence(is_dealer_p1,turncard,p1,p2)
        show_sequence(is_dealer_p1,d,crib,p1,p2)









    







'''
#TODO(Jon)
Basic idea here is to play n number of rounds of computer vs computer and update scores in dictionaries.
One dictionary records the statistics for discarding as a dealer
The other dictionaary records the statistics for discarding as a non-dealer
Should essentially be constant time lookup at runtime, much faster than the intermediate strategy of computing scores first

Both computer players will be using the same decisions hueristics
They will be able to see each other's cards so as to give accurate data for hand performance
'''

