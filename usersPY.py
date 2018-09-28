import csv
import time

with open('users.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    UserID = []
    Password = []
    Status = []

    for row in readCSV:
        userID = row[0]
        password = row[1]
        status = row[2]
        UserID.append(userID)
        Password.append(password)
        Status.append(status)
