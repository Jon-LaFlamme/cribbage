#TODO(Jon) This module is for managing all gameplay sequences


def sign_in():






def mode_selection():
    
    print('----- Classic cribbage game modes -----')
    print('1) Human vs Computer')
    print('2) Human vs Human')
    invalid = True
    while invalid:
        mode = int(input('Make your selection:'))
        if mode == 1 or mode == 2:
                invalid = False
        else:
            print('Invalid selection: Please try again.')
    if mode  == 1:
        print('\nYou have selected Human vs Computer.\n')
    if mode == 2:
        print('\nYou have selected Human vs Human.\n')
    return mode






def discard_sequence()

def peg_sequence():






if __name__ == "__main__":
    print('\n  Launching Classic Cribbage  \n')