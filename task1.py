import csv
import time
import random
import usersPY

with open('songs.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    Songs = []
    Artist = []

    for row in readCSV:
        songs = row[0]
        artist = row[1]
        Songs.append(songs)
        Artist.append(artist)

usersPY.init_users()

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







'''
print("These are songs:\n")
for song in Songs:
    print(song)
=======
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
>>>>>>> df514aa16723649bab3b773de7912a7f37562a5b


'''

'''
=======
>>>>>>> df514aa16723649bab3b773de7912a7f37562a5b
print(len(Songs))
print(len(Artist))


random_song_index = random.randint(0, len(Songs))

print('this is the random index between %(start)d and %(finish)d = %(random_song)d' %
    { 'start': 0, 'finish': len(Songs), 'random_song': random_song_index})


print('This is a song = %(song_name)s and this is the artist = %(artist)s' %
    { 'song_name': Songs[random_song_index], 'artist': Artist[random_song_index]})
<<<<<<< HEAD

'''
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

guess = 0
while guess < 3:
    x = random.randint(0,108)
    print(Artist[x])
    title = Songs[x]
=======
>>>>>>> df514aa16723649bab3b773de7912a7f37562a5b

'''
