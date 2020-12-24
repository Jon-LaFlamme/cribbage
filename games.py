import hand
import players
import board
import deck
import verbose



class Cribbage():

    def __init__(self, player_one, player_two): 
        self.player_one = player_one    #players.Player() object
        self.player_two = player_two    
        self.board = board.Classic(self.player_one, self.player_two)             
        self.deck = deck.Deck()      
        self.game_not_over = True
        self.peg_count = 0
        self.crib = []
        self.turncard = None


    def update_board(self):
        if self.player_one.score >= 121 or self.player_two.score >= 121:
            self.end_sequence()
        else: 
            self.board.update_pegs()
        

    def determine_dealer_sequence(self):
        verbose.start_game(self.player_one, self.player_two)
        verbose.cut_for_deal()
        #lower cut wins the deal
        undetermined = True
        while undetermined:
            card_1 = self.player_one.cut_deck(self.deck, for_first_deal=True)
            verbose.cuts_card(self.player_one, card_1)
            card_2 = self.player_two.cut_deck(self.deck, for_first_deal=True)
            verbose.cuts_card(self.player_two, card_2)
            if card_1.rank < card_2.rank:
                self.player_one.is_dealer = True
                verbose.win_first_deal(self.player_one)
                undetermined = False
            elif card_2.rank < card_1.rank:
                self.player_two.is_dealer = True
                verbose.win_first_deal(self.player_two)
                undetermined = False
            else:
                print('Tie! Return cards to deck and cut again for first deal.')
            self.deck.deck.append(card_1)
            self.deck.deck.append(card_2)


    def deal_sequence(self):
        if self.player_one.is_dealer:
            verbose.dealing(self.player_one)
            for i in range(6):
                self.player_one.cards.append(self.deck.deal_one())
                self.player_two.cards.append(self.deck.deal_one())
        else:
            verbose.dealing(self.player_two)
            for i in range(6):
                self.player_two.cards.append(self.deck.deal_one())
                self.player_one.cards.append(self.deck.deal_one())


    def discard_sequence(self):
        p1_discards = self.player_one.discard()
        verbose.discard(self.player_one)
        p2_discards = self.player_two.discard()
        verbose.discard(self.player_two)
        p1_discards.extend(p2_discards)
        self.crib = p1_discards


    def turncard_sequence(self):
        if self.player_one.is_dealer:
            self.player_two.cut_deck(self.deck)
            self.turncard = self.deck.deal_one()
            verbose.turncard(self.player_two, self.player_one, self.turncard)
            if self.turncard.rankname == 'jack':
                self.player_one.score += 2
                verbose.heels(self.player_one, self.turncard)
                self.update_board()
        else:
            self.player_one.cut_deck(self.deck)
            self.turncard = self.deck.deal_one()
            verbose.turncard(self.player_one, self.player_two, self.turncard)
            if self.turncard.rankname == 'jack':
                self.player_two.score += 2
                verbose.heels(self.player_two, self.turncard)
                self.update_board()


    def peg_sequence(self):
        verbose.pegging()
        #temporary copy to restore player.cards to original state after peg_sequence() is complete
        hand1 = self.player_one.cards.copy()
        print('player one hand')
        self.player_one.display_hand()
        hand2 = self.player_two.cards.copy()
        print('player two hand')
        self.player_two.display_hand()
        if self.player_one.is_dealer:
            is_p1_turn = False
        else:
            is_p1_turn = False
        
        while self.player_one.cards or self.player_two.cards:
            self.peg_count = 0
            stack = hand.Hand([], turncard=self.turncard)
            while self.peg_count <= 31 and (self.player_one.can_peg(self.peg_count) or self.player_two.can_peg(self.peg_count)):
                if is_p1_turn and self.player_one.can_peg(self.peg_count):
                    selected = self.player_one.peg_one(stack.hand, self.peg_count, self.turncard)
                    self.player_one.cards.remove(selected)
                    stack.hand.append(selected)
                    self.peg_count += selected.value
                    verbose.peg_one(self.player_one, selected, self.peg_count)
                    peg_points = stack.determine_peg_points(self.peg_count)
                    if peg_points > 0:
                        verbose.peg_points(self.player_one, peg_points)
                    self.player_one.score += peg_points
                    self.update_board()
                    is_p1_turn = False
                    p1_played_last = True
                    if not self.game_not_over:
                        break
                if self.player_two.can_peg(self.peg_count):
                    selected = self.player_two.peg_one(stack.hand, self.peg_count, self.turncard)
                    self.player_two.cards.remove(selected)
                    stack.hand.append(selected)
                    self.peg_count += selected.value
                    verbose.peg_one(self.player_two, selected, self.peg_count)
                    peg_points = stack.determine_peg_points(self.peg_count)
                    if peg_points > 0:
                        verbose.peg_points(self.player_two, peg_points)
                    self.player_two.score += peg_points
                    self.update_board()
                    if not self.game_not_over:
                        break
                    p1_played_last = False
                    is_p1_turn = True
                else:
                    is_p1_turn = True
            if self.peg_count < 31:
                if p1_played_last:
                    verbose.peg_go(self.player_one)
                    self.player_one.score += 1
                    self.update_board()
                else:
                    verbose.peg_go(self.player_two)
                    self.player_two.score += 1
                    self.update_board()
            if not self.game_not_over:
                break
        self.player_one.cards = hand1
        self.player_two.cards = hand2


    def show_sequence(self):
        verbose.counting()
        h1 = hand.Hand(self.player_one.cards, turncard=self.turncard)
        h2 = hand.Hand(self.player_two.cards, turncard=self.turncard)
        cr = hand.Hand(self.crib, turncard=self.turncard, is_crib=True)
        print('player one hand')
        self.player_one.display_hand()
        print('player two hand')
        self.player_two.display_hand()
        print('crib')
        for card in cr.hand:
            print(card.name)
        h1_pts = h1.compute_score()
        h2_pts = h2.compute_score()
        cr_pts = cr.compute_score()

        if self.player_one.is_dealer:
            verbose.score_hand(self.player_two, h2_pts)
            self.player_two.score +=  h2_pts
            self.update_board()
            if self.game_not_over:
                verbose.score_hand(self.player_one, h1_pts)
                self.player_one.score += h1_pts
                self.update_board()
            if self.game_not_over:
                verbose.score_hand(self.player_one, cr_pts, is_crib=True)
                self.player_one.score += cr_pts
                self.update_board()
        else:
            verbose.score_hand(self.player_one, h1_pts)
            self.player_one.score += h1_pts
            self.update_board()
            if self.game_not_over:
                verbose.score_hand(self.player_two, h2_pts)
                self.player_two.score +=  h2_pts
                self.update_board()
            if self.game_not_over:
                verbose.score_hand(self.player_two, cr_pts, is_crib=True)
                self.player_two.score += cr_pts
                self.update_board()


    def cleanup(self):
        verbose.new_round()
        self.deck.deck.append(self.turncard)
        self.deck.deck.extend(self.player_one.cards)
        self.deck.deck.extend(self.player_two.cards)
        self.deck.deck.extend(self.crib)
        self.player_one.cards = []
        self.player_two.cards = []
        self.crib = []
        self.deck.shuffle()

        

    def end_sequence(self):
        # MATCH_TEMPLATE = {'win': 0, 'was_skunked': 0, 'was_dbl_skunked': 0, 'skunked_opponent': 0, 'dbl_skunked_oppenent': 0}
        if self.player_one.score >= 121:
            print(f'{self.player_one.name} wins!')
            if isinstance(self.player_one, players.Human):
                self.player_one.user.game_stats['win'] += 1
                if self.player_two.score < 61:
                    self.player_one.user.game_stats['dbl_skunked_opponent'] += 1
                    self.player_two.user.game_stats['was_dbl_skunked'] += 1
                elif self.player_two.score < 91:
                    self.player_one.user.game_stats['skunked_opponent'] += 1
                    self.player_two.user.game_stats['was_skunked'] += 1
        else:
            print(f'{self.player_two.name} wins!')
            if isinstance(self.player_two, players.Human):
                self.player_two.user.game_stats['win'] += 1
                if self.player_one.score < 61:
                    self.player_two.user.game_stats['dbl_skunked_opponent'] += 1
                    self.player_one.user.game_stats['was_dbl_skunked'] += 1
                elif self.player_one.score < 91:
                    self.player_two.user.game_stats['skunked_opponent'] += 1
                    self.player_one.user.game_stats['was_skunked'] += 1
        #update user stats
        if isinstance(self.player_one, players.Human):
            self.player_one.user.update_profile()
            self.player_two.user.save_profile()     
        if isinstance(self.player_two, players.Human):
            self.player_two.user.update_profile()
            self.player_one.user.save_profile()
            
        #end the game
        self.game_not_over = False


    def game_driver(self):    
        #TODO(Jon) Put everything together in a while loop
        self.deck.shuffle()
        self.determine_dealer_sequence()
        while self.game_not_over:
            self.deal_sequence()
            self.discard_sequence()
            self.turncard_sequence()
            self.board.display_board()
            if self.game_not_over:
                self.peg_sequence()
            self.board.display_board()
            if self.game_not_over:
                self.show_sequence()
            self.board.display_board()
            if self.game_not_over:
                self.cleanup()
            self.board.display_board()


class Ultimate(Cribbage):

    def __init__(self, board):
        super().__init__()



class Classic(Cribbage):

    def __init__(self):
        super().__init__()

