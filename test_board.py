import board
import players
import users


def test_Classic_constructor():
    print('\n--------- Test Board constructor -------------\n')
    u1 = users.User('test_user_1', 'test_user_1@yahoo.com')
    u2 = users.User('test_user_1', 'test_user_2@yahoo.com')
    p1 = players.Human(name='Jon', user=u1, land=2)
    p2 = players.Human(name='Rick', user=u2, lane=2)
    b = board.Classic(p1, p2)

    print(f'- Player 1 name:     {b.player_one.name}')
    print(f'- Player 2 name:     {b.player_two.name}\n')
    b.display_board()


def test_update_pegs():
    print('\n--------- Test Board constructor -------------\n')
    b = board.Classic('Jon','Rick')
    b.update_pegs('Jon', 5)
    b.update_pegs('Rick', 3)
    b.display_board()
    b.update_pegs('Jon', 9)
    b.update_pegs('Rick', 11)
    b.display_board()


if __name__ == "__main__":
    test_Classic_constructor()
    #test_update_pegs()
