import learning
import deck


def test_hand_id_mapper():
    print('\n--------- Test hand id mapper ---------\n')
    id_ranks = learning.hand_id_mapper(learning.suits, learning.ranks)
    for key,value in id_ranks.items():
        print(f'- card id: {key}; deck rank: {value}')


def test_hand_suit_signature():
    print('\n--------- Test hand suit signature ---------\n')
    d = deck.Deck()
    d.shuffle()
    hand = []
    for i in range(4):
        hand.append(d.deal_one())
    hand_signature = learning.hand_suit_signature(hand)
    print('-------------------------------')
    for card in hand:
        print(f'- {card.name}')
    print('-------------------------------')
    print(f'Hand suit signature: {hand_signature}')


def test_hand_id():
    print('\n--------- Test hand id ---------\n')
    d = deck.Deck()
    d.shuffle()
    hand = []
    for i in range(4):
        hand.append(d.deal_one())
    print('-------------------------------')
    for card in hand:
        print(f'- {card.name}')
    print('-------------------------------')
    unique_hand_id = learning.hand_id(hand)
    print(f'Unique hand id: {unique_hand_id}')


if __name__ == "__main__":
    #test_hand_id_mapper()
    #test_hand_suit_signature()
    #test_hand_id()
    #TODO(Jon) test_peg_logic()
    #TODO(Jon) test_can_play()
    #TODO(Jon) test_determine_peg_points()
    #TODO(Jon) test_peg_sequence()
    #TODO(Jon) test_show_sequence()
    #TODO(Jon) test_crib_sequence()
    #TODO(Jon) test_memorize_results()
    #TODO(Jon) test_learning_by_rounds()
    #TODO(Jon) test_main()
