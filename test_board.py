import board

def test_BoardMember_constructor():
    print('\n--------- Test BoardMember constructor -------------\n')
    bm = board.BoardMember('Jon')
    print(f'- name:     {bm.name}')
    print(f'- hind peg: {bm.hind_peg}')
    print(f'- lead peg: {bm.lead_peg}')
 








if __name__ == "__main__":
    test_BoardMember_constructor()
    #TODO(Jon) test_Board_constructor()
    #TODO(Jon) test_Classic_constructor()

    #TODO(Jon) test_update_pegs()
    #TODO(Jon) test_update_board()
    #TOOD(Jon) test_display_board()
