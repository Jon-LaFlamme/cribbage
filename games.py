


class Cribbage():

    def __init__(self, player_one, player_two, board, deck):
        self.player_one = player_one    #players.Player() object
        self.player_two = player_two
        self.board = board              #board.Board() object
        self.deck = deck                #deck.Deck() object
        self.crib = []

    def determine_dealer(self):
        #lower cut wins the deal
        undetermined = True
        while undetermined:
            card_1 = self.player_one.cut_deck(self.deck, for_first_deal=True)
            card_2 = self.player_two.cut_deck(self.deck, for_first_deal=True)
            if card_1 < card_2:
                self.player_one.is_dealer = True
                undetermined = False
            elif card_2 < card_1:
                self.player_two.is_dealer = True
                undetermined = False
            else:
                print('Tie! Return cards to deck and cut again for first deal.')
            self.deck.deck.append(card_1)
            self.deck.deck.append(card_2)
            
    def deal_hands(self):
        if self.dealer == self.player_one:
            for i in range(6):
                self.player_one.cards.append(self.deck.deal_one())
                self.player_two.cards.append(self.deck.deal_one())
        else:
            for i in range(6):
                self.player_two.cards.append(self.deck.deal_one())
                self.player_one.cards.append(self.deck.deal_one())

    def discard_sequence(self):
        p1_discards = self.player_one.discard()
        p2_discards = self.player_two.discard()
        self.crib = p1_discards.extends(p2_discards)

    def peg_sequence(self):
        hand1 = self.player_one.cards.copy()
        hand2 = self.player_two.cards.copy()
        if self.player_one.is_dealer:
            is_p1_turn = False
        else:
            is_p1_turn = False
        

"""
def peg_sequence(is_dealer_p1,turncard,p1,p2):
    hand1 = list(p1.cards).copy()
    hand2 = list(p2.cards).copy()
    if is_dealer_p1:
        p1_turn = True
    else:
        p1_turn = False
    while hand1 or hand2:
        count = 0
        stack = []
        while count <= 31 and (can_play(hand1,count) or can_play(hand2,count)):
            if p1_turn and can_play(hand1,count):
                choice = peg_logic(hand1,stack,count,turncard)
                count += choice.value
                stack.append(choice)
                hand1.remove(choice)
                p1.score += determine_peg_points(stack,count)
                p1_played_last = True
            if can_play(hand2,count):
                choice = peg_logic(hand2,stack,count,turncard)
                count += choice.value
                stack.append(choice)
                hand2.remove(choice)
                p2.score += determine_peg_points(stack,count)
                p1_turn = True
                p1_played_last = False
            else:
                p1_turn = True
        if count < 31:
            if p1_played_last:
                p1.score += 1
            else:
                p2.score += 1

"""





class Ultimate(Cribbage):

    def __init__(self, board):
        super().__init__()



class Classic(Cribbage):

    def __init__(self):
        super().__init__()

