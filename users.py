#TODO(Jon) This module will require online components for production, but will be locally implemented in this package
import os

MATCH_TEMPLATE = {'win': 0, 'was_skunked': 0, 'was_dbl_sunked': 0, 'skunked_opponent': 0, 'dbl_skunked_oppenent': 0}

PROFILE_TEMPLATE = {'email': 'none',
                    'rank': 0,
                    'credits': 0,
                    'badges': {'win_streak_3': 0,    #0: not achieved, #1 achieved on easy, #2 achieved on medium, #3 achieved on hard
                            'hand_of_eight': 0,
                            'hand_of_twelve': 0,
                            'hand_of_sixteen': 0,
                            'hand_of_twenty': 0,
                            'hand_of_twenty-four': 0,
                            'hand_of_twenty-eight': 0,
                            'hand_of_twenty-nine': 0,
                            'peg_five': 0,
                            'peg_eight': 0,
                            'peg_twelve': 0,
                            'three_skunks': 0,
                            'three_dbl_skunks': 0,
                            'rank_status': 0,},     #0: beginner,  #1: intermediate,  #2: advanced,  #3: elite
                    'unlocked_boards': {'classic_1': 0,'ultimate_1': 0},  #0: not won, #1 won on easy, #2 won on medium, #3 won on hard   
                    'vs_humans': {'skunks':0,'skunked':0,'dbl_skunks':0,'dbl_skunked':0,'wins':0,'losses':0},
                    'computer_easy': {'skunks':0,'skunked':0,'dbl_skunks':0,'dbl_skunked':0,'wins':0,'losses':0},
                    'computer_med': {'skunks':0,'skunked':0,'dbl_skunks':0,'dbl_skunked':0,'wins':0,'losses':0},
                    'computer_hard': {'skunks':0,'skunked':0,'dbl_skunks':0,'dbl_skunked':0,'wins':0,'losses':0}
                    }

#Found but not authenticated: 'fna',  Found and authenticated: 'fa',  Not found: 'nf'
def lookup_user(username, email):
    with open('user_directory.json','r') as f:
        user_directory = json.load(f)
        if username in user_directory:
            if user_directory[username]['email'] == email:
                return 'fa'
            else:
                return 'fna'
        else:
            return 'nf'


def add_user(username, email):
    with open('user_directory.json','r') as f:
        user_directory = json.load(f)
    user_directory[username] = {'email': email, 'rank': 0} 
    with open('user_directory.json', 'w') as f:
        json.dump(user_directory, f)


class User():

    def __init__(self, username, email):
        self.name = username
        self.match_stats = MATCH_TEMPLATE
        if os.path.exists(f'{self.name}.json'):
            with open(f'{self.name}.json','r') as f:
                self.profile = json.load(f)
        else:
            self.profile = {username: PROFILE_TEMPLATE}
            with open(f'{self.name}.json', 'w') as f:
                f.write(self.profile)
        

    def add_badge(self, badge=None, difficulty=0):
        self.profile['badges'][badge] = difficulty  


    def add_credits(self):
        pass


    def unlock_board(self):
        pass


    def compute_new_rank(self):
        rank = self.profile[self.name]['rank']
        outcome = 0
        penalty = 0
        bonus = 0
        if rank < 1000:
            weighted_gain = 100
            weighted_loss = 50
        elif rank < 2000:
            weighted_gain = 75
            weighted_loss = 50
        elif rank < 3000:
            weighted_gain = 50
            weighted_loss = 50
        else:
            weighted_gain = 25
            weighted_loss = 50
        if self.match_stats['win'] == 1:
            outcome += weighted_gain
        else:
            outcome -= weighted_loss
        if self.match_stats['was_skunked'] == 1:
            penalty = 50
        elif self.match_stats['was_dbl_skunked'] == 1:
            penalty = 100
        elif self.match_stats['skunked_opponent'] == 1:
            bonus = 50
        elif self.match_stats['dbl_skunked_opponent'] == 1:
            bonus = 100
        return rank + outcome + bonus - penalty


    def update_profile(self,game_mode): #game_mode argument must match the dictionary keys available
        #stats to update: {'skunks':0,'skunked':0,'dbl_skunks':0,'dbl_skunked':0,'wins':0,'losses':0}
        self.profile[self.name][game_mode]['skunks'] += self.match_stats['skunked_opponent']
        self.profile[self.name][game_mode]['skunked'] += self.match_stats['was_skunked']
        self.profile[self.name][game_mode]['dbl_skunks'] += self.match_stats['dbl_skunked_opponent']
        self.profile[self.name][game_mode]['dbl_skunked'] += self.match_stats['was_dbl_skunked']
        if self.match_stats['win'] == 1:
            self.profile[self.name][game_mode]['wins'] += 1
        else:
            self.profile[self.name][game_mode]['losses'] += 1
        self.profile[self.name]['rank'] = self.compute_new_rank()


    def save_updated_profile(self):
        with open(f'{self.name}.json', 'w') as f:
            json.dump(self.profile, f)


    def display_stats(self):
        print(f'======== Player stats for {self.name} ========\n')
        print(f'Rank:    {self.profile[self.name]['rank']}')
        print(f'Credits: {self.profile[self.name]['credits']}')
        print(f'Badges:  {self.profile[self.name]['badges']}')
        print(f'Boards unlocked: {self.profile[self.name]['boards_unlocked']}')
        print('============================================== \n')
        print('               Versus Humans                   \n')
        print(f'WINS:            {self.profile[self.name]['vs_humans']['wins']}')
        print(f'LOSSES:          {self.profile[self.name]['vs_humans']['wins']}')
        print(f'SKUNKS:          {self.profile[self.name]['vs_humans']['skunks']}')
        print(f'SKUNKED:         {self.profile[self.name]['vs_humans']['skunked']}')
        print(f'DOUBLE SKUNKS:   {self.profile[self.name]['vs_humans']['dbl_skunks']}')
        print(f'DOUBLE SKUNKED:  {self.profile[self.name]['vs_humans']['dbl_skunked']}')
        print('============================================== \n')
        print('              Versus Computer                  \n')
        print(f'EASY:   {self.profile[self.name]['computer_easy']}')
        print(f'MEDIUM: {self.profile[self.name]['computer_med']}')
        print(f'HARD:   {self.profile[self.name]['computer_hard']}')