import deck
import gameplay

suits = ['clubs','diamonds','hearts','spades']
values = {'ace':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
            'nine':9,'ten':10,'jack':10,'queen':10,'king':10}

#template: {"hand_id" {"peg_pts":int, "hand_points":int, "crib_pts":+/-int, "times_played":int. "avg_score":+/-int, }, ... }
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

'''
#TODO(Jon)
Basic idea here is to play n number of rounds of computer vs computer and update scores in dictionaries.
One dictionary records the statistics for discarding as a dealer
The other dictionaary records the statistics for discarding as a non-dealer
Should essentially be constant time lookup at runtime, much faster than the intermediate strategy of computing scores first

The other task is implementing a peg learning module that has probabilities for pegging choices at each decision point
This could and should probably be done concurrently with the discard learning module
'''

