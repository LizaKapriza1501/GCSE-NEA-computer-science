
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

def userExists(user_id_param):
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

    if (found_user_index == -1):
        print ('User Not Found!')

    return found_user_index

def user_authentication(userGiven, passwordGiven):
    index = findUser(userGiven)
    ret_value = False

    if (index != -1 and passwordGiven == Password[index] ):
        ret_value = True
        print('Password Valid!')
    else:
        print('Invalid Password!')

    return ret_value

def user_authorised(userGiven):
    index = findUser(userGiven)

    ret_value = False

    if (index != -1):
        if('Authorised' == Status[index] ):
            ret_value = True
            print('User Authorised!')
        else:
            print('User NOT Authorised!')

    return ret_value


