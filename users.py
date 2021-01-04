#TODO(Jon) This module will require online components for production, but will be locally implemented in this package
import os
import json

MATCH_TEMPLATE = {'win': 0, 'was_skunked': 0, 'was_dbl_skunked': 0, 'skunked_opponent': 0, 'dbl_skunked_opponent': 0}
DIFFICULTY_MAP = {'beginner': 1, 'intermediate': 2, 'expert': 3}
GAME_MODES = {'vs_humans','computer_easy','computer_med','computer_hard'}
BADGES = {'win_streak_3','hand_of_eight','hand_of_twelve','hand_of_sixteen','hand_of_twenty',
                 'hand_of_twenty-four','hand_of_twenty-eight','hand_of_twenty-nine','peg_five',
                 'peg_eight','peg_twelve','three_skunks','three_dbl_skunks','rank_status'}
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
                    'computer_beginner': {'skunks':0,'skunked':0,'dbl_skunks':0,'dbl_skunked':0,'wins':0,'losses':0},
                    'computer_intermediate': {'skunks':0,'skunked':0,'dbl_skunks':0,'dbl_skunked':0,'wins':0,'losses':0},
                    'computer_expert': {'skunks':0,'skunked':0,'dbl_skunks':0,'dbl_skunked':0,'wins':0,'losses':0}
                    }

#returns the new or existing user after successfull sign-in or new profile created
def sign_in():
    invalid = True
    while invalid:
        print('\n ======== User Sign-In ======== \n')
        print('1) Sign-in to an existing account.')
        print('2) Create a new account.')
        selection = int(input('Make a selection: '))
        if selection == 1:
            while invalid:
                username = input('\nEnter your username: ').lower()
                email = input('Enter your email: ').lower()
                feedback = lookup_user(username=username, email=email)
                if feedback == 'fna':
                    print('email does not match username.')
                    option = input('Enter 0 to return to menu. Any other key to try again:')
                    if option == 0:
                        break
                if feedback == 'fa':
                    u = User(username=username, email=email)
                    print('Loading profile.')
                    return u
        elif selection == 2:
            while invalid:
                username = input('\nCreate a username: ').lower()
                email = input('Enter your email: ').lower()
                feedback = lookup_user(username=username, email=email)
                if feedback == 'nf':
                    add_user(username=username, email=email)
                    u = User(username=username, email=email)
                    print('User profile created.')
                    return u  
                else:
                    print(f'username: {username} is already claimed. Please try again.') 
        else:
            print('Invalid selection. Please try again.')


#Found but not authenticated: 'fna',  Found and authenticated: 'fa',  Not found: 'nf'
def lookup_user(username=None, email=None):
    with open('user_directory.json','r') as f:
        user_directory = json.load(f)
        if username in user_directory:
            if user_directory[username]['email'] == email:
                return 'fa'
            else:
                return 'fna'
        else:
            return 'nf'


def add_user(username=None, email=None):
    with open('user_directory.json','r') as f:
        user_directory = json.load(f)
    user_directory[username] = {'email': email, 'rank': 0} 
    with open('user_directory.json', 'w') as f:
        json.dump(user_directory, f)


class User():

    def __init__(self, username=None, email=None):
        self.name = username
        self.match_stats = MATCH_TEMPLATE
        if os.path.exists(f'{self.name}.json'):
            with open(f'{self.name}.json','r') as f:
                self.profile = json.load(f)
        else:
            self.profile = {username: PROFILE_TEMPLATE}
            self.profile[username]['email'] = email
            with open(f'{self.name}.json', 'w') as f:
                json.dump(self.profile, f)
        

    def add_badge(self, badge=None, difficulty=None):
        if badge in BADGES and difficulty in DIFFICULTY_MAP:
            self.profile[self.name]['badges'][badge] = DIFFICULTY_MAP[difficulty]  

    def new_credits_calculator(self):
        #TODO(Jon) Create function that calculates the new credits awarded a user after achieving various tasks. Done once per game at end.
        #Requires a credits dictionary mapping credit value for various achievements
        #In-app purchases can also purchase credits 
        pass

    def add_credits(self, credits=None):
        self.profile[self.name]['credits'] += credits


    def update_unlocked_boards(self, board=None, difficulty=None):
        if difficulty in DIFFICULTY_MAP:
            value = DIFFICULTY_MAP[difficulty]
        if board in self.profile[self.name]['unlocked_boards']:
            #Only overwrite old scores if achieved at a greater difficulty level
            if value > self.profile[self.name]['unlocked_boards'][board]:
                self.profile[self.name]['unlocked_boards'][board] = value
        else: self.profile[self.name]['unlocked_boards'][board] = value


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


    def update_profile(self, game_mode=None):
        if game_mode in GAME_MODES:
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

        rank = self.profile[self.name]['rank']
        credits = self.profile[self.name]['credits']
        badges = self.profile[self.name]['badges']
        boards = self.profile[self.name]['unlocked_boards']
        wins = self.profile[self.name]['vs_humans']['wins']
        losses = self.profile[self.name]['vs_humans']['wins']
        skunks = self.profile[self.name]['vs_humans']['skunks']
        skunked = self.profile[self.name]['vs_humans']['skunked']
        dbl_skunks = self.profile[self.name]['vs_humans']['dbl_skunks']
        dbl_skunked = self.profile[self.name]['vs_humans']['dbl_skunked']
        easy = self.profile[self.name]['computer_easy']
        medium = self.profile[self.name]['computer_med']
        hard = self.profile[self.name]['computer_hard']

        print(f'======== Player stats for {self.name} ========\n')
        print(f'Rank:            {rank}')
        print(f'Credits:         {credits}')
        print(f'Badges:          {badges}')
        print(f'Boards unlocked: {boards}')
        print('============================================== \n')
        print('               Versus Humans                   \n')
        print(f'WINS:            {wins}')
        print(f'LOSSES:          {losses}')
        print(f'SKUNKS:          {skunks}')
        print(f'SKUNKED:         {skunked}')
        print(f'DOUBLE SKUNKS:   {dbl_skunks}')
        print(f'DOUBLE SKUNKED:  {dbl_skunked}')
        print('============================================== \n')
        print('              Versus Computer                  \n')
        print(f'BEGINNER:       {easy}')
        print(f'INTERMEDIATE:   {medium}')
        print(f'EXPERT:         {hard}')