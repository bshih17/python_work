# 8-7 Album
def make_album(artist_name, album_title, number_of_songs = None):
	"""Make an album."""
	album ={'artist': artist_name, 'album title': album_title}
	if number_of_songs:
		album['number of songs'] = number_of_songs

	return album

album_info = make_album('Elevation', 'There Is a Cloud')
print(album_info)

album_info = make_album('Bethel Music', 'After All These Years')
print(album_info)

album_info = make_album('Jeremiah Grube', 'The Room')
print(album_info)

album_info = make_album('Jeremiah Grube', 'The Room', 12)
print(album_info)

# 8-8 User Albums
while True:
	print("\nEnter the artist name and album title. Enter 'q' to quit.")
	artist_name = input("Artist name: ")
	if artist_name == 'q':
		break

	album_title = input("Album title: ")
	if album_title == 'q':
		break
	
	# I didn't put this in the while loop... So the program never reached it...
	album_info = make_album(artist_name, album_title)
	print(album_info)
