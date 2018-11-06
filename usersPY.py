#importing of modules
import csv
import time

UserID = []
Password = []
Status = []

#defining a function which will open the csv file 'users' as a read file
def init_users():
    with open('users.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter = ',')
        for row in readCSV: #will assign variables to specific column/row in external csv file
            userID = row[0]
            password = row[1]
            status = row[2]
            UserID.append(userID)
            Password.append(password)
            Status.append(status)

#defines variable using specific parameter to see if user inputs matches value in file
def userExists(user_id_param):
    user_found = False #sets variable user_found to boolean 'False' as not yet found
    for user in UserID:
        if user == user_id_param: #if users input matches value from csv file:
            user_found = True #sets variable user_found to boolean 'True'
    return user_found #will return value assigned to this variable

#defines variable using specific parameter to find index number for username
def findUser(user_id_param):

    found_user_index = -1 #index value for 'False'
    for idx, user in enumerate(UserID):
        if user == user_id_param: #if user input matches username in file
            found_user_index = idx #assign index to the user index variable

    if (found_user_index == -1): #if the user index is false and not found:
        print ('User Not Found!') #will print this message

    return found_user_index #value inside variable will be returned

#defines variable using specific parameter to authenticate the users username and password
def user_authentication(userGiven, passwordGiven):
    index = findUser(userGiven) #variable index will be assigned to the index found in previous code
    ret_value = False #boolean value 'False' will be returned

    #if the index is not -1 (so therefore 'True') AND user password matches a password in csv file
    if (index != -1 and passwordGiven == Password[index] ):
        ret_value = True #boolean value 'True' will be returned
        print('Password Valid!') #message will be printed
    else: #otherwise:
        print('Invalid Password!') #counter message will be printed

    return ret_value #value assigned to this variable will be returned

#defines variable using speciic parameter to see if user inputs matches value in file for UAA(authorisation)
#currently not in use as not needed in task criteria
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


