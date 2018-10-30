import scores

#initialise the scores
scores.init_scores()

#print scores
scores.print_scores()

#print scores from file, sorted desc.
scores.print_file_sorted()

#add new user - user4 with a score of 3
scores.add_score('user4', 3)

#save scores to file - we should have a new line with user4 and score 3
scores.save_scores()

#test No.2
scores.init_scores()

#print scores, we should have a user4 in the score table now.
scores.print_scores()

#print scores from file, sorted desc.
scores.print_file_sorted()

#test No.3 - add score to the existing user
scores.init_scores()

#print scores, we should have a user4 in the score table now.
scores.print_scores()

scores.add_score('user1', 5)

scores.save_scores()

#print scores from file, sorted desc.
scores.print_file_sorted()





'''

userAuthenticated = usersPY.user_authentication('user1', 'pass2')

print(userAuthenticated)

userAuthenticated = usersPY.user_authentication('user1', 'pass1')

print(userAuthenticated)

userAuthorised = usersPY.user_authorised('user11')

print(userAuthorised)

'''