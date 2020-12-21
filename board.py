
class Board():


    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_one
        self.lane1_lead_peg = 0
        self.lane1_hind_peg = 0
        self.lane2_lead_peg = 0
        self.lane2_hind_peg = 0

    def update_pegs(self): 
        if self.lane1_lead_peg != self.player_one.score:
            vacant = self.lane1_hind_peg
            self.lane1_hind_peg = self.lane1_lead_peg
            self.land1_lead_peg = self.player_one.score
            self.update_board(vacant)
        elif self.lane2_lead_peg != self.player_two.score:
            vacant = self.lane2_hind_peg
            self.lane2_hind_peg = self.lane2_lead_peg
            self.land1_lead_peg = self.player_two.score
            self.update_board(vacant)


    def display_board(self):
        pass

class Classic(Board):

    def __init__(self, player_one, player_two):
        super().__init__(player_one, player_two)
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
    


    def update_board(self, vacant):
        #determine Lane 1 positions: out: 4, back: 7
        if vacant != self.lane1_hind_peg:
            old_row = self.mapper[str(vacant)]
            new_row = self.mapper[str(self.lane1_lead_peg)]
            if vacant in range(0,30) or vacant in range(60,122):
                old_col = 4
            else:
                old_col = 7
            if self.lane1_lead_peg in range(0,30) or self.lane1_lead_peg in range(60,122):
                new_col = 4
            else:
                new_col = 7
        #determine lane 2 positions: out: 31, back 28
        elif vacant != self.lane2_hind_peg:
                        old_row = self.mapper[str(vacant)]
            new_row = self.mapper[str(self.lane1_lead_peg)]
            if vacant in range(0,30) or vacant in range(60,122):
                old_col = 31
            else:
                old_col = 28
            if self.lane1_lead_peg in range(0,30) or self.lane1_lead_peg in range(60,122):
                new_col = 31
            else:
                new_col = 28
        #update self.display
        self.display[old_row] = self.display[old_row][:old_col] + 'o' + self.display[old_row][old_col + 1:]
        self.display[new_row] = self.display[new_row][:new_col] + '+' + self.display[new_row][new_col + 1:]
        #self.display[0] = f'        {self.player_one.name}: {self.player_one.lead_peg}   vs   {self.player_two.name}: {self.player_two.lead_peg}\n'


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


