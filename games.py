import hand
import players
import board
import deck



class Cribbage():

    def __init__(self, game_mode, player_one, player_two, board, deck):
        self.game_mode = game_mode      #self.game_mode = 'vs_human', 'computer_easy', 'computer_med', 'computer_hard'
        self.game_not_over = True
        self.player_one = player_one    #players.Player() object
        self.player_two = player_two
        self.board = board              #board.Board() object
        self.deck = deck                #deck.Deck() object
        self.peg_count = None
        self.crib = []
        self.turncard

    

    def update_board(self):
        if self.player_one.score >= 121 or self.player_two.score >= 121:
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
        if self.player_one.is_dealer:
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
                self.update_board()
        else:
            self.turncard = self.player_one.cut_deck(self.deck)
            if self.turncard.rankname == 'jack':
                self.player_two.score += 2
                self.update_board()


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
                    self.update_board()
                    p1_played_last = True
                    if not self.game_not_over:
                        break
                if self.player_two.can_peg(self.peg_count):
                    selected = self.player_two.peg_one(self.peg_count)
                    self.player_two.cards.remove(selected)
                    stack.hand.append(selected)
                    self.peg_count += selected.value
                    self.player_two.score += stack.determine_peg_points(self.peg_count)
                    self.update_board():
                    if not self.game_not_over:
                        break
                    p1_played_last = False
                else:
                    is_p1_turn = True
            if self.peg_count < 31:
                if p1_played_last:
                    self.player_one.score += 1
                else:
                    self.player_two.score += 1
            if not self.game_not_over:
                break
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
            if self.game_not_over:
                self.player_one.score += h1_pts
            if self.game_not_over:
                self.player_one.score += cr_pts
        else:
            self.player_one.score += h1_pts
            if self.game_not_over:
                self.player_two.score +=  h2_pts
            if self.game_not_over:
                self.player_two.score += cr_pts


    def cleanup(self):
        self.deck.append(self.turncard)
        self.deck.extend(self.player_one.cards)
        self.deck.extend(self.player_two.cards)
        self.deck.extend(self.crib)
        self.deck.shuffle()
        
    def end_sequence(self):
        # MATCH_TEMPLATE = {'win': 0, 'was_skunked': 0, 'was_dbl_skunked': 0, 'skunked_opponent': 0, 'dbl_skunked_oppenent': 0}
        if self.player_one.score >= 121:
            print(f'{self.player_one.name} wins!')
            self.player_one.user.game_stats['win'] += 1
            if self.player_two.score < 61:
                self.player_one.user.game_stats['dbl_skunked_opponent'] += 1
                self.player_two.user.game_stats['was_dbl_skunked'] += 1
            elif self.player_two.score < 91:
                self.player_one.user.game_stats['skunked_opponent'] += 1
                self.player_two.user.game_stats['was_skunked'] += 1
        else:
            print(f'{self.player_two.name} wins!')
            self.player_two.user.game_stats['win'] += 1
            if self.player_one.score < 61:
                self.player_two.user.game_stats['dbl_skunked_opponent'] += 1
                self.player_one.user.game_stats['was_dbl_skunked'] += 1
            elif self.player_one.score < 91:
                self.player_two.user.game_stats['skunked_opponent'] += 1
                self.player_one.user.game_stats['was_skunked'] += 1
        #update user stats
        self.player_one.user.update_profile(self.game_mode)
        self.player_two.user.update_profile(self.game_mode)
        self.player_one.user.save_profile()
        self.player_two.user.save_profile()
        #end the game
        self.game_not_over = False


    def game_driver(self):    
        #TODO(Jon) Put everything together in a while loop
        self.determine_dealer_sequence()
        while self.game_not_over:
            self.deal_sequence()
            self.discard_sequence()
            self.turncard_sequence()
            if self.game_not_over:
                self.peg_sequence()
            if self.game_not_over:
                self.show_sequence()
            if self.game_not_over:
                self.cleanup()


class Ultimate(Cribbage):

    def __init__(self, board):
        super().__init__()



class Classic(Cribbage):

    def __init__(self):
        super().__init__()

