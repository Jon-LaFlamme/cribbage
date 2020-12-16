import learning
import deck
import random
import players


def test_hand_id_mapper():
    print('\n--------- Test hand id mapper ---------\n')
    id_ranks = learning.hand_id_mapper(learning.suits, learning.ranks)
    for key,value in id_ranks.items():
        print(f'- card id: {key}; deck rank: {value}')


def test_hand_suit_signature():
    print('\n--------- Test hand suit signature ---------\n')
    d = deck.Deck()
    d.shuffle()
    hand = []
    for i in range(4):
        hand.append(d.deal_one())
    hand_signature = learning.hand_suit_signature(hand)
    print('-------------------------------')
    for card in hand:
        print(f'- {card.name}')
    print('-------------------------------')
    print(f'Hand suit signature: {hand_signature}')


def test_hand_id():
    print('\n--------- Test hand id ---------\n')
    d = deck.Deck()
    d.shuffle()
    hand = []
    for i in range(4):
        hand.append(d.deal_one())
    print('-------------------------------')
    for card in hand:
        print(f'- {card.name}')
    print('-------------------------------')
    unique_hand_id = learning.hand_id(hand)
    print(f'Unique hand id: {unique_hand_id}')

def test_can_play():
    print('\n--------- Test can play ---------\n')
    d = deck.Deck()
    d.shuffle()
    count = random.randint(0,31)
    hand = []
    for i in range(4):
        hand.append(d.deal_one())
    print('-------------------------------')
    for card in hand:
        print(f'- {card.name}: value of {card.value}')
    print('-------------------------------')
    print(f'Count is: {count}')
    print(f'Can play retruns: {learning.can_play(hand,count)}')

def test_peg_logic():
    print('\n--------- Test peg logic ---------\n')
    d = deck.Deck()
    d.shuffle()
    count = 0
    hand = []
    stack = []
    for i in range(random.randint(0,5)):
        stack.append(d.deal_one())
    print('------- stack is ---------')
    for card in stack:
        print(f'- {card.name}')  
        count += card.value   
    print(f'---stack count: {count} ---------')
    for i in range(8):
        hand.append(d.deal_one())
    turncard = d.deal_one()
    print('-------------------------------')
    print(f'turncard is {turncard.name}')
    print('-------------------------------')
    print('------- original hand -----------')
    for card in hand:
        print(f'- {card.name}: value of {card.value}')
    print('-------------------------------')
    while learning.can_play(hand,count):
        choice = learning.peg_logic(hand,stack,count,turncard)
        hand.remove(choice)
        print('-------------------------------')
        print(f'- peg selection is: {choice.name}')
        stack.append(choice)
        print('------- stack is ---------')
        for card in stack:
            print(f'- {card.name}') 
        count += choice.value  
        print(f'---stack count: {count} ---------')    

def test_determine_peg_points():
    print('\n--------- Test determine peg points ---------\n')
    d = deck.Deck()
    d.shuffle()
    count = 0
    stack = []
    for i in range(random.randint(2,7)):
        stack.append(d.deal_one())
    print('------- stack is ---------')
    for card in stack:
        count += card.value
        print(f'- {card.name}')
    if count > 31:
        print('\n ---- Try again. Count overflow! ------ /n')
    else:
        points = learning.determine_peg_points(stack,count)
        print(f'------- count is:    {count}')
        print(f'------- peg points:  {points} ---------')
    

def test_peg_sequence():
    print('\n--------- Test peg sequence ---------\n')
    d = deck.Deck()
    d.shuffle()
    p1 = players.computer('difficult')
    p2 = players.computer('difficult')
    for i in range(4):
        p1.hand.append(d.deal_one())
        p2.hand.append(d.deal_one())
    tc = d.deal_one()
    if tc.value > 6:
        is_dealer_p1 = True
        print('-------- player 1 is dealer ---------')
    else:
        is_dealer_p1 = False
        print('-------- player 2 is dealer ---------')
    print('-------------------------------')
    print(f'turncard is {tc.name}')
    print('-------------------------------')
    print('\n------- player 1 hand ---------\n')
    for card in p1.hand:
        print(f'- {card.name}')
    print('\n------- player 2 hand ---------\n')
    for card in p2.hand:
        print(f'- {card.name}')
    print('\n-------------------------------')
    stack = learning.peg_sequence(is_dealer_p1,tc,p1,p2)
    print('\n------- stack ---------')
    for card in stack:
        print(f'- {card.name}')
    print(f'\n------- player 1 points: {p1.score} ---------')  
    print(f'------- player 2 points: {p2.score} ---------')


def test_show_sequence():
    print('\n--------- Test show sequence ---------\n')
    d = deck.Deck()
    d.shuffle()
    p1 = players.computer('difficult')
    p2 = players.computer('difficult')
    for i in range(4):
        p1.hand.append(d.deal_one())
        p2.hand.append(d.deal_one())
    tc = d.deal_one()
    print('-------------------------------')
    print(f'turncard is {tc.name}')
    print('-------------------------------')
    learning.show_sequence(tc,p1,p2)
    print(f'\n------- player 1 points: {p1.score} ---------')  
    print(f'------- player 2 points: {p2.score} ---------')
    print('\n------- player 1 hand ---------\n')
    for card in p1.hand:
        print(f'- {card.name}')
    print('\n------- player 2 hand ---------\n')
    for card in p2.hand:
        print(f'- {card.name}')

def test_crib_sequence():
    print('\n--------- Test crib sequence ---------\n')
    d = deck.Deck()
    d.shuffle()
    crib = []
    for i in range(4):   
        crib.append(d.deal_one())
    tc = d.deal_one()
    print('-------------------------------')
    print(f'turncard is {tc.name}')
    print('-------------------------------')
    print('\n----------- crib ------------')
    for card in crib:
        print(f'- {card.name}')
    print('-------------------------------')
    points = learning.crib_sequence(tc,crib)
    print(f'-- points from crib: {points} ')

    









if __name__ == "__main__":
    #test_hand_id_mapper()
    #test_hand_suit_signature()
    #test_hand_id()
    #test_can_play()
    #test_peg_logic()
    #test_determine_peg_points()
    #test_peg_sequence()
    #test_show_sequence()
    test_crib_sequence()
    #TODO(Jon) test_memorize_results()
    #TODO(Jon) test_learning_by_rounds()
    #TODO(Jon) test_main()
