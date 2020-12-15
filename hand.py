import learning
from itertools import combinations



class Hand():

    def __init__(self,list_of_cards, is_crib=False, turncard=None):
        self.hand = list_of_cards
        self.turncard = turncard
        self.is_crib = is_crib
        self.values = []
        self.ranks = {}
        self.suits = {}
    
        for card in self.hand:  
            self.values.append(card.value)
            if card.rank not in self.ranks:
                self.ranks[card.rank] = 1
            else:
                self.ranks[card.rank] = self.ranks[card.rank] + 1
            if card.suit not in self.suits:
                self.suits[card.suit] = 1
            else:
                self.suits[card.suit] = self.suits[card.suit] + 1


    def points_from_pairs(self):
        points = 0
        ranks = self.ranks.copy()
        if self.turncard:
            if self.turncard.rank not in ranks:
                ranks[self.turncard.rank] = 1
            else:
                ranks[self.turncard.rank] = ranks[self.turncard.rank] + 1
        for key in ranks.keys():
            if ranks[key] == 2:
                points += 2
            elif ranks[key] == 3:
                points += 6
            elif ranks[key] == 4:
                points += 12
        return points


    def points_from_fifteens(self):
        points = 0
        collection = []
        if self.turncard:
            hand = self.hand.copy()
            hand.append(self.turncard)
            fives = combinations(hand,5)
            fours = combinations(hand,4)
            threes = combinations(hand,3)
            twos = combinations(hand,2)
            collection = [fives,fours,threes,twos]
        else:
            fours = combinations(self.hand,4)
            threes = combinations(self.hand,3)
            twos = combinations(self.hand,2)
            collection = [fours,threes,twos]
        for denomination in collection:
            for combination in denomination:
                tally = 0
                for card in combination:
                    tally += card.value
                if tally == 15:
                    points += 2
        return points


    def points_from_flush(self):
        points = 0
        suits = self.suits.copy()
        if self.turncard:
            if self.turncard.suit in suits:
                suits[self.turncard.suit] = suits[self.turncard.suit] + 1
        for key,value in suits.items():
            if value > 3:
                points = value
        if self.is_crib and points < 5:
            points = 0       
        return points


    def points_from_runs(self):
        is_run = False
        ranks = self.ranks.copy()
        if self.turncard:
            if self.turncard.rank in ranks:
                ranks[self.turncard.rank] = ranks[self.turncard.rank] + 1 
            else:
                ranks[self.turncard.rank] = 1
        #Early exit condition if fewer than 3 unique ranks
        if len(ranks) < 3:
            return 0
        rank_list = []
        for key in ranks.keys():
            rank_list.append(key)
        rank_list.sort()

        #Create hash tables and keys to quickly identify run sequences in hand
        three = {'1-2-3','2-3-4','3-4-5','4-5-6','5-6-7','6-7-8','7-8-9','8-9-10','9-10-11','10-11-12','11-12-13'}
        four = {'1-2-3-4','2-3-4-5','3-4-5-6','4-5-6-7','5-6-7-8','6-7-8-9','7-8-9-10','8-9-10-11','9-10-11-12','10-11-12-13'}
        five = {'1-2-3-4-5','2-3-4-5-6','3-4-5-6-7','4-5-6-7-8','5-6-7-8-9','6-7-8-9-10','7-8-9-10-11','8-9-10-11-12','9-10-11-12-13'}
        if len(rank_list) == 5:
            hash_5 = f'{rank_list[0]}-{rank_list[1]}-{rank_list[2]}-{rank_list[3]}-{rank_list[4]}'
            hash_4_hi = f'{rank_list[1]}-{rank_list[2]}-{rank_list[3]}-{rank_list[4]}'
            hash_3_hi = f'{rank_list[2]}-{rank_list[3]}-{rank_list[4]}'
        if len(rank_list) >= 4:
            hash_4_lo = f'{rank_list[0]}-{rank_list[1]}-{rank_list[2]}-{rank_list[3]}'     
            hash_3_mi = f'{rank_list[1]}-{rank_list[2]}-{rank_list[3]}' 
        if len(rank_list) >= 3:
            hash_3_lo = f'{rank_list[0]}-{rank_list[1]}-{rank_list[2]}'

        #Peform lookups and store the keys that get hits inside 'run' variable
        run = []
        if len(rank_list) == 5:
            if hash_5 in five:
                return 5
            elif hash_4_hi in four:
                run = rank_list[1:]
                is_run = True
            elif hash_3_hi in three:
                run = rank_list[2:]
                is_run = True
        if len(rank_list) >= 4 and not is_run:
            if hash_4_lo in four:
                run = rank_list[:4]
                is_run = True
            elif hash_3_mi in three:
                run = rank_list[1:4]
                is_run = True
            elif hash_3_lo in three:
                run = rank_list[:3]
                is_run = True
        elif not is_run and hash_3_lo in three:
            run = rank_list[:3]
            is_run = True
        if not is_run:
            return 0

        #Determine if single, double, double-double, triple runs exist
        if len(run) == 4:
            for rank in run:
                if ranks[rank] == 2:
                    return 8
            return 4
        if len(run) == 3:
            num_pairs = 0
            for rank in run:
                if ranks[rank] == 3:
                    return 9
                elif ranks[rank] == 2:
                    num_pairs += 1
            if num_pairs == 2:
                return 12
            elif num_pairs == 1:
                return 6
            else:
                return 3


    def points_from_knobs(self):
        points = 0
        if 11 in self.ranks and self.turncard:
            for card in self.hand:
                if card.rank == 11 and card.suit == self.turncard.suit:
                    points += 1
        return points
    

    def compute_score(self):
        points = 0
        points += self.points_from_fifteens()
        points += self.points_from_flush()
        points += self.points_from_pairs()
        points += self.points_from_runs()
        points += self.points_from_knobs()
        return points


    def optimize_by_points(self):
        cards = self.hand.copy()
        possible_hands = combinations(cards,4)
        best_hand = []
        max_score = 0
        score = 0
        for combo in possible_hands:
            h = Hand(combo)
            score = h.compute_score()
            if score > max_score:
                max_score = score
                best_hand = combo
        return best_hand


    def optimize_statistically(self):
        cards = self.hand.copy()
        hand_scores = {}
        possible_hands = combinations(cards,4)
        for hand in possible_hands:
            hand_id = learning.hand_id(hand)
            hand_scores[hand_id] = learning.performance_by_hand[hand_id]
        ordered_hand_id = sorted(hand_scores.items(), key=lambda x: x[1],reverse=True)
        best_hand = ordered_hand_id[0]
        return best_hand


    def peg_selection_lead(self,turncard):
        #Check if there is a pair. If so, lead one of the cards in the pair
        for key,value in self.ranks.items():
            if value > 1:
                for card in self.hand:
                    if card.rank == key:
                        return card
        #Otherwise, match the turncard 
        for card in self.hand:
            if card.rank == turncard.rank:
                return card
        #Otherwise, avoid playing fives
        for card in self.hand:
            if card.rank != 5:
                return card
        #If no other choices, select the first card
        return self.hand[0]


    def peg_selection(self,stack,count,turncard):
        #route to lead-off method if count is zero
        if count == 0:
            return self.peg_selection_lead(turncard)
        #check for three or four of a kind
        if len(stack) > 2:
            for key,value in self.ranks.items():
                if value > 2:
                    for card in self.hand:
                        if card.rank == key and key + count <= 31:
                            return card
        #check for a run
        hand_copy = self.hand.copy()
        for card in self.hand:
            self.hand = stack.copy()
            self.hand.append(card)
            return_tuple = self.points_from_runs()
            if return_tuple[0]:
                self.hand = hand_copy.copy()
                return card
        self.hand = hand_copy.copy
        #check for a fifteen or 31
        for card in self.hand:
            if card.value + count == 15 or card.value + count == 31:
                return card
        #check for a single pair
        for unplayed_card in self.hand:
            for played_card in stack:
                if unplayed_card.rank == played_card.rank and unplayed_card.rank + count <= 31:
                    return unplayed_card
        #finally, play first card under 31
        for card in self.hand:
            if card.rank + count < 31:
                return card


                        


