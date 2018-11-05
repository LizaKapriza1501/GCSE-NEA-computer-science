#importing of modules which are default and which i created
import csv
import time
import random
import usersPY
import re
import scores

#function defining to keep the first letter of every word of song title
#and changes every other character into a dash '_'
def obfuscate(name):
    name=name.split(" ")
    name=list(map(lambda x:x[0]+re.sub(r"[a-z]","_",x[1:],flags=re.IGNORECASE),name))
    return " ".join(name)

#writing the code to open and read the csv file written for song titles and artists
with open('songs.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    Songs = []
    Artist = []

    #for loop stating which column/row is for which piece of information
    for row in readCSV:
        song = row[0].strip()
        artist = row[1].strip()
        Songs.append(song)
        Artist.append(artist)


#importing the modules which i wrote for user authorisation and authentication (UAA)
usersPY.init_users()
scores.init_scores()

#setting the variable 'tries' to 0 as user has not started playing yet
tries = 0

#while loop alowing the user to log in with maximum of 3 attempts at log in information
#program uses module called 'usersPY' to auntenticate if the user and password match/exist
while (tries < 3):
    userGiven = input("Please input your Username")
    passwordGiven = input("Please input your Password")
    userAuthenticated = usersPY.user_authentication(userGiven, passwordGiven)
    print(userAuthenticated)
    if (userAuthenticated):
        break
    tries += 1 #increase the tries after each attempt

#code stating that if tries attempts have been used up, user will not be authenticated and will
#have to exit the program
if (tries >= 3):
    print ('we could not authenticate you!')
    print('program will be terminated.')
    exit(1)

#otherwise the user is given a welcome message and is shown the current highscores of the game
#by importing the code from a seperate module which i wrote called 'scores'
print("Welcome ", userGiven)
print("This is the current highscore table: ")
scores.print_file_sorted()

#sets this variable to the boolean 'true'
stillPlaying = True

#states that is the player has chose to continue playing/next level, then their score will be 0 and guess
#will be starting at 1
#random_song_index variable is being assigned to a value which will be calculated
#printed will be a randomised selected index from the csv file 'songs.csv'
#printed after the selected index will be the corresponding index's song name only showing the first letter
#and showing the user the artist name as a clue
while (stillPlaying):
    score = 0
    guess = 1
    random_song_index = random.randint(0, len(Songs)-1)

    print('this is the random index between %(start)d and %(finish)d = %(random_song)d' %
        { 'start': 0, 'finish': len(Songs), 'random_song': random_song_index})


    print('This is a song = %(song_name)s and this is the artist = %(artist)s' %
        { 'song_name': obfuscate(Songs[random_song_index]), 'artist': (Artist[random_song_index])})


    #while loop stating that is the number of guesses that the user has had is less than 3 then the user
    #will be given a platform in which to input their guess
    while (guess < 3):
        guessGiven = input("Please input your guess for the name of the song")
        if guessGiven == Songs[random_song_index]: #if the user guess is equal to song chosen:
            print("correct! well done!")  #will print message 'correct'
            break #to move on to next block of code
        else: #otherwise do this:
            print("incorrect, please try again!")
            guess += 1

    #if only 1 guess was needed to get correct answer:
    if guess == 1:
        score = 3 #score of 3 will be awarded

    #if 2 guesses were needed to get correct answer:
    if guess == 2:
        score = 1 #score of 1 will be awarded

    #if statement saying that if guess = 3 then no more guesses - game over and prints correct answer
    if guess == 3:
        print("Game Over! Better luck next time!")
        print("Here is the correct answer: " + Songs[random_song_index])

    #once game is ended the score user recieved will be printed
    print("This is your score: ", score)
    scores.add_score(userGiven, score) #users score will be added to csv file 'scores'
    scores.save_scores() #users scores will be saved to csv file 'scores'

    #asking the user if want to continue for another 'level'
    answer = input("Do you want to continue playing y/n: ")
    if (answer == 'y' or answer == 'Y'): #if yes then:
        stillPlaying = True #set variable to boolean 'True'
    else: #otherwise set it to 'False'
        stillPlaying = False
        print("These are the high scores: ") #therefore printing the highscores
        scores.print_file_sorted() #highscores are printed by importing the function from another
                                    #module that i wrote 'scores'















