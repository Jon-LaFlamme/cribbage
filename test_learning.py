import learning
import deck
import random
import players
import hand


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
    count = random.randint(25,31)
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
    for i in range(random.randint(2,4)):
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
    

#For test_peg_sequence: be sure to enable test methods in learning.py, namely return element
def test_peg_sequence():
    print('\n--------- Test peg sequence ---------\n')
    d = deck.Deck()
    d.shuffle()
    p1 = players.computer('difficult')
    p2 = players.computer('difficult')
    for i in range(4):
        p1.cards.append(d.deal_one())
        p2.cards.append(d.deal_one())
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
    for card in p1.cards:
        print(f'- {card.name}')
    print('\n------- player 2 hand ---------\n')
    for card in p2.cards:
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
        p1.cards.append(d.deal_one())
        p2.cards.append(d.deal_one())
    tc = d.deal_one()
    print('-------------------------------')
    print(f'turncard is {tc.name}')
    print('-------------------------------')
    learning.show_sequence(tc,p1,p2)
    print(f'\n------- player 1 points: {p1.score} ---------')  
    print(f'------- player 2 points: {p2.score} ---------')
    print('\n------- player 1 hand ---------\n')
    for card in p1.cards:
        print(f'- {card.name}')
    print('\n------- player 2 hand ---------\n')
    for card in p2.cards:
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


def test_learning_by_hands(intelligent=True):
    #Test_learning_by_hands() does not call the target function. It is a lightly modified copy with console output, no memorization

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

    #Test output
    print('-------------------------------')
    print(f'turncard is {turncard.name}')
    print('-------------------------------')
    print('\n------- player 1 hand ---------\n')
    for card in p1.cards:
        print(f'- {card.name}')
    print('\n------- player 2 hand ---------\n')
    for card in p2.cards:
        print(f'- {card.name}')
    print('\n----------- crib ------------')
    for card in crib:
        print(f'- {card.name}')
    print('-------------------------------')

    #Main driver block: peg sequence updates player scores; scores stored before updated again in show_sequence 
    learning.peg_sequence(is_dealer_p1, turncard, p1, p2)  
    p1_peg = p1.score
    p2_peg = p2.score  
    learning.show_sequence(turncard,p1,p2)
    crib_pts = learning.crib_sequence(turncard, crib)

    #Memorize the results
    #learning.memorize_results(p1, p2, p1_peg, p2_peg, crib_pts, is_dealer_p1)

    #Print the results to console
    print(f'\n player 1 score:      {p1.score - p1_peg}')
    print(f' player 1 peg points: {p1_peg}')
    print(f' player 2 score:      {p2.score - p2_peg}')
    print(f' player 2 peg points: {p2_peg}')
    print(f' crib points:         {crib_pts}\n\n')


def test_memorize_results():
    p1 = players.computer("moderate")
    p2 = players.computer("moderate")
    d = deck.Deck()
    d.shuffle()
    crib = []
    turncard = d.deal_one()
    is_dealer_p1 = True
    if random.randint(0,9) & 1  == 1:
        is_dealer_p1 = False
    for i in range(4):
        p1.cards.append(d.deal_one())
        p2.cards.append(d.deal_one())
        crib.append(d.deal_one())
    print('\n------- player 1 hand ---------\n')
    for card in p1.cards:
        print(f'- {card.name}')
    print('\n------- player 2 hand ---------\n')
    for card in p2.cards:
        print(f'- {card.name}')
    print('\n----------- crib ------------')
    for card in crib:
        print(f'- {card.name}')
    print('-------------------------------')

    learning.peg_sequence(is_dealer_p1, turncard, p1, p2)
    p1_peg = p1.score
    p2_peg = p2.score  
    learning.show_sequence(turncard,p1,p2)
    crib_pts = learning.crib_sequence(turncard, crib)

    #Print the results to compare against
    print(f'\n player 1 score:      {p1.score - p1_peg}')
    print(f' player 1 peg points: {p1_peg}')
    print(f' player 2 score:      {p2.score - p2_peg}')
    print(f' player 2 peg points: {p2_peg}')
    print(f' crib points:         {crib_pts}\n\n')

    learning.memorize_results(p1, p2, p1_peg, p2_peg, crib_pts, is_dealer_p1)
    print(learning.performance_by_hand)




if __name__ == "__main__":
    #test_hand_id_mapper()
    #test_hand_suit_signature()
    #test_hand_id()
    #test_can_play()
    #test_peg_logic()
    #test_determine_peg_points()        #TODO(Jon) Lousy test, needs to be reworked
    test_peg_sequence()                 #TODO(Jon) peg_sequence Appears to be the choke point in learning.py
    #test_show_sequence()
    #test_crib_sequence()
    #test_learning_by_hands(intellligent=False)    
    #test_memorize_results() 
    #TODO(Jon) test_main()
