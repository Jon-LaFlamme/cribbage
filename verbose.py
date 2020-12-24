import inflect

#Utility Function
def words(num):
    v = inflect.engine()
    return v.number_to_words(num)

#Newgame and First Deal sequence
def start_game(player1, player2):
    print('=============== NEW GAME ===============\n')
    print(f'{player1.name} versus {player2.name}\n')

def cut_for_deal():
    print('\n--------- Cut for first deal ----------\n')

def cuts_card(player, card):
    print(f'{player.name} cuts a {card.name}.')

def win_first_deal(player):
    print(f'{player.name} wins first deal')

#Deal, Discard and Cut Sequence
def dealing(player):
    print(f'{player.name} dealing...')

def discard(player):
    print(f'{player.name} discards.')

def turncard(nondealer, dealer, card):
    print(f'{nondealer.name} cuts the deck.')
    print(f'{dealer.name} turns a {card.name}.')

def heels(player, card):
    print(f'{player.name} scores two points for heels.')

#Peg Sequence
def pegging():
    print('\n---------- Pegging Begins ---------\n')

def peg_one(player, card, count):
    print(f'{player.name} plays a {card.name}. Count is {words(count)}.')

def peg_points(player, points):
    print(f'{player.name} pegs {points} points.')

def peg_go(player):
    print(f'{player.name} played last card for a go and scores 1 point.')

#Count Sequence
def counting():
    print(f'\n---------- Pegging Complete. Now Scoring Hands  -----------\n')

def score_hand(player, points, is_crib=False):
    if is_crib:
        print(f'{player.name} scores {points} points in the crib.')
    else:
        print(f'{player.name} scores {points} in his/her hand.')

def new_round():
    print('\n---------------- Next Round --------------------\n')


