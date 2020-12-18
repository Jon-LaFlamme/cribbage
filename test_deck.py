import deck as d

#Test1 52-card Deck constructor validation
def test_deck_constructor():   

    print("\n---------  TEST Deck Constructor -------------\n")
    deck = d.Deck()
    print(f'---Length of deck is: {len(deck.deck)}\n')
    for card in deck.deck:
        print(f'- {card.name}')


#Test2 Card property validation
def test_card_properties():    

    print("\n---------  TEST Card Properties -------------\n")
    deck = d.Deck()                      #expected face card values = 10, expected ranks 1-13
    for card in deck.deck:
        print(f'- Card name: {str(card.name)},   Card value: {str(card.value)},   Card rank: {str(card.rank)}')


#test3 Deck.peek() validation @param is an integer representing a valid index
def test_deck_peek():

    print("\n---------  TEST Deck Shuffle -------------\n")
    deck = d.Deck()
    #edge cases 
    print(f'---Peek deck at index 0:  {deck.peek(0).name}.')
    print(f'---Peek deck at index 51: {deck.peek(51).name}.')
    #Invalid case exception test
    print(f'---Peek deck at index 52: {deck.peek(52).name}.')


#test4 Deck.cut()
def test_deck_cut():

    print("\n---------  TEST Deck Cut -------------\n")
    deck = d.Deck()
    i = 0
    print(f'---Original Deck\n')
    for card in deck.deck:
        i += 1
        print(f'- {i}) {card.name}')

    #typical case (index 25):
    deck.cut(26)
    i = 0
    print(f'\n--- Deck cut at index 26 \n')
    i = 0
    for card in deck.deck:
        i += 1
        print(f'- {i}) {card.name}')

    #edge case 1 (index 0):
    deck.cut(0)
    i = 0
    print(f'\n--- Deck cut at index 0 \n')
    for card in deck.deck:
        i += 1
        print(f'- {i}) {card.name}')

    #edge case 2 (index 51):
    deck.cut(51)
    i = 0
    print(f'\n--- Deck cut at index 51 \n')
    for card in deck.deck:
        i += 1
        print(f'- {i}) {card.name}')

    #Invalid case (index 52):
    deck.cut(52)
    i = 0
    print(f'\n--- Deck cut at indext 52 \n')
    for card in deck.deck:
        i += 1
        print(f'- {i}) {card.name}')
    

#test5 deck.shuffle() method, dependency on deck.cut() method
#Expectation: deck should be appear sufficiently randomized with minimal clustering
def test_deck_shuffle():            
    print("\n---------  TEST Deck Shuffle -------------\n")
    deck = d.Deck()                  
    print("\n---default deck order---\n")
    i = 0
    for card in deck.deck:
        i += 1
        print(f'{i}) {card.name}')
    print("\n---after shuffle---\n")
    deck.shuffle()
    i = 0
    for card in deck.deck:
        i += 1
        print(f'{i}) {card.name}')


#test6 deck.deal_one() method
def test_deck_deal_one():
    print("\n---------  TEST Deck Deal One  -------------\n")
    deck = d.Deck()
    for i in range(len(deck.deck)):
        print(f'Card Dealt: {deck.deal_one().name}')
    #testing exception
    deck.deal_one()

#print card IDs for deck
def card_ids():
    print("\n---------  Card Ids  -------------\n")
    deck = d.Deck()
    for card in deck.deck:
        print(card.id)


if __name__ == "__main__":
    #test_deck_constructor()
    #test_card_properties()
    #test_deck_peek()
    #test_deck_cut()
    #test_deck_shuffle()
    #test_deck_deal_one()
    #card_ids()

