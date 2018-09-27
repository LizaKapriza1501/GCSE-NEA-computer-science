import csv
import time
import random
with open('songs.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    Songs = []
    Artist = []

    for row in readCSV:
        songs = row[0]
        artist = row[1]
        Songs.append(songs)
        Artist.append(artist)

count = 0
while True:
    userName = input("Hello! Welcome to SongGuess! \n\nUsername: ")
    password = input("Password: ")
    count += 1
    if count == 3:
        print("GoodBye, you used all of your attempts")
        break
    else:
        if userName == 'Hello' and password == 'World':
            print("Welcome to SongGuess!")
            break
        else:
            print("Your username or password is incorrect, please try again")

guess = 0
while guess < 3:
    x = random.randint(0,108)
    print(Artist[x])
    title = Songs[x]

    test = title[0] + title[1:].replace(title[0], "_")
    guess += 1


input = Songs[x]
    words = input.split()
    letters = [word[0] for word in words]
    print("".join(letters))

