import players
import deck
import users


def test_player():
    p = players.Player()
    print("\n---------  TEST player constructor  -------------\n")
    print(f'--Player name: {p.name}')
    print(f'--Player score: {str(p.score)}')
    print(f'--Player cards: {p.cards}')
    print(f'--Player is_dealer: {p.is_dealer}')


def test_human():
    username = 'test_user3'
    email = 'test_user3@test.com'
    u = users.User(username=username, email=email)
    h = players.Human(user=u)
    print("\n---------  TEST human constructor  -------------\n")
    print(f'--Human name: {h.name}')
    print(f'--Human score: {str(h.score)}')
    print(f'--Human cards: {h.cards}')
    print(f'--Human is_dealer: {h.is_dealer}')
    print(f'--Human user match stats: {h.user.match_stats}')


def test_computer():
    difficulty = 'hard'
    c = players.Computer(difficulty=difficulty)
    print("\n---------  TEST computer constructor  -------------\n")
    print(f'--Player name: {c.name}')
    print(f'--Player score: {str(c.score)}')
    print(f'--Player difficulty: {c.difficulty}')


def test_display_hand():
    d = deck.Deck()
    c = players.Computer('easy')
    hand = []
    for i in range(4):
        hand.append(d.deal_one())
    c.cards = hand
    print("\n---------  TEST display_hand() method without numbers  -------------\n")
    c.display_hand(is_numbered=False)
    print("\n---------  TEST display_hand() method with numbers  -------------\n")
    c.display_hand(is_numbered=True)
    

def test_discard_computer():
    difficulty = 'medium'
    num_discards = 2
    d = deck.Deck()
    d.shuffle()
    c = players.Computer(difficulty=difficulty)
    hand = []
    discards = []
    for i in range(6):
        hand.append(d.deal_one())
    c.cards = hand
    print(f"\n---------  TEST discard() method computer -- {difficulty}  -------------\n")
    print('---hand before discards---')
    c.display_hand(False)
    discards = c.discard(num_discards=num_discards, is_dealer=True)
    print('---hand after discards---')
    c.display_hand(False)
    c.cards = discards
    print('---Discard choices---')
    c.display_hand(False)


def test_discard_human():
    d = deck.Deck()
    d.shuffle()
    username = 'test_user3'
    email = 'test_user3@test.com'
    u = users.User(username=username, email=email)
    h = players.Human(user=u)
    hand = []
    discards = []
    for i in range(6):
        hand.append(d.deal_one())
    h.cards = hand
    print(f"\n---------  TEST discard() method human -------------\n")
    print('---hand before discards---')
    h.display_hand(is_numbered=True)
    discards = h.discard(2)
    print('---hand after discards---')
    h.display_hand(is_numbered=False)
    h.cards = discards
    print('---Discard choices---')
    h.display_hand(is_numbered=False)


def test_cut_deck():
    d = deck.Deck()
    c = players.Computer(difficulty='easy')
    print(f"\n---------  TEST cut_deck() method computer -------------\n")
    print(f'\n-- before cut --\n')
    i = 0
    for card in d.deck:
        i += 1
        print(f'{i}) {card.name}')
    c.cut_deck(d)
    print(f'\n-- after cut --\n')
    i = 0
    for card in d.deck:
        i += 1
        print(f'{i}) {card.name}')

    d = deck.Deck()
    username = 'test_user3'
    email = 'test_user3@test.com'
    u = users.User(username=username, email=email)
    h = players.Human(user=u)
    print(f"\n---------  TEST cut_deck() method human -------------\n")
    print(f'\n-- before cut --\n')
    i = 0
    for card in d.deck:
        i += 1
        print(f'{i}) {card.name}')
    h.cut_deck(d)
    print(f'\n-- after cut --\n')
    i = 0
    for card in d.deck:
        i += 1
        print(f'{i}) {card.name}')

def test_peg_one_computer():
    print(f"\n---------  TEST peg_one() computer -------------\n")
    difficulty = 'easy'
    count = 10
    d = deck.Deck()
    d.shuffle()
    c = players.Computer(difficulty=difficulty)
    hand = []
    stack = []
    for i in range(2):
        hand.append(d.deal_one())
        stack.append(d.deal_one())
    c.cards = hand
    c.display_hand()
    selected = c.peg_one(count=count, stack=stack)
    print(f'Peg selection: {selected.name}')


if __name__ == "__main__":
    #test_player()      #PASSED 12/22/20  
    #test_human()       #PASSED 12/22/20
    #test_computer()      #PASSED 12/22/20
    #test_display_hand()    #PASSED 12/22/20
    #test_discard_computer()    #Test1: 'easy', Test2: 'medium'  Test3: 'hard' PASSED 12/22/20  TODO(Jon) (Optimized Statistically Needs Tuning)
    #test_discard_human()   #PASSED 12/22/20
    #test_cut_deck()     #Test1: Computer random cut, Test1: Human chosen cut, PASSED 12/22/20
    #test_peg_one_computer()
    #test_peg_one_human()       


    
    