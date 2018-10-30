
import csv
import time

UserID = []
Scores = []

def init_scores():
    UserID.clear()
    Scores.clear()

    with open('scores.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter = ',')
        for row in readCSV:
            #you should check that the row (e.g.: line in the file) is NOT empty
            currentUserID = row[0]
            currentScore = row[1]
            UserID.append(currentUserID)
            Scores.append(int(currentScore))

def save_scores():
#save the data in the arrays UserID and Scores, into a CSV file.
    with open('scores.csv', mode='w', newline='') as scores_file:
        scores_writer = csv.writer(scores_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        array_length = len(UserID)
        for x in range(array_length):
            scores_writer.writerow([UserID[x], Scores[x]])

def print_scores():
    array_length = len(UserID)
    print ('Scores:')
    for x in range(array_length):
        print('%(user_id)s and %(score)s' %
            { 'user_id': UserID[x], 'score': Scores[x]})

def add_score(user_id_param, score_param):
    #check if user_id_param already exist in the UserID array
    found_user_index = -1
    for idx, user in enumerate(UserID):
        if user == user_id_param:
            found_user_index = idx
            break
    #if exist, get the index and update the score in the Scores array
    #if doesn't exist, create a new entry in UserID and Scores
    if (found_user_index == -1):
        #this user was NOT in the score table
        UserID.append(user_id_param)
        Scores.append(score_param)
    else:
        #this user is already in the score table, the score should be updated with the new value
        #which is the current score + the new score
        #print('%(user_id)s and %(score)s' %
        #   { 'user_id': UserID[idx], 'score': Scores[idx]})
        Scores[idx] = Scores[idx] + score_param

def print_file_sorted():
    with open('scores.csv', 'r') as data:
        reader = csv.reader(data)
        newList = sorted(reader, key=lambda row : int(row[1]), reverse=True)
        print ('  | Usernames | Scores')
        for i, r in enumerate(newList):
            print('{} | {} | {}'.format(str(i), r[0], r[1]))




