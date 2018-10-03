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

def GivenData():
    GivenUserID = input("Please input your username: ")
    GivenPassword = input("Please input your password: ")
    for input in GivenPassword:
        if GivenUserID == usersPY.userExists():
            print("your Username is correct")
        else:
            print("incorrect Username")

    for input in GivenPassword:
        if GivenPassword == userPY.passExists():
            print("your Password is correct")
        else:
            print("incorrect Password")


'''
print(len(Songs))
print(len(Artist))


random_song_index = random.randint(0, len(Songs))

print('this is the random index between %(start)d and %(finish)d = %(random_song)d' %
    { 'start': 0, 'finish': len(Songs), 'random_song': random_song_index})


print('This is a song = %(song_name)s and this is the artist = %(artist)s' %
    { 'song_name': Songs[random_song_index], 'artist': Artist[random_song_index]})

'''
