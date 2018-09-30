
import csv
import time

UserID = []
Password = []
Status = []


def init_users():
    with open('users.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter = ',')
        for row in readCSV:
            userID = row[0]
            password = row[1]
            status = row[2]
            UserID.append(userID)
            Password.append(password)
            Status.append(status)



'''
find user with the name that is send in user_id_param in the UserID array
'''
def userExists(user_id_param):
    '''
    liza - change this function, so it is using the findUser function and does NOT do it's own traversing of array
    '''

    user_found = False
    for user in UserID:
        if user == user_id_param:
            user_found = True

    return user_found

def findUser(user_id_param):

    found_user_index = -1
    for idx, user in enumerate(UserID):
        if user == user_id_param:
            found_user_index = idx

    return found_user_index

