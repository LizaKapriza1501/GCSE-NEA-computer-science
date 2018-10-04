import usersPY

'''
initialise users
'''

usersPY.init_users()

'''
check if user 'user1' exists and print the index for the userID
'''
'''
user_checker = usersPY.userExists('user1')

print(user_checker)

user_index = usersPY.findUser('user5')
print(user_index)

'''
'''
comparing users input with my arrays
'''

userAuthenticated = usersPY.user_authentication('user1', 'pass2')

print(userAuthenticated)

userAuthenticated = usersPY.user_authentication('user1', 'pass1')

print(userAuthenticated)

userAuthorised = usersPY.user_authorised('user11')

print(userAuthorised)


