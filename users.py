#TODO(Jon) This module will require online components for production, but will be locally implemented in this package
import os


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
                    'unlocked_boards': {'classic_1','ultimate_1'},    
                    'vs_humans': {'skunks':0,'skunked':0,'dbl_skunks':0,'dbl_skunked':0,'wins':0,'losses':0},
                    'computer_easy': {'skunks':0,'skunked':0,'dbl_skunks':0,'dbl_skunked':0,'wins':0,'losses':0},
                    'computer_med': {'skunks':0,'skunked':0,'dbl_skunks':0,'dbl_skunked':0,'wins':0,'losses':0},
                    'computer_hard': {'skunks':0,'skunked':0,'dbl_skunks':0,'dbl_skunked':0,'wins':0,'losses':0}
                    }

#Found but not authenticated: 'fna',  Found and authenticated: 'fa',  Not found: 'nf'
def lookup_user(username, email):
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
        if os.path.exists(f'{self.name}.json'):
            with open(f'{self.name}.json','r') as f:
                self.profile = json.load(f)
        else:
            self.profile = {username: PROFILE_TEMPLATE}
            with open(f'{self.name}.json', 'w') as f:
                f.write(self.profile)


    def display_stats(self):
        print(f'======== Player stats for {self.name} ========\n')
        print(f'Rank: {self.profile['rank']}')
        print(f'Badges: {self.profile['badges']}')
        print(f'Boards unlocked: {self.profile['boards_unlocked']}/10')
        print('============================================== \n')
        print('     vs Humans        ||         vs Computer   \n')
        print(f'WINS:            {self.profile['vs_human']['wins']}            EASY WINS:            {self.profile['vs_computer']['easy_wins']}       ')
        print(f'LOSSES:          {self.profile['vs_human']['wins']}            EASY LOSSES:          {self.profile['vs_computer']['easy_losses']}       ')
        print(f'SKUNKS:          {self.profile['vs_human']['skunks']}            MEDIUM WINS:          {self.profile['vs_computer']['medium_wins']}       ')
        print(f'SKUNKED:         {self.profile['vs_human']['skunked']}            MEDIUM LOSSES:        {self.profile['vs_computer']['medium_losses']}       ')
        print(f'DOUBLE SKUNKS:   {self.profile['vs_human']['dbl_skunks']}            HARD WINS:          {self.profile['vs_computer']['hard_wins']}       ')
        print(f'DOUBLE SKUNKED:  {self.profile['vs_human']['dbl_skunked']}            HARD LOSSES:        {self.profile['vs_computer']['hard_losses']}       ')

    def add_badge(self, badge=None, difficulty=0):
        self.profile['badges'][badge] = difficulty  


    def compute_new_rank(self, opponent_rank):
        

    def add_match(self, stats):



    def update_profile(self):
        with open(f'{self.name}.json', 'w') as f:
            json.dump(self.profile, f)

