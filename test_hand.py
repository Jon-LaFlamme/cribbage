import hand
import deck


def test_hand_constructor():
    print("\n---------  TEST hand constructor -------------\n")
    d = deck.Deck()
    d.shuffle()
    cards = []
    for i in range(6):
        cards.append(d.deal_one())
    h = hand.Hand(list_of_cards=cards)
    if h.turncard:
        print(f'- turncard: {h.turncard}')
    else:
        print(f'- no turncard')   
    print(f'- is_crib: {h.is_crib}')
    print(f'- values: {h.values}')
    print(f'- ranks: {h.ranks}')
    print(f'- suits: {h.suits}')
    print(f'------------------------')
    for card in h.hand:
        print(card.name)


def test_points_from_pairs():
    d = deck.Deck()
    d.shuffle()
    cards = []
    for i in range(5):
        cards.append(d.deal_one())
    h = hand.Hand(cards)
    if h.turncard:
        print(f'- turncard: {h.turncard}')
    else:
        print(f'- no turncard')   
    print(f'- is_crib: {h.is_crib}')
    print(f'- values: {h.values}')
    print(f'- ranks: {h.ranks}')
    print(f'- suits: {h.suits}')
    print(f'------------------------')
    for card in h.hand:
        print(card.name)
    print("\n---------  TEST points from pairs -------------\n")
    points = h.points_from_pairs()
    print(f'- points from pairs: {points}')


def test_points_from_runs():
    d = deck.Deck()
    d.shuffle()
    cards = []
    for i in range(4):
        cards.append(d.deal_one())
    turncard = d.deal_one()
    h = hand.Hand(list_of_cards=cards, turncard=turncard)
    print(f'- is_crib: {h.is_crib}')
    print(f'- values: {h.values}')
    print(f'- ranks: {h.ranks}')
    print(f'- suits: {h.suits}')
    print(f'------------------------')
    print(f'- turncard: {h.turncard.name}')
    print(f'------------------------')
    for card in h.hand:
        print(card.name)
    print("\n---------  TEST points from runs -------------\n")
    points = h.points_from_runs()
    print(f'- points from runs: {points}')


def test_points_from_fifteens():
    d = deck.Deck()
    d.shuffle()
    cards = []
    for i in range(5):
        cards.append(d.deal_one())
    h = hand.Hand(list_of_cards=cards)
    if h.turncard:
        print(f'- turncard: {h.turncard}')
    else:
        print(f'- no turncard')   
    print(f'- is_crib: {h.is_crib}')
    print(f'- values: {h.values}')
    print(f'- ranks: {h.ranks}')
    print(f'- suits: {h.suits}')
    print(f'------------------------')
    for card in h.hand:
        print(card.name)
    print("\n---------  TEST points from fifteens -------------\n")
    points = h.points_from_fifteens()
    print(f'- points from fifteens: {points}')


def test_points_from_flush():
    d = deck.Deck()
    d.shuffle()
    cards = []
    for i in range(5):
        cards.append(d.deal_one())
    h = hand.Hand(list_of_cards=cards)
    if h.turncard:
        print(f'- turncard: {h.turncard}')
    else:
        print(f'- no turncard')   
    print(f'- is_crib: {h.is_crib}')
    print(f'- values: {h.values}')
    print(f'- ranks: {h.ranks}')
    print(f'- suits: {h.suits}')
    print(f'------------------------')
    for card in h.hand:
        print(card.name)
    print("\n---------  TEST points from flush -------------\n")
    points = h.points_from_flush()
    print(f'- points from flush: {points}')


def test_points_from_knobs():
    d = deck.Deck()
    d.shuffle()
    cards = []
    turncard = d.deal_one()
    for i in range(4):
        cards.append(d.deal_one())
    h = hand.Hand(list_of_cards=cards, turncard=turncard)
    if h.turncard:
        print(f'- turncard: {h.turncard.name}')
    else:
        print(f'- no turncard')   
    print(f'- is_crib: {h.is_crib}')
    print(f'- values: {h.values}')
    print(f'- ranks: {h.ranks}')
    print(f'- suits: {h.suits}')
    print(f'------------------------')
    for card in h.hand:
        print(card.name)
    print("\n---------  TEST points from knobs -------------\n")
    points = h.points_from_knobs()
    print(f'- points from knobs: {points}')


def test_compute_score():
    d = deck.Deck()
    d.shuffle()
    cards = []
    turncard = d.deal_one()
    for i in range(4):
        cards.append(d.deal_one())
    h = hand.Hand(list_of_cards=cards, turncard=turncard)  
    print(f'- is_crib: {h.is_crib}')
    print(f'- values: {h.values}')
    print(f'- ranks: {h.ranks}')
    print(f'- suits: {h.suits}')
    print(f'------------------------')
    print(f'turncard: {turncard.name}')
    print(f'------------------------')
    for card in h.hand:
        print(card.name)
    print("\n---------  TEST compute score -------------\n")
    points = h.compute_score()
    print(f'- score: {points}')


def test_optimize_by_points():
    print("\n---------  TEST optimize by points -------------\n")
    d = deck.Deck()
    d.shuffle()
    cards = []
    print(f'--- 6-card deal -----')
    for i in range(6):
        cards.append(d.deal_one())
        print(f'- {cards[-1].name}')
    h = hand.Hand(cards)
    choices = h.optimize_by_points(2)
    ch = hand.Hand(list_of_cards=choices)
    print(f'--- 4-cards selected -----')
    for card in ch.hand:
        print(card.name)
    points = ch.compute_score()
    print(f'---------------------')
    print(f'points from selection: {points}')



if __name__ == "__main__":
    #test_hand_constructor()
    #test_points_from_pairs()
    #test_points_from_runs()
    #test_points_from_fifteens()
    #test_points_from_flush()
    #test_points_from_knobs()
    #test_compute_score()
    #test_optimize_by_points()

    #Remaining methods from hand.py are to be tested in test_learning.py

