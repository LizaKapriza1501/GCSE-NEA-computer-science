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


print(len(Songs))
print(len(Artist))

random_song_index = random.randint(0, len(Songs))

print('this is the random index between %(start)d and %(finish)d = %(random_song)d' %
    { 'start': 0, 'finish': len(Songs), 'random_song': random_song_index})


print('This is a song = %(song_name)s and this is the artist = %(artist)s' %
    { 'song_name': Songs[random_song_index], 'artist': Artist[random_song_index]})
'''
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

'''
