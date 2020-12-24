import games
import players
import users
import board
import deck

def test_determine_dealer_sequence():
    print(f'\n-------- Test Determine Dealer Sequence ----------\n')
    #computer vs computer
    p1 = players.Computer(difficulty='medium')
    p2 = players.Computer(difficulty='medium')
    g = games.Cribbage(p1,p2)
    g.deck.shuffle()
    g.determine_dealer_sequence()
    print(f'\n-- Is {g.player_one.name} Dealer? {g.player_one.is_dealer}')
    print(f'\n-- Is {g.player_two.name} Dealer? {g.player_two.is_dealer}')


def test_deal_sequence():
    print(f'\n-------- Test Deal Sequence ----------\n')
    #computer vs computer
    p1 = players.Computer(difficulty='medium')
    p2 = players.Computer(difficulty='medium')
    g = games.Cribbage(p1,p2)
    g.deck.shuffle()
    g.determine_dealer_sequence()
    g.deal_sequence()
    print(f'-- {g.player_one.name} hand:')
    g.player_one.display_hand()
    print(f'-- {g.player_two.name} hand:')
    g.player_two.display_hand()
    
def test_discard_sequence():
    print(f'\n-------- Test Discard Sequence ----------\n')
    #computer vs computer
    p1 = players.Computer(difficulty='medium')
    p2 = players.Computer(difficulty='medium')
    g = games.Cribbage(p1,p2)
    g.deck.shuffle()
    g.determine_dealer_sequence()
    g.deal_sequence()
    print(f'-- {g.player_one.name} hand:')
    g.player_one.display_hand()
    print(f'-- {g.player_two.name} hand:')
    g.player_two.display_hand()
    g.discard_sequence()
    print(f'-- {g.player_one.name} hand:')
    g.player_one.display_hand()
    print(f'-- {g.player_two.name} hand:')
    g.player_two.display_hand()
    print('\n----------- The crib --------------')
    for card in g.crib:
        print(f'|| {card.name}')

def test_turncard_sequence():
    print(f'\n-------- Test Turncard Sequence ----------\n')
    #computer vs computer
    p1 = players.Computer(difficulty='medium')
    p2 = players.Computer(difficulty='medium')
    g = games.Cribbage(p1,p2)
    g.deck.shuffle()
    g.determine_dealer_sequence()
    g.turncard_sequence()

def test_peg_sequence():
    print(f'\n-------- Test Pegging Sequence ----------\n')
    #computer vs computer
    p1 = players.Computer(difficulty='medium')
    p2 = players.Computer(difficulty='medium')
    g = games.Cribbage(p1,p2)
    g.deck.shuffle()
    g.determine_dealer_sequence()
    g.deal_sequence()
    g.turncard_sequence()
    g.discard_sequence()
    g.peg_sequence()
    

def test_show_sequence():
    print(f'\n-------- Test Show Sequence ----------\n')
    #computer vs computer
    p1 = players.Computer(difficulty='medium')
    p2 = players.Computer(difficulty='medium')
    g = games.Cribbage(p1,p2)
    g.deck.shuffle()
    g.determine_dealer_sequence()
    g.deal_sequence()
    g.turncard_sequence()
    g.discard_sequence()
    g.show_sequence()


def test_game_driver():
    #computer vs computer
    p1 = players.Computer(difficulty='medium')
    p2 = players.Computer(difficulty='medium')
    g = games.Cribbage(p1,p2)
    g.game_driver()
    





if __name__ == "__main__":
    #test_determine_dealer_sequence()        #PASSED 12/23/20
    #test_deal_sequence()           #PASSED 12/23/20
    #test_discard_sequence()         #PASSED 12/23/20
    #test_turncard_sequence()        #PASSED 12/23/20
    #test_peg_sequence()            #PASSED 12/23/20
    #test_show_sequence()           #PASSED 12/23/20
    test_game_driver()
