#importing of modules
import csv
import time

UserID = []
Scores = []

#clears these variable every time run this code so no addition errors
def init_scores():
    UserID.clear()
    Scores.clear()

    #code to open the csv file 'scores' as a reader text file
    with open('scores.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter = ',')
        for row in readCSV:

            currentUserID = row[0]
            currentScore = row[1]
            UserID.append(currentUserID)
            Scores.append(int(currentScore))

#defines variable to save the new scores to users row in the external file
def save_scores():
#save the data in the arrays UserID and Scores, into a CSV file.
    with open('scores.csv', mode='w', newline='') as scores_file: #code to write into csv file
        scores_writer = csv.writer(scores_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        array_length = len(UserID)
        for x in range(array_length):
            scores_writer.writerow([UserID[x], Scores[x]]) #writes scores into row using index (x = index)

#defines varibale to print the scores of the csv file
def print_scores():
    array_length = len(UserID)
    print ('Scores:')
    for x in range(array_length): #for every index must print the corresponding username and its score
        print('%(user_id)s and %(score)s' %
            { 'user_id': UserID[x], 'score': Scores[x]})

#defines variable to add new scores to csv file with existing scores
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

#defines variable to print the scores in a sorted table
def print_file_sorted():
    with open('scores.csv', 'r') as data:
        reader = csv.reader(data)
        newList = sorted(reader, key=lambda row : int(row[1]), reverse=True)[0:5] #how to sort it
        print ('  | Usernames | Scores') #how it will look and print headings
        for i, r in enumerate(newList):
            print('{} | {} | {}'.format(str(i), r[0], r[1])) #print settings with the data




