
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

    if (found_user_index == -1):
        print ('User Not Found!')

    return found_user_index

    '''
    Liza - add function that is comparing given user/password to user/password that is stored in your Arrays.
    '''
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




'''
Liza - add function that is comparing given user/password to user/password that is stored in your Arrays.
'''

