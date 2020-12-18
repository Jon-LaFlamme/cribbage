import hand
import inflect

verbose = inflect.engine()


def process_play(stack, name, count):

    points = 0
    if count == 15:
        _fifteen = True
        points += 2
    else:
        _fifteen = False
    if count ==  31:
        _thirtyone = True
        points += 2
    else:
        _thirtyone = False
    _run_points = 0
    _pair_points = 0 
    _matched_cards = 0
    _card_played = stack[-1].rankname
    h = stack.copy()

    if len(stack) > 1:
        #check for runs by working backward
        if len(stack) > 2:
            i = 3
            while i <= len(stack):
                substack = hand.Hand(h[-i:])
                result = substack.points_from_runs()
                if result > 0:
                    _run_points = result
                else:
                    break
                i += 1
        #check for pairs
        if stack[-1].rank == stack[-2].rank:
            _pair_points += 2
            _matched_cards = 2
            if len(stack) > 2 and stack[-2].rank == stack[-3].rank:
                _pair_points += 6
                _matched_cards = 3
                if len(stack) > 3 and stack[-3].rank == stack[-4].rank:
                    _pair_points += 12  
                    _matched_cards = 4


    if points == 0:
        return nada(name, count, points)
    if _run_points > 0:
        if _fifteen or _thirtyone:
            return  run(name, count, True)
        else:
            return  run(name, count)






    return points


def fifteen(self, string=None):
    


def thirtyone(self):


def run(name, count, _run_points, points, is_fiteen_or_thirtyone=False):
    if is_fiteen_or_thirtyone:
        print(f'{name}: {verbose.number_to_words(count)} and a run of {verbose.number_to_words(_run_points)} is {verbose.number_to_words(points)}.')
    else:
        print(f'{name}: {verbose.number_to_words(count)} makes a run of {verbose.number_to_words(_run_points)}.')
    return points

def pair(name, count, points, _matched_cards, _card_played, is_fiteen_or_thirtyone=False):
    if is_fiteen_or_thirtyone:
        print(f'{name}: {verbose.number_to_words(count)} and {verbose.number_to_words(_matched_cards)} {_card_played}s for {verbose.number_to_words(points)}.')
    else:
        print(f'{name}: {verbose.number_to_words(count)} and {verbose.number_to_words(_matched_cards)} {_card_played}s for {verbose.number_to_words(points)}.')
    return points

def nada(name, count, points):
    print(f'{name}:  {verbose.number_to_words(count)}.')
    return points



def peg_driver(self):