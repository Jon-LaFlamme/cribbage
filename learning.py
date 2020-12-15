import deck
import players
import hand
from itertools import combinations

ranks = {'ace':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
    'nine':9,'ten':10,'jack':11,'queen':12,'king':13}
suits = ['clubs','diamonds','hearts','spades']

performance_by_hand = {}    
#template: {"hand_id": 
#               {"times_nodeal":int,
#                "times_dealer":int,
#                "dealer_neg_peg":-int,
#                "nodeal_neg_peg":-int,
#                "dealer_pos_peg":+int,
#                "nodeal_pos_peg":+int,
#                "hand_points":+int, 
#                "neg_crib_pts":-int,
#                "pos_crib_pts"+int}, 
#           ... }
# size = only 9,100 unique hand possibilities if abstracting the suits in hand_suit_signature

pegging_performance = {} 
# TODO(Jon) Store id as turncard_rank + played_cards_concatenated as rank_id_string
#           Computer can loop through each card in hand to find matching ids and select best option
#           Example: {"jacacetwothrfou": 3}
#expected about 50,000 unique IDs after many iterations.

# First map a value from 1-52 for each card in the deck. (eg {'acc':1,'acd':2,'ach':3,'acs':4,'twc':5, ....})


def hand_id_mapper(suits,ranks):
    deck_rank = 0
    id_ranks = {}
    for rank in ranks.keys():
        for suit in suits:
            deck_rank += 1
            id_ranks[f'{rank[:2]}{suit[0]}'] = deck_rank
    return id_ranks

#To compress posssibilities, 5 unique suit combinations are represented:
# 4d = 4 different suits; 3d = 3 different suits; 3s = 3 same suit; 2s = 2 of each; 4s = 4 same suit
def hand_suit_signature(a_hand):
    h = hand.Hand(a_hand)
    composition = []
    for key,value in h.suits.items():  
        composition.append(value)
    if len(composition) == 4:
        signature = "4d"
    elif len(composition) == 3:
        signature = "3d"
    elif len(composition) == 2:
        for k,v in h.suits.items():
            if v == 3:
                signature = "3s"
            elif v == 2:
                signature = "2s"
    else:
        signature = "4s"
    return signature
    

# This function takes a hand as input and based on id_ranks, creates and returns a correcly oredered unique hand id as a string
# This resolves the issue of redundant permutations of the same combination of cards in a hand
def hand_id(hand):
    signature = hand_suit_signature(hand)
    id_ranks = hand_id_mapper(suits,ranks)
    ids = {}
    ordered_hand_id = []
    for card in hand:
        ids[f'{card.name[:2]}{card.suit[0]}'] = id_ranks[f'{card.name[:2]}{card.suit[0]}']
    ordered_hand_id = sorted(ids.items(), key=lambda x: x[1], reverse=True)
    return f'{ordered_hand_id[0][0]}{ordered_hand_id[1][0]}{ordered_hand_id[2][0]}{ordered_hand_id[3][0]}{signature}'

#strategy is one of maximization of points and is blind to other bot's cards with zero statistical adjustments
def peg_logic(hand_playing,stack,count,turncard):
    h = hand.Hand(hand_playing,turncard)
    return h.peg_selection(stack,count,turncard)

def can_play(hand,count):
    for card in hand:
        if card.value + count <= 31:
            return True
    return False

def determine_peg_points(stack,count):
    points = 0
    h = hand.Hand(stack)
    if len(stack) > 1:
        if count == 15 or count ==  31:
            points += 2
        count += h.points_from_runs()
        if stack[-1] == stack[-2]:
            points += 2
            if len(stack) > 2 and stack[-2] == stack[-3]:
                points += 4
                if len(stack) > 3 and stack[-3] == stack[-4]:
                    points += 6
    return points


def peg_sequence(is_dealer_p1,turncard,p1,p2):
    hand1 = p1.hand.copy()
    hand2 = p2.hand.copy()
    if is_dealer_p1:
        p1_turn = True
    else:
        p1_turn = False
    while hand1 or hand2:
        count = 0
        stack = []
        while count <= 31 and (can_play(hand1,count) or can_play(hand2,count)):
            if p1_turn and can_play(hand1,count):
                choice = peg_logic(hand1,stack,count,turncard)
                count += choice.value
                stack.append(choice)
                hand1.remove(choice)
                p1.points += determine_peg_points(stack,count)
                p1_turn = False
                p1_played_last = True
            if can_play(hand2,count):
                choice = peg_logic(hand2,stack,count,turncard)
                count += choice.value
                stack.append(choice)
                hand2.remove(choice)
                p2.points += determine_peg_points(stack,count)
                p1_turn = True
                p1_played_last = False
        if count < 31:
            if p1_played_last:
                p1.score += 1
            else:
                p2.score += 1


