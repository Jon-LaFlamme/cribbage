import deck as d

def test_deck_constructor():   

    print("\n---------  TEST Deck Constructor -------------\n")
    deck = d.Deck()
    print(f'---Length of deck is: {len(deck.deck)}\n')
    for card in deck.deck:
        print(f'- {card.name}')


def test_card_properties():    

    print("\n---------  TEST Card Properties -------------\n")
    deck = d.Deck()                      #expected face card values = 10, expected ranks 1-13
    for card in deck.deck:
        print(f'- Card name: {str(card.name)},   Card value: {str(card.value)},   Card rank: {str(card.rank)}')


def test_deck_peek():

    print("\n---------  TEST Deck Shuffle -------------\n")
    deck = d.Deck()
    #edge cases 
    print(f'---Peek deck at index 0:  {deck.peek(0).name}.')
    print(f'---Peek deck at index 51: {deck.peek(51).name}.')
    #Invalid case exception test
    print(f'---Peek deck at index 52: {deck.peek(52).name}.')


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


def test_deck_deal_one():
    print("\n---------  TEST Deck Deal One  -------------\n")
    deck = d.Deck()
    for i in range(len(deck.deck)):
        print(f'Card Dealt: {deck.deal_one().name}')
    #testing exception/error handling
    deck.deal_one()




if __name__ == "__main__":
    #test_deck_constructor()     #PASSED 12/22/20
    #test_card_properties()     #PASSED 12/22/20
    #test_deck_peek()           #PASSED 12/22/20
    #test_deck_cut()            #PASSED 12/22/20
    #test_deck_shuffle()        #PASSED 12/22/20
    #test_deck_deal_one()       #PASSED 12/22/20

