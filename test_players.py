import players
import deck

#test1 player constructor
def test_player():
    p = players.player()
    print("\n---------  TEST player constructor  -------------\n")
    print(f'--Player name: {p.name}')
    print(f'--Player record: {p.record}')
    print(f'--Player score: {str(p.score)}')
    print(f'--Player is_human: {str(p.is_human)}')

#test2 human constructor defualt and with name argument
def test_human(*arg):
    h = players.human(arg)
    print("\n---------  TEST human constructor  -------------\n")
    print(f'--Player name: {h.name}')
    print(f'--Player record: {h.record}')
    print(f'--Player score: {str(h.score)}')
    print(f'--Player is_human: {str(h.is_human)}')

#test3 human constructor defualt and with name argument
def test_computer(difficulty):
    c = players.computer(difficulty)
    print("\n---------  TEST computer constructor  -------------\n")
    print(f'--Player name: {c.name}')
    print(f'--Player record: {c.record}')
    print(f'--Player score: {str(c.score)}')
    print(f'--Player is_human: {c.is_human}')
    print(f'--Player difficulty: {c.difficulty}')

#test4 display_hand() method
def test_display_hand():
    d = deck.Deck()
    p = players.computer('easy')
    hand = []
    for i in range(4):
        hand.append(d.deal_one())
    p.cards = hand
    print("\n---------  TEST display_hand() method without numbers  -------------\n")
    p.display_hand(False)
    print("\n---------  TEST display_hand() method with numbers  -------------\n")
    p.display_hand(True)
    
#test5 discard() method computer [easy, intermediate, difficult]
def test_discard_computer(difficulty):
    d = deck.Deck()
    d.shuffle()
    p = players.computer(difficulty)
    hand = []
    discards = []
    for i in range(5):
        hand.append(d.deal_one())
    p.cards = hand
    print(f"\n---------  TEST discard() method computer -- {difficulty}  -------------\n")
    print('---hand before discards---')
    p.display_hand(False)
    discards = p.discard(1)
    print('---hand after discards---')
    p.display_hand(False)
    p.cards = discards
    print('---Discard choices---')
    p.display_hand(False)

#test6 discard() method human
def test_discard_human():
    d = deck.Deck()
    d.shuffle()
    p = players.human()
    hand = []
    discards = []
    for i in range(6):
        hand.append(d.deal_one())
    p.cards = hand
    print(f"\n---------  TEST discard() method human -------------\n")
    print('---hand before discards---')
    p.display_hand(True)
    discards = p.discard(2)
    print('---hand after discards---')
    p.display_hand(False)
    p.cards = discards
    print('---Discard choices---')
    p.display_hand(False)

#test7 cut_deck() computer and human
def test_cut_deck():
    d = deck.Deck()
    p = players.computer('easy')
    print(f"\n---------  TEST cut_deck() method computer -------------\n")
    print(f'-- before cut --')
    i = 0
    for card in d.deck:
        i += 1
        print(f'{i}) {card.name}')
    p.cut_deck(d)
    print(f'-- after cut --')
    i = 0
    for card in d.deck:
        i += 1
        print(f'{i}) {card.name}')

    d = deck.Deck()
    p = players.human()
    print(f"\n---------  TEST cut_deck() method human -------------\n")
    print(f'-- before cut --')
    i = 0
    for card in d.deck:
        i += 1
        print(f'{i}) {card.name}')
    p.cut_deck(d)
    print(f'-- after cut --')
    i = 0
    for card in d.deck:
        i += 1
        print(f'{i}) {card.name}')

if __name__ == "__main__":
    #test_player()
    #test_human()
    #test_human('Jane Doe')
    #test_computer('easy')
    #test_computer('intermediate')
    #test_computer('difficult')
    #test_display_hand()
    #test_discard_computer('easy')
    #test_discard_computer('intermediate')
    #test_discard_computer('difficult')
    #test_discard_human()
    #test_cut_deck()


    
    