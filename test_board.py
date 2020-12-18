import board

def test_BoardMember_constructor():
    print('\n--------- Test BoardMember constructor -------------\n')
    bm = board.BoardMember('Jon')
    print(f'- name:     {bm.name}')
    print(f'- hind peg: {bm.hind_peg}')
    print(f'- lead peg: {bm.lead_peg}')
 

def test_Classic_constructor():
    print('\n--------- Test Board constructor -------------\n')
    b = board.Classic('Jon','Rick')
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
    #test_BoardMember_constructor()
    #test_Classic_constructor()
    #test_update_pegs()
