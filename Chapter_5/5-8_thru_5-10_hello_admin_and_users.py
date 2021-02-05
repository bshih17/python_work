# 5-8 Hello Admin
usernames = ['admin', 'Hooligan', 'Jay123', 'Clone Trooper77', 'Mofive']

for username in usernames:
	if username == 'admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print(f"Hello {username}, thank for you logging in again.")

# 5-9 No Users
usernames = []
if usernames:
	print("We have users.")
else:
	print("All users have been deleted. We no have no users.\n")

#5-10 Checking Usernames
current_users = ['admin', 'Hooligan', 'Jay123', 'ajfm88', 'Mofive']
new_users = ['Mofive', 'AJFM88', 'Moflve', 'MOFIVE']

# This code is to ensure that the new user can't be 'JOHN' if 'John' is already a user.
# case insensitive
current_users_lowercase = []
for current_user in current_users:
	current_users_lowercase.append(current_user.lower())

for new_user in new_users:
	if new_user in current_users:
		print(f"Sorry, the username '{new_user}' has already been taken. Try another one.")
	elif new_user.lower() in current_users_lowercase:
		print(f"Sorry, the username '{new_user}' has already been taken. Try another one.")
	else:
		print(f"Welcome {new_user}. You have successfully created a new account.")





