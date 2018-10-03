import usersPY

'''
initialise users
'''

usersPY.init_users()

'''
check if user 'user1' exists and print the index for the userID
'''

user_checker = usersPY.userExists('user1')

print(user_checker)

user_checker = usersPY.userExists('user111')

print(user_checker)

user_index = usersPY.findUser('user5')
print(user_index)

user_index = usersPY.findUser('user555')
print(user_index)


