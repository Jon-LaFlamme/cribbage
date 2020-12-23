import players
import users


class Board():


    def __init__(self, player_one=None, player_two=None):
        self.player_one = player_one
        self.player_two = player_two
        self.lane1_lead_peg = 0
        self.lane1_hind_peg = 0
        self.lane2_lead_peg = 0
        self.lane2_hind_peg = 0

    def update_pegs(self): 
        self.display[0] = f'{self.player_one.name}: {self.player_one.score}   vs   {self.player_two.name}: {self.player_two.score}\n'
        if self.lane1_lead_peg != self.player_one.score:
            vacant = self.lane1_hind_peg
            self.lane1_hind_peg = self.lane1_lead_peg
            self.lane1_lead_peg = self.player_one.score
            self.update_board(vacant=vacant, lane=1)
        elif self.lane2_lead_peg != self.player_two.score:
            vacant = self.lane2_hind_peg
            self.lane2_hind_peg = self.lane2_lead_peg
            self.lane2_lead_peg = self.player_two.score
            self.update_board(vacant=vacant, lane=2)


    def display_board(self):
        pass

class Classic(Board):

    def __init__(self, player_one=None, player_two=None):
        super().__init__(player_one=None, player_two=None)
        self.mapper = {'0':1,'1':3,'2':4,'3':5,'4':6,'5':7,'6':9,'7':10,'8':11,'9':12,'10':13,
                        '11':15,'12':16,'13':17,'14':18,'15':19,'16':21,'17':22,'18':23,'19':24,'20':25,
                        '21':27,'22':28,'23':29,'24':30,'25':31,'26':33,'27':34,'28':35,'29':36,'30':37,
                        '31':37,'32':36,'33':35,'34':34,'35':33,'36':31,'37':30,'38':29,'39':28,'40':27,
                        '41':25,'42':24,'43':23,'44':22,'45':21,'46':19,'47':18,'48':17,'49':16,'50':15,
                        '51':13,'52':12,'53':11,'54':10,'55':9,'56':7,'57':6,'58':5,'59':4,'60':3,

                        '61':3,'62':4,'63':5,'64':6,'65':7,'66':9,'67':10,'68':11,'69':12,'70':13,
                        '71':15,'72':16,'73':17,'74':18,'75':19,'76':21,'77':22,'78':23,'79':24,'80':25,
                        '81':27,'82':28,'83':29,'84':30,'85':31,'86':33,'87':34,'88':35,'89':36,'90':37,
                        '91':37,'92':36,'93':35,'94':34,'95':33,'96':31,'97':30,'98':29,'99':28,'100':27,
                        '101':25,'102':24,'103':23,'104':22,'105':21,'106':19,'107':18,'108':17,'109':16,'110':15,
                        '111':13,'112':12,'113':11,'114':10,'115':9,'116':7,'117':6,'118':5,'119':4,'120':3,'121':1}

        self.display = [f'{self.player_one.name}: {self.player_one.score}   vs   {self.player_two.name}: {self.player_two.score}\n',
                        '    +  o         ||         o  +    ',
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
    


    def update_board(self, vacant=None, lane=None):
        #determine Lane 1 positions: out: 4, back: 7
        if lane == 1:
            old_row = self.mapper[str(vacant)]
            new_row = self.mapper[str(self.lane1_lead_peg)]
            if vacant in range(0,31) or vacant in range(61,122):
                old_col = 4
            else:
                old_col = 7
            if self.lane1_lead_peg in range(0,31) or self.lane1_lead_peg in range(61,122):
                new_col = 4
            else:
                new_col = 7
        #determine lane 2 positions: out: 31, back 28
        elif lane == 2:
            old_row = self.mapper[str(vacant)]
            new_row = self.mapper[str(self.lane2_lead_peg)]
            if vacant in range(0,31) or vacant in range(61,122):
                old_col = 31
            else:
                old_col = 28
            if self.lane1_lead_peg in range(0,31) or self.lane1_lead_peg in range(61,122):
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


