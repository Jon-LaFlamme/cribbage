import hand
import deck


def test_hand_constructor():
    print("\n---------  TEST hand constructor -------------\n")
    d = deck.Deck()
    d.shuffle()
    cards = []
    for i in range(6):
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
    print("\n---------  TEST points from runs -------------\n")
    points = h.points_from_runs()
    print(f'- points from runs: {points}')

def test_points_from_fifteens():
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
    print("\n---------  TEST points from fifteens -------------\n")
    points = h.points_from_fifteens()
    print(f'- points from fifteens: {points}')

def test_points_from_flush():
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
    print("\n---------  TEST points from flush -------------\n")
    points = h.points_from_flush()
    print(f'- points from flush: {points}')


if __name__ == "__main__":
    #test_hand_constructor()
    #test_points_from_pairs()
    #test_points_from_runs()
    #test_points_from_fifteens()
    #test_points_from_flush()
    #TODO(Jon) test points from knobs
    #TODO(Jon) test compute score
    #TODO(Jon) test all methods with turncard
    #TODO(Jon) test optimize by points
    #TODO(Jon) test optimize statistically
    #TODO(Jon) test peg selection lead
    #TODO(Jon) test peg selection

