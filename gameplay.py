#TODO(Jon) This module is for managing all gameplay sequences

import users
import deck
import board
import players
import hand


def sign_in():
    invalid = True
    while invalid:
        print('\n ======== User Sign-In ======== \n')
        print('1) Sign-in to an existing account.')
        print('2) Create a new account.')
        selection = int(input('Make a selection: '))
        if selection == 1:
            while invalid:
                username = input('\nEnter your username: ')
                email = input('Enter your email: ')
                feedback = users.lookup_user(username,email)
                if feedback == 'fna':
                    print('email does not match username.')
                    option = input('Enter 0 to return to menu. Any other key to try again:')
                    if option == 0:
                        break
                if feedback == 'fa':
                    u = users.User(username, email)
                    print('Loading profile.')
                    return u
        elif selection == 2:
            while invalid:
                username = input('\nCreate a username: ')
                email = input('Enter your email: ')
                feedback = users.lookup_user(username,email)
                if feedback == 'nf':
                    users.add_user(username,email)
                    u = users.User(username, email)
                    print('User profile created.')
                    return u  
                else:
                    print(f'username: {username} is already claimed. Please try again.') 
        else:
            print('Invalid selection. Please try again.')


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
    if mode == 1:
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


def play_game(user, mode, settings):
    if mode == 1:
        play_classic(user, settings)
    else:
        play_classic(user, settings)


def play_classic(user, settings):
    player_vec = initialize_players(user, settings)
    p1 = player_vec[0]
    p2 = player_vec[1]
    d = deck.Deck()
    d.shuffle()
    b = board.Classic(p1.name,p2.name)
    print(f'\n    {p1.name}   vs   {p2.name}     \n')

    print('\n -------- Cutting for first deal ---------\n')
    while True:
        c1 = p1.cut_deck(d)
        c2 = p2.cut_deck(d)
        print(f'{p1.name} cuts a {c1.name}.')
        print(f'{p2.name} cuts a {c2.name}.')

        if c1.rank < c2.rank:
            is_p1_dealer = True
            print(f'{p1.name} wins first deal.')
            break
        elif c2.rank < c1.rank:
            is_p1_dealer = False
            print(f'{p2.name} wins first deal.')
            break
        else:
            d.deck.append(c1)
            d.deck.append(c2)
            print('Tie! Cut again.')
    d.deck.append(c1)
    d.deck.append(c2)

    #Game begins
    while p1.score < 121 and p2.score < 121:
        b.display_board()
        d.shuffle()
        print('Dealing ...')
        for i in range(6):
            p1.cards.append(d.deal_one())
            p2.cards.append(d.deal_one())
        p1_discards = p1.discard(2)
        p2_discards = p2.discard(2)
        crib = p1_discards.extends(p2_discards)





    

if __name__ == "__main__":

    print('\n  Launching Ultimate Cribbage ...  \n')
    user = sign_in()
    run_app = True
    while run_app:
        selection = main_menu()
        if selection == 1 or selection == 2:
            mode = select_mode()
            settings = configurations(mode)
            play_game(user, mode, settings)
        elif selection == 3:
            user.display_stats()
        else:
            run_app = False
    print('\n  Exiting Ultimate Cribbage ...  \n')
            
