
import board, players, users

def test_Classic_constructor():
    print('\n--------- Test Board constructor -------------\n')
    u1 = users.User('test_user1', 'test_user_1@yahoo.com')
    u2 = users.User('test_user2', 'test_user_2@yahoo.com')
    p1 = players.Human(name='Jon', user=u1, lane=1)
    #p2 = players.Human(name='Rick', user=u2, lane=2)
    p2 = players.Computer(difficulty='hard', lane=2)
    b = board.Classic(p1, p2)
    print(f'- Player 1 name:     {b.player_one.name}')
    print(f'- Player 2 name:     {b.player_two.name}\n')
    b.display_board()


def test_update_pegs():
    print('\n--------- Test Update Pegs -------------\n')
    u1 = users.User('test_user1', 'test_user_1@yahoo.com')
    u2 = users.User('test_user2', 'test_user_2@yahoo.com')
    p1 = players.Human(name='Jon', user=u1, lane=1)
    p2 = players.Human(name='Rick', user=u2, lane=2)
    b = board.Classic(p1, p2)
    p1.score = 15
    b.update_pegs()
    p2.score = 25
    b.update_pegs()
    b.display_board()
    p1.score = 35
    b.update_pegs()
    p2.score = 40
    b.update_pegs()
    b.display_board()
    print(f'Player one: {b.player_one.score}')
    print(f'Player two: {b.player_two.score}')
    print(f'lane1 lead: {b.lane1_lead_peg}')
    print(f'lane1 hind: {b.lane1_hind_peg}')
    print(f'lane2 lead: {b.lane2_lead_peg}')
    print(f'lane2 hind: {b.lane2_hind_peg}')

def test_display_board():
    print('\n--------- Test Update Pegs -------------\n')
    u1 = users.User('test_user1', 'test_user_1@yahoo.com')
    u2 = users.User('test_user2', 'test_user_2@yahoo.com')
    p1 = players.Human(name='Jon', user=u1, lane=1)
    p2 = players.Human(name='Rick', user=u2, lane=2)
    b = board.Classic(p1, p2)
    b.display_board()



if __name__ == "__main__":
    #test_Classic_constructor()      #Test1: Human vs Human, Test2: Human vs Computer, PASSED 12/22/20
    #test_update_pegs()      #Test1: update scores and pegs and check results on board for lead peg and hind peg, PASSED 12/22/20
    #test_display_board()    #PASSED 12/22/20
