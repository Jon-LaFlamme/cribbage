import deck
import players
import hand
from itertools import combinations
import json
import random
import time

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
    #points for 15 or 31
    if len(stack) > 1:
        if count == 15 or count ==  31:
            points += 2
        #check for runs by working backward
        if len(stack) > 2:
            i = 3
            max_run_points = 0
            while i <= len(stack):
                substack = hand.Hand(h.hand[-i:])
                run_points = substack.points_from_runs()
                if run_points > 0:
                    max_run_points = run_points
                else:
                    break
            points += max_run_points
        #check for pairs
        if stack[-1].rank == stack[-2].rank:
            points += 2
            if len(stack) > 2 and stack[-2].rank == stack[-3].rank:
                points += 6
                if len(stack) > 3 and stack[-3].rank == stack[-4].rank:
                    points += 12
    return points


def peg_sequence(is_dealer_p1,turncard,p1,p2):
    #multistack for testing only
    multistack = []
    hand1 = list(p1.cards).copy()
    hand2 = list(p2.cards).copy()
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
                p1.score += determine_peg_points(stack,count)
                p1_turn = False
                p1_played_last = True
            if can_play(hand2,count):
                choice = peg_logic(hand2,stack,count,turncard)
                count += choice.value
                stack.append(choice)
                hand2.remove(choice)
                p2.score += determine_peg_points(stack,count)
                p1_turn = True
                p1_played_last = False
        if count < 31:
            if p1_played_last:
                p1.score += 1
            else:
                p2.score += 1
        #For testing only
        print(f' count sums to {count}')   
        multistack.extend(stack)
    return multistack
    

def show_sequence(turncard,p1,p2):
    h1 = hand.Hand(p1.cards, turncard=turncard)
    h2 = hand.Hand(p2.cards, turncard=turncard)
    p1.score += h1.compute_score()
    p2.score += h2.compute_score()


def crib_sequence(turncard,crib_hand):
    c = hand.Hand(crib_hand, is_crib=True, turncard=turncard)
    return c.compute_score()


def memorize_results(p1, p2, p1_peg, p2_peg, crib_pts, p1_is_dealer):
    h1 = hand_id(p1.cards)
    h2 = hand_id(p2.cards)
    hand_vec = [h1,h2]
    #initialize hand if not present in hash table
    for hand in hand_vec:
        if hand not in performance_by_hand:
            performance_by_hand[hand] = {'times_nodeal':0,
                                       'times_dealer':0,
                                       'dealer_neg_peg':0,
                                       'nodeal_neg_peg':0,
                                       'dealer_pos_peg':0,
                                       'nodeal_pos_peg':0,
                                       'hand_pts':0,
                                       'neg_crib_pts':0,
                                       'pos_crib_pts':0}

    if p1_is_dealer:
        performance_by_hand[h1]['times_dealer'] += 1
        performance_by_hand[h1]['dealer_neg_peg'] -= p2_peg
        performance_by_hand[h1]['dealer_pos_peg'] += p1_peg
        performance_by_hand[h1]['hand_pts'] += p1.score - p1_peg
        performance_by_hand[h1]['pos_crib_pts'] += crib_pts

        performance_by_hand[h2]['times_nodeal'] += 1
        performance_by_hand[h2]['nodeal_neg_peg'] -= p1_peg
        performance_by_hand[h2]['nodeal_pos_peg'] += p2_peg
        performance_by_hand[h2]['hand_pts'] += p2.score - p2_peg
        performance_by_hand[h2]['neg_crib_pts'] -= crib_pts
    else:
        performance_by_hand[h2]['times_dealer'] += 1
        performance_by_hand[h2]['dealer_neg_peg'] -= p1_peg
        performance_by_hand[h2]['dealer_pos_peg'] += p2_peg
        performance_by_hand[h2]['hand_pts'] += p2.score - p2_peg
        performance_by_hand[h2]['pos_crib_pts'] += crib_pts

        performance_by_hand[h1]['times_nodeal'] += 1
        performance_by_hand[h1]['nodeal_neg_peg'] -= p2_peg
        performance_by_hand[h1]['nodeal_pos_peg'] += p1_peg
        performance_by_hand[h1]['hand_pts'] += p1.score - p1_peg
        performance_by_hand[h1]['neg_crib_pts'] -= crib_pts


def learning_by_hands(intelligent=True):
    #Function initializations: setup players, deck, turncard, local variables, determine dealer
    p1 = players.computer("moderate")
    p2 = players.computer("moderate")
    d = deck.Deck()
    d.shuffle()
    crib = []
    turncard = d.deal_one()
    is_dealer_p1 = True
    if random.randint(0,9) & 1  == 1:
        is_dealer_p1 = False

    #Allows learning Function to focus either on random configurations or heuristically influenced configurations 
    if not intelligent:
        for i in range(4):
            p1.cards.append(d.deal_one())
            p2.cards.append(d.deal_one())
            crib.append(d.deal_one())
    else:
        p1_dealt_hand = []
        p2_dealt_hand = []
        for i in range(6):
            p1_dealt_hand.append(d.deal_one())
            p2_dealt_hand.append(d.deal_one())
        h1 = hand.Hand(p1_dealt_hand)
        h2 = hand.Hand(p2_dealt_hand)
        h1_selects = h1.optimize_by_points()
        h2_selects = h2.optimize_by_points()
        p1.cards = list(h1_selects)
        p2.cards = list(h2_selects)
        for cp1,cp2 in zip(p1_dealt_hand,p2_dealt_hand):
            if cp1 not in h1_selects:
                crib.append(cp1)
            if cp2 not in h2_selects:
                crib.append(cp2)

    time.sleep(1)
    #Main driver block: peg sequence updates player scores; scores stored before updated again in show_sequence 
    peg_sequence(is_dealer_p1, turncard, p1, p2)
    time.sleep(1)  
    p1_peg = p1.score
    p2_peg = p2.score  
    show_sequence(turncard,p1,p2)
    crib_pts = crib_sequence(turncard, crib)
    time.sleep(1)
    #Memorize the results
    memorize_results(p1, p2, p1_peg, p2_peg, crib_pts, is_dealer_p1)

if __name__ == "__main__":

    '''
    with open('outcomes.json','r') as f:
        performance_by_hand = json.load(f)

    for i in range(2):
        learning_by_hands(intelligent=True)
        time.sleep(1)

    print(f' length of peformance by hand: {len(performance_by_hand)}')

    with open('outcomes.json', 'w') as f:
        json.dump(performance_by_hand, f)
    '''



    







'''
#TODO(Jon)
Basic idea here is to play n number of rounds of computer vs computer and update scores in dictionaries.
One dictionary records the statistics for discarding as a dealer
The other dictionaary records the statistics for discarding as a non-dealer
Should essentially be constant time lookup at runtime, much faster than the intermediate strategy of computing scores first

Both computer players will be using the same decisions hueristics
They will be able to see each other's cards so as to give accurate data for hand performance
'''

