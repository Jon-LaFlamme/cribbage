
class BoardMember():

    def __init__(name):
        self.name = name
        self.lead_peg = -1
        self.hind_peg = -1

class Board():


    def __init__(name_one, name_two):
        self.player_one = BoardMember(name_one)
        self.player_two = BoardMember(name_two)

    def update_pegs(name, score):
        if self.player_one.name == name and score > self.player_one.lead_peg:
            lane = 1
            temp = self.player_one.hind_heg
            self.player_one.hind_peg = self.player_one.lead_peg
            self.player_one.lead_peg = score
            update_board(lane, temp, score)
        if self.player_two.name == name and score > self.player_two.lead_peg:
            lane = 2
            temp = self.player_two.hind_heg
            self.player_two.hind_peg = self.player_two.lead_peg
            self.player_two.lead_peg = score
            update_board(lane, temp, score)

    def update_board(lane, old, new):
        pass

    def display_board():
        pass

class Classic(Board):

    def __init__():
        self.mapper = {'0':1,'1':3,'2':4,'3':5,'4':6,'5':7,'6':9,'7':10,'8':11,'9':12,'10':13,
                        '11':15,'12':16,'13':17,'14':18,'15':19,'16':21,'17':22,'18':23,'19':24,'20':25,
                        '21':27,'22':28,'23':29,'24':30,'25':31,'26':33,'27':34,'28':35,'29':36,'30':37}
        #Lane 1: 4, Lane 2: 7, Lane 3: 28, Lane 4: 31
        self.display = [[f'{self.player_one.name}: {self.player_one.lead_peg}  vs {self.player_two.name}: {self.player_two.lead_peg}\n'],
                        ['    o  o         ||         o  o    '],
                        ['===================================='],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['===================================='],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['===================================='],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['===================================='],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['===================================='],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['===================================='],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['    o  o         ||         o  o    '],
                        ['====================================']]
    

    def update_board(lane, old, new):
        old_row = self.mapper(str(old))
        new_row = self.mapper(str(new))
        if (old > 0 and old < 31) and (old > 60 and old < 91): 
            if lane == 1: 
                old_col = 4
            else: 
                old_col = 28
        else:
            if lane == 2: 
                old_col = 7
            else: 
                old_col = 31
        if (new > 0 and new < 31) and (new > 60 and new < 91):
            if lane == 1: 
                new_col = 4
            else: 
                new_col = 28
        else:
            if lane == 2: new_col = 7
            else: new_col = 31
        self.display[old_row][old_col] = 'o'
        self.display[new_row][new_col] = '+'


    def display_board():
        for line in self.display:
            print(line)


    class Four_Person(Classic):

        def __init__():
            pass

    class Three_Person(Classic):

        def __init__():
            pass

class Ultimate(Board):

    def __init__():
        pass