def show_sequence(turncard,p1,p2):
    h1 = hand.Hand(p1.hand, turncard)
    h2 = hand.Hand(p2.hand, turncard)
    p1.points += h1.compute_score()
    p2.points += h2.compute_score()


def crib_sequence(turncard,hand):
    c = hand.Hand(hand, is_crib=True, turncard=turncard)
    return c.compute_score()


def memorize_results(p1, p2, p1_peg, p2_peg, crib_pts, p1_is_dealer):
    performance_by_hand = {}
    h1 = hand_id(p1.hand)
    h2 = hand_id(p2.hand)
    hand_vec = [h1,h2]
    #initialize hand if not present in hash table
    for hand in hand_vec:
        if hand not in performance_by_hand:
            performance_by_hand[h1]['times_nodeal'] = 0
            performance_by_hand[h1]['times_dealer'] = 0
            performance_by_hand[h1]['dealer_neg_peg'] = 0
            performance_by_hand[h1]['nodeal_neg_peg'] = 0
            performance_by_hand[h1]['dealer_pos_peg'] = 0
            performance_by_hand[h1]['nodeal_pos_peg'] = 0
            performance_by_hand[h1]['hand_pts'] = 0
            performance_by_hand[h1]['neg_crib_pts'] = 0
            performance_by_hand[h1]['pos_crib_pts'] = 0

    if p1_is_dealer:
        performance_by_hand[h1]['times_dealer'] += 1
        performance_by_hand[h1]['dealer_neg_peg'] -= p2_peg
        performance_by_hand[h1]['dealer_pos_peg'] += p1_peg
        performance_by_hand[h1]['hand_pts'] += p1.points - p1_peg
        performance_by_hand[h1]['pos_crib_pts'] += crib_pts

        performance_by_hand[h2]['times_nodeal'] += 1
        performance_by_hand[h2]['nodeal_neg_peg'] -= p1_peg
        performance_by_hand[h2]['nodeal_pos_peg'] += p2_peg
        performance_by_hand[h2]['hand_pts'] += p2.points - p2_peg
        performance_by_hand[h2]['neg_crib_pts'] -= crib_pts
    else:
        performance_by_hand[h2]['times_dealer'] += 1
        performance_by_hand[h2]['dealer_neg_peg'] -= p1_peg
        performance_by_hand[h2]['dealer_pos_peg'] += p2_peg
        performance_by_hand[h2]['hand_pts'] += p2.points - p2_peg
        performance_by_hand[h2]['pos_crib_pts'] += crib_pts

        performance_by_hand[h1]['times_nodeal'] += 1
        performance_by_hand[h1]['nodeal_neg_peg'] -= p2_peg
        performance_by_hand[h1]['nodeal_pos_peg'] += p1_peg
        performance_by_hand[h1]['hand_pts'] += p1.points - p1_peg
        performance_by_hand[h1]['neg_crib_pts'] -= crib_pts


def learning_by_rounds():
    p1 = players.computer('difficult')
    p2 = players.computer('difficult')
    num_rounds = 10
    d = deck.Deck()
    d.shuffle()
    is_dealer_p1 = True

    for round in range(num_rounds):
        print(f'Starting {round} of computer vs computer ...')
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
            p1.points = 0
            p2.points = 0
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
            peg_sequence(is_dealer_p1,turncard,p1,p2)
            p1_peg = p1.points
            p2_peg = p2.points
            #Updates scores in place from hand + turncard
            show_sequence(turncard,p1,p2)
            #Returns points from crib
            crib_pts = crib_sequence(turncard, hand)
            #Memorize the results
            memorize_results(p1, p2, p1_peg, p2_peg, crib_pts, is_dealer_p1)


            

if __name__ == "__main__":
    id_ranks = hand_id_mapper(suits, ranks)







    







'''
#TODO(Jon)
Basic idea here is to play n number of rounds of computer vs computer and update scores in dictionaries.
One dictionary records the statistics for discarding as a dealer
The other dictionaary records the statistics for discarding as a non-dealer
Should essentially be constant time lookup at runtime, much faster than the intermediate strategy of computing scores first

Both computer players will be using the same decisions hueristics
They will be able to see each other's cards so as to give accurate data for hand performance
'''

