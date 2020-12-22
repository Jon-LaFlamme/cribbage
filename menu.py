import users
import deck
import board
import players
import hand
import game


def main_menu():
    while True:
        print(' ========= Main Menu ======== \n')
        print('1) Play Classic Cribbage ')
        print('2) Play Ultimate Cribbage ')
        print('3) View Profile \n')
        print('4) Exit Program')
        selection = int(input('Make a selection: '))
        if selection >= 1 or selection <= 4:
            return selection
        else:
            print('Invalid Selection. Please try again.\n')


def select_mode():
    while True:
        print(' ========= Game Mode ======== \n')
        print('1) Singleplayer ')
        print('2) Multiplayer online ')
        print('3) Multiplayer local\n')
        selection = int(input('Make a selection: '))
        if (selection == 1 or selection == 2) or selection == 3:
            return selection
        else:
            print('Invalid Selection. Please try again.\n')


def select_difficulty():
    invalid = True
    while invalid:
        print(' ******** Choose Difficulty ******** \n')
        print('1) Beginner ')
        print('2) Intermediate ')
        print('3) Expert \n')
        selection = int(input('Make a selection: '))
        if selection == 1:
            difficulty = 'easy'
            invalid == False
        elif selection == 2:
            difficulty = 'medium'
            invalid == False
        elif selection == 3:
            difficulty = 'hard'
            invalid == False
        else:
            print('Invalid Selection. Please try again.\n')

    return difficulty


def select_board(mode):
    if mode == 1 or mode == 2:
        return 'classic_1'
    else:
        return 'classic_1'


def configurations(mode):
    if mode == 1:
        difficulty = select_difficulty()
        board = select_board(mode)
        settings = {'mode': 1, 'difficulty': difficulty, 'board': board}
    elif mode == 2:
        print('Sorry, online multiplayer mode not yet supported.')
        print('Routing to singleplayer mode now.')
        difficulty = select_difficulty()
        board = select_board(mode)
        settings = {'mode': 1, 'difficulty': difficulty, 'board': board}
    elif mode == 3:
        board = select_board(mode)
        settings = {'mode': 3, 'board': board}
    return settings


def initialize_players(user1 ,settings):
    if settings['mode'] == 1:
        p1 = players.human(name=user1.name)
        p2 = players.computer(settings['difficulty'])
    elif settings['mode'] == 2:
        print('Sorry, online multiplayer mode not yet supported.')
        print('Routing to singleplayer mode now.')
        p1 = players.human(name=user1.name)
        p2 = players.computer(settings['difficulty'])
    elif settings['mode'] == 3:
        p1 = players.human(name=user1.name)
        user2 = sign_in()
        p2 = players.human(name=user2.name)
    return {'users': [user1,user2], 'players': [p1,p2]}


def discard_sequence():
    pass


def peg_sequence():
    pass


def play_classic(user, settings):

    #Game Setup Procedures
    player_vec = initialize_players(user, settings)
    users = player_vec['users']
    players = player_vec['players']
    p1 = players[0]
    p2 = players[1]
    d = deck.Deck()
    d.shuffle()
    b = board.Classic(p1.name,p2.name)
    print(f'\n    {p1.name}   vs   {p2.name}     \n')




    

if __name__ == "__main__":

    print('\n  Launching Ultimate Cribbage ...  \n')
    user = sign_in()
    run_app = True
    while run_app:
        selection = main_menu()
        if selection == 1 or selection == 2:
            mode = select_mode()
            settings = configurations(mode)
            play_classic(user, settings)
        elif selection == 3:
            user.display_stats()
        else:
            run_app = False
    print('\n  Exiting Ultimate Cribbage ...  \n')
            
