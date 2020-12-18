
class BoardMember():

    def __init__(self,name):
        self.name = name
        self.lead_peg = 0
        self.hind_peg = 0

class Board():


    def __init__(self,name_one, name_two):
        self.player_one = BoardMember(name_one)
        self.player_two = BoardMember(name_two)

    def update_pegs(self, name, score):
        if score >= 121:
            print(f' ******* {name} WINS! ******** ')
        else:
            if self.player_one.name == name and score > self.player_one.lead_peg:
                lane = 1
                vacant = self.player_one.hind_peg
                self.player_one.hind_peg = self.player_one.lead_peg
                self.player_one.lead_peg = score
                self.update_board(lane, vacant, score)
            if self.player_two.name == name and score > self.player_two.lead_peg:
                lane = 2
                vacant = self.player_two.hind_peg
                self.player_two.hind_peg = self.player_two.lead_peg
                self.player_two.lead_peg = score
                self.update_board(lane, vacant, score)

    def update_board(self, lane, old, new):
        pass

    def display_board(self):
        pass

class Classic(Board):

    def __init__(self, name1, name2):
        super().__init__(name1, name2)
        self.mapper = {'0':1,'1':3,'2':4,'3':5,'4':6,'5':7,'6':9,'7':10,'8':11,'9':12,'10':13,
                        '11':15,'12':16,'13':17,'14':18,'15':19,'16':21,'17':22,'18':23,'19':24,'20':25,
                        '21':27,'22':28,'23':29,'24':30,'25':31,'26':33,'27':34,'28':35,'29':36,'30':37}
        self.display = [f'        {self.player_one.name}: {self.player_one.lead_peg}   vs   {self.player_two.name}: {self.player_two.lead_peg}\n',
                        '    +  o         ||         +  o    ',
                        '====================================',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '====================================',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '====================================',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '====================================',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '====================================',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '====================================',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '    o  o         ||         o  o    ',
                        '====================================']
    


    def update_board(self, lane, old, new):

        old_row = self.mapper[str(old)]
        new_row = self.mapper[str(new)]
        #Lane 1 left-out: 4, Lane 1 left-back: 7, Lane 2 right-out: 28, Lane 2: right-back 31
        if (old > -1 and old < 31) or (old > 60 and old < 91): 
            if lane == 1: 
                old_col = 4
            else: 
                old_col = 28
        else:
            if lane == 2: 
                old_col = 7
            else: 
                old_col = 31
        if (new > -1 and new < 31) or (new > 60 and new < 91):
            if lane == 1: 
                new_col = 4
            else: 
                new_col = 28
        else:
            if lane == 2: 
                new_col = 7
            else: 
                new_col = 31
        self.display[old_row] = self.display[old_row][:old_col] + 'o' + self.display[old_row][old_col + 1:]
        self.display[new_row] = self.display[new_row][:new_col] + '+' + self.display[new_row][new_col + 1:]
        self.display[0] = f'        {self.player_one.name}: {self.player_one.lead_peg}   vs   {self.player_two.name}: {self.player_two.lead_peg}\n'


    def display_board(self):
        for line in self.display:
            print(line)


class Four_Person(Classic):

    def __init__(self):
        pass

class Three_Person(Classic):

    def __init__(self):
        pass

class Ultimate(Board):

    def __init__(self):
        pass


