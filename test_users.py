import users


def test_sign_in():
    print(f'\n---------- Testing user sign-in -----------')
    u = users.sign_in()
    print(f'\n User username: {u.name}')
    print(f'\n User match statistics: {u.match_stats}')

def test_add_user():
    print(f'\n---------- Testing add user -----------')
    username = 'test_user3'
    email = 'test_user3@test.com'
    users.add_user(username=username, email=email)

def test_lookup_user():
    print(f'\n---------- Testing user lookup -----------\n')
    username = 'test_user3'
    email = 'test_user3@test.com'
    response = users.lookup_user(username=username, email=email)
    print(f'\n--Response key: fa = found,authenticated; fna = found,non-authenticated; nf = not found -\n')
    print(f'- Response code: {response}.  ')

def test_User_constructor():
    print(f'\n---------- Testing User constructor -----------\n')
    username = 'Fred Astaire'
    email = 'fred@portlandia.com'
    u = users.User(username=username, email=email)
    print(f'\n User username: {u.name}')
    print(f'\n User match statistics: {u.match_stats}')

def test_add_badge():
    print(f'\n---------- Testing Add Badge -----------\n')
    username = 'test_user1'
    email = 'test_user1@test.com'
    badge = 'win_streak_3'
    difficulty = 'expert'
    u = users.User(username=username, email=email)
    u.add_badge(badge, difficulty)
    print(f'--- Updated Badges field for {u.name}: \n')
    print(u.profile[username]['badges'])
 
def test_add_credits():
    print(f'\n---------- Testing Add Credits -----------\n')
    username = 'test_user1'
    email = 'test_user1@test.com'
    u = users.User(username=username, email=email)
    u.add_credits(credits=3)
    print(f'--- Updated Credits field for {u.name}:')
    print(u.profile[username]['credits'])

def test_update_unlocked_boards():
    print(f'\n---------- Testing Update Unlocked Boards -----------\n')
    username = 'test_user1'
    email = 'test_user1@test.com'
    u = users.User(username=username, email=email)
    u.update_unlocked_boards(board='miracle_mile', difficulty='expert')
    print(f'--- Updated Unlocked Boards Field for {u.name}:')
    print(u.profile[username]['unlocked_boards']) 

def test_compute_new_rank():
    print(f'\n---------- Testing Compute New Rank -----------\n')
    test_match_stats = {'win': 1, 'was_skunked': 0, 'was_dbl_skunked': 0, 'skunked_opponent': 1, 'dbl_skunked_opponent': 0}
    username = 'test_user1'
    email = 'test_user1@test.com'
    u = users.User(username=username, email=email)
    print(f'\n--- Original rank for {u.name}:')
    print(u.profile[username]['rank'])
    u.match_stats = test_match_stats
    new_rank = u.compute_new_rank()
    print(f'\n--- Updated rank for {u.name}: {new_rank}')

def test_update_profile():
    print(f'\n---------- Testing Update Profile -----------\n')
    test_match_stats = {'win': 1, 'was_skunked': 0, 'was_dbl_skunked': 0, 'skunked_opponent': 1, 'dbl_skunked_opponent': 0}
    username = 'test_user1'
    email = 'test_user1@test.com'
    u = users.User(username=username, email=email)
    print(f'--- The original profile for {u.name}\n')
    print(u.profile)
    u.match_stats = test_match_stats
    u.update_profile(game_mode='vs_humans')
    print(f'\n--- The updated profile for {u.name}\n')
    print(u.profile)

def test_save_updated_profile():
    print(f'\n---------- Testing Save Updated Profile -----------\n')
    test_match_stats = {'win': 1, 'was_skunked': 0, 'was_dbl_skunked': 0, 'skunked_opponent': 1, 'dbl_skunked_opponent': 0}
    username = 'test_user1'
    email = 'test_user1@test.com'
    u = users.User(username=username, email=email)
    print(f'--- The original profile for {u.name}\n')
    print(u.profile)
    u.match_stats = test_match_stats
    u.update_profile(game_mode='vs_humans')
    u.save_updated_profile()
    print('Saving new stats to file...')
    print('Loading the updated file now...')
    updated_u = users.User(username=username, email=email)
    print(f'--- The updated profile for {updated_u.name}\n')
    print(updated_u.profile)

def test_display_stats():
    print(f'\n---------- Testing Display Stats -----------\n')
    username = 'test_user1'
    email = 'test_user1@test.com'
    u = users.User(username=username=, email=email)
    u.display_stats()








if __name__ == "__main__":
    #test_sign_in()     #Test1: Create new profile, verify account in user_directory.json and new json with {username}.json created, PASSED 12/21/20.
                        #Test2: Sign-in to existing profile, PASSED 12/21/20. 
                        #Test3: Wrong username or email handling, PASSED 12/21/20.
    #test_add_user()    #Test: Check user_directory.json for successful add. Make sure username and email is not present before running test, PASSED 12/21/20.
    #test_lookup_user()  #Test: Verify response codes work for each case by changing inputs. PASSED ALL 12/21/20
    #test_User_constructor()    #Test PASSED 12/21/20
    #test_add_badge()    #Test PASSED 12/21/20
    #TODO(Jon) test_new_credits_calculator() #Method needs to be built still
    #test_add_credits()     #Test PASSED 12/21/20
    #test_update_unlocked_boards()  #Test PASSED 12/21/20
    #test_compute_new_rank()     #Test PASSED 12/21/20
    #test_update_profile()       #Test PASSED 12/21/20
    #test_save_updated_profile()        #Test PASSED 12/21/20
    #test_display_stats()       #Test PASSED 12/21/20
