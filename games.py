import hand
import players
import board
import deck



class Cribbage():

    def __init__(self, player_one, player_two, board, deck):
        self.player_one = player_one    #players.Player() object
        self.player_two = player_two
        self.board = board              #board.Board() object
        self.deck = deck                #deck.Deck() object
        self.peg_count = None
        self.crib = []
        self.turncard

    

    def update_board(self):
        if self.player_one.score >= 121 or self.player_two.score >= 121 :
            self.end_sequence()
        else: 
            self.board.update_pegs()
        

    def determine_dealer_sequence(self):
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
            
    def deal_sequence(self):
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

    def turncard_sequence(self):
        if self.player_one.is_dealer:
            self.turncard = self.player_two.cut_deck(self.deck)
            if self.turncard.rankname == 'jack':
                self.player_one.score += 2
        else:
            self.turncard = self.player_one.cut_deck(self.deck)
            if self.turncard.rankname == 'jack':
                self.player_two.score += 2


    def peg_sequence(self):
        #temporary copy to restore player.cards to original state after peg_sequence() is complete
        hand1 = self.player_one.cards.copy()
        hand2 = self.player_two.cards.copy()
        if self.player_one.is_dealer:
            is_p1_turn = False
        else:
            is_p1_turn = False
        
        while self.player_one.cards or self.player_two.cards:
            self.peg_count = 0
            stack = hand.Hand([])
            while self.peg_count <= 31 and (self.player_one.can_peg(self.peg_count) or self.player_two.can_peg(self.peg_count)):
                if is_p1_turn and self.player_one.can_peg(self.peg_count):
                    selected = self.player_one.peg_one(self.peg_count)
                    self.player_one.cards.remove(selected)
                    stack.hand.append(selected)
                    self.peg_count += selected.value
                    self.player_one.score += stack.determine_peg_points(self.peg_count)
                    p1_played_last = True
                if self.player_two.can_peg(self.peg_count):
                    selected = self.player_two.peg_one(self.peg_count)
                    self.player_two.cards.remove(selected)
                    stack.hand.append(selected)
                    self.peg_count += selected.value
                    self.player_two.score += stack.determine_peg_points(self.peg_count)
                    p1_played_last = False
                else:
                    is_p1_turn = True
            if self.peg_count < 31:
                if p1_played_last:
                    self.player_one.score += 1
                else:
                    self.player_two.score += 1
        self.player_one.cards = hand1
        self.player_two.cards = hand2


    def show_sequence(self):
        h1 = hand.Hand(self.player_one.cards, turncard=self.turncard)
        h2 = hand.Hand(self.player_two.cards, turncard=self.turncard)
        cr = hand.Hand(self.crib, turncard=self.turncard, is_crib=True)
        h1_pts = h1.compute_score()
        h2_pts = h2.compute_score()
        cr_pts = cr.compute_score()

        if self.player_one.is_dealer:
           self.player_two.score +=  h2_pts
           self.player_one.score += h1_pts
           self.player_one.score += cr_pts
        else:
            self.player_one.score += h1_pts
            self.player_two.score +=  h2_pts
            self.player_two.score += cr_pts

    def cleanup(self):
        self.deck.append(self.turncard)
        self.deck.extend(self.player_one.cards)
        self.deck.extend(self.player_two.cards)
        self.deck.extend(self.crib)
        self.deck.shuffle()
        
    def end_sequence(self):
        #TODO(Jon) There is a winner. Exit the game

    def game_driver(self):    
        #TODO(Jon) Put everything together in a while loop


class Ultimate(Cribbage):

    def __init__(self, board):
        super().__init__()



class Classic(Cribbage):

    def __init__(self):
        super().__init__()

