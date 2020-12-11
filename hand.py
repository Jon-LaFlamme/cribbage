import learning
from itertools import combinations



class hand():

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
        for key,value in ranks.items():
            if value == 2:
                points += 2
            elif value == 3:
                points += 6
            elif value == 4:
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
                for value in combination:
                    tally += value
                if tally == 15:
                    points += 2
        return points


    def points_from_flush(self):
        points = 0
        suits = self.suits.copy()
        if self.turncard:
            if self.turncard.suit in suits:
                suits[self.turncard.suit] = suits[self.turncard.suit] + 1
        for key,value in self.suits.items():
            if value > 3:
                points == value
        if self.is_crib and points < 5:
            points = 0       
        return points


    def runs_helper_three(self,list_of_three):
        default = (False,[])
        if list_of_three[2] - list_of_three[1] == 1:
            if list_of_three[1] - list_of_three[0] == 1:
                return (True,list_of_three)  
        return default      


    def runs_helper_four(self,list_of_four):
        default = (False,[])
        if list_of_four[3] - list_of_four[2] == 1:
            if list_of_four[2] - list_of_four[1] == 1:
                if list_of_four[1] - list_of_four[0] == 1:
                    return (True,list_of_four)
        else:
            return_tuple_lo = self.runs_helper_three(list_of_four[:3])
            if return_tuple_lo[0]:
                return return_tuple_lo
            else:
                return_tuple_hi = self.runs_helper_three(list_of_four[1:4])
                if return_tuple_hi[0]:
                    return return_tuple_hi 
        return default      


    def runs_helper_five(self,list_of_five): 
        default = (False,[])
        if list_of_five[4] - list_of_five[3] == 1:
            if list_of_five[3] - list_of_five[2] == 1:
                if list_of_five[2] - list_of_five[2] == 1:
                    if list_of_five[2] - list_of_five[2] == 1:
                        return (True,list_of_five)
        else:
            return_tuple_lo = self.runs_helper_four(list_of_five[:4])
            if return_tuple_lo[0]:
                return return_tuple_lo
            else:
                return_tuple_hi = self.runs_helper_four(list_of_five[1:5])
                if return_tuple_hi[0]:
                    return return_tuple_hi 
        return default

    #TODO(Jon) Optional, Convert this into a recursive algorithm or functional programming if feasible
    def points_from_runs(self):
        points = 0
        ranks = self.ranks.copy()
        return_tuple = (False,[])
        #Supports point calculation for computer discard and show sequences 
        if self.turncard:
            if self.turncard.rank not in ranks:
                ranks[self.turncard.rank] = 1
            else:
                ranks[self.turncard.rank] = ranks[self.turncard.rank] + 1
        #If not enough unique ranks in hand, runs calculation can be skipped
        if len(ranks) > 2:
            ranks_as_list = []
            sorted(ranks)
            for key,value in ranks.items():
                ranks_as_list.append(key)
            #Runs helpers check for runs of 5,4 or 3 separately
            if len(ranks_as_list) == 3:
                return_tuple = self.runs_helper_three(ranks_as_list)
            elif len(ranks_as_list) == 4:
                return_tuple = self.runs_helper_four(ranks_as_list)
            else:
                return_tuple = self.runs_helper_five(ranks_as_list)
        #Score calculated from 
        if return_tuple[0]:
            for number in return_tuple[1]:
                points += ranks[number]
                return (points, ranks)
        return (points,{})


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
        points += self.points_from_runs()[0]
        points += self.points_from_knobs()
        return points

    def optimize_by_points(self):
        cards = self.hand.copy()
        possible_hands = combinations(cards,4)
        best_hand = []
        max_score = 0
        for hand in possible_hands:
            score += self.points_from_fifteens()
            score += self.points_from_flush()
            score += self.points_from_pairs()
            score += self.points_from_runs()[0]
            if score > max_score:
                max_score = score
                best_hand = hand
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

