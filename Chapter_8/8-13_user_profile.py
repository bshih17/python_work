def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('Bram', 'Shih',
	location='Davie',
	race='Asian',
	occupation='Teacher')

print(user_profile)

for key, value in user_profile.items():
	print(f"{key.title()}: {value}")



