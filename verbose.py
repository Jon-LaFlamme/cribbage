import inflect

#Utility Functions
def words(num):
    v = inflect.engine()
    return v.number_to_words(num)

def post_score(player1, player2):
    if player1.score > 121:
        player1.score = 121
    if player2.score > 121:
        player2.score = 121
    print(f'\n~~~~~~~  {player1.name}: {player1.score}  ~~~~~~~~~~~~  {player2.name}: {player2.score}  ~~~~~~~\n')

#Newgame and First Deal sequence
def start_game(player1, player2):
    print('\n\n=============== NEW GAME ===============\n')
    print(f'{player1.name} versus {player2.name}\n')

def cut_for_deal():
    print('\n================ Cut for first deal =====================\n')

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
    print('\n=============== Pegging Begins ==================\n')

def peg_one(player, card, count):
    print(f'{player.name} plays a {card.name}. Count is {words(count)}.')

def peg_points(player, points):
    print(f'{player.name} pegs {points} points.')

def peg_go(player):
    print(f'{player.name} last card for a go (+1 point).')

#Count Sequence
def counting():
    print(f'\n=================== Pegging Complete. Begin Scoring Hands  ===================\n')

def score_hand(player, points, is_crib=False):
    if is_crib:
        print(f'CRIB: {player.name} counts {points}.')
    else:
        print(f'HAND: {player.name} counts {points}.')

def new_round():
    print('\n==================== Next Round ========================\n')


def show_hand(player, turncard, points, hand=None):
    is_crib = False
    if hand:
        is_crib = True
    print('\n#############################################')
    score_hand(player, points, is_crib=is_crib)
    print(f'\n--------- TURNCARD: {turncard.name} ----------')
    if is_crib:
        for card in hand:
            print(f'|| {card.name}')
    else:
        player.display_hand()
    print('#############################################\n')