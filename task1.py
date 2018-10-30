import csv
import time
import random
import usersPY
import re
import scores

def obfuscate(name):
    name=name.split(" ")
    name=list(map(lambda x:x[0]+re.sub(r"[a-z]","_",x[1:],flags=re.IGNORECASE),name))
    return " ".join(name)

with open('songs.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    Songs = []
    Artist = []

    for row in readCSV:
        song = row[0].strip()
        artist = row[1].strip()
        Songs.append(song)
        Artist.append(artist)



usersPY.init_users()
scores.init_scores()

tries = 0

while (tries < 3):
    userGiven = input("Please input your Username")
    passwordGiven = input("Please input your Password")
    userAuthenticated = usersPY.user_authentication(userGiven, passwordGiven)
    print(userAuthenticated)
    if (userAuthenticated):
        break
    tries += 1


if (tries >= 3):
    print ('we could not authenticate you!')
    print('program will be terminated.')
    exit(1)

print("Welcome ", userGiven)
print("This is the current highscore table: ")
scores.print_file_sorted()

stillPlaying = True

while (stillPlaying):
    score = 0
    guess = 1
    random_song_index = random.randint(0, len(Songs)-1)

    print('this is the random index between %(start)d and %(finish)d = %(random_song)d' %
        { 'start': 0, 'finish': len(Songs), 'random_song': random_song_index})


    print('This is a song = %(song_name)s and this is the artist = %(artist)s' %
        { 'song_name': obfuscate(Songs[random_song_index]), 'artist': (Artist[random_song_index])})



    while (guess < 3):
        guessGiven = input("Please input your guess for the name of the song")
        if guessGiven == Songs[random_song_index]:
            print("correct! well done!")
            break
        else:
            print("incorrect, please try again!")
            guess += 1

    if guess == 1:
        score = 3
        #print("This is your score for this game: ", + score)

    if guess == 2:
        score = 1
        #print("This is your score for this game: ", + score)


    if guess == 3:
        print("Game Over! Better luck next time!")
        print("Here is the correct answer: " + Songs[random_song_index])


    print("This is your score: ", score)
    scores.add_score(userGiven, score)
    scores.save_scores()

    answer = input("Do you want to continue playing y/n: ")
    if (answer == 'y' or answer == 'Y'):
        stillPlaying = True
    else:
        stillPlaying = False
        print("These are the high scores: ")
        scores.print_file_sorted()















