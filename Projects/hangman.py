from random import choice


def create_word_bank(filename):
	"""Create a word bank from a text file of words."""

	# Create a word bank from file, though it has whitespaces.
	with open(filename) as f:
		word_bank = f.readlines()

	# Recreate word bank without whitespaces.
	# Replace each word with stripped word.
	for i in range(0,len(word_bank)):
		word_bank[i] = word_bank[i].strip()

	return word_bank


def split_word(word):
    """Splits word into letters and stores them in a list"""
    letters_of_word = []
    for i in range(0,len(word)):
        letters_of_word.append(word[i])

    return letters_of_word


def check_if_a_in_b(guess, alphabet):
	"""
	Checks to see if the guess is a valid input, a single letter string
	Check to see if the guess is in the alphabet.	
	Check to see if the guess is in the slots.
	"""
	boolean = False

	for letter in alphabet:
		if guess == letter:
			boolean = True

	return boolean


def get_positions(guess, word):
	"""
	Checks to see if the letter you guessed is in the word
	If the guess is correct, store the positions in which the guessed letter appears.
	"""
	positions_of_guessed_letter = []

	for i in range(0,len(word)):
		if guess == word[i]:
			positions_of_guessed_letter.append(i)

	return positions_of_guessed_letter



def get_updated_displayed_slots(slots, displayed_slots):
	"""Take from the current slots, and update displayed slots."""
	displayed_slots = ''

	for i in range(0, len(slots)):
		if slots[i]:
			displayed_slots += f'{slots[i]}  '
		else:
			displayed_slots += '_  '
	
	return displayed_slots



alphabet = [
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]


# Initiate Hangman game.
while True:
	slots = []
	displayed_slots = ''
	tries_left = 10
	guessed_letters = []
	
	print("Welcome to Hangman.")

	difficulty = input(f"Choose a difficulty. Enter 'easy' or 'hard': ")

	if difficulty == 'easy':
		filename = 'hangman_words.txt'

	elif difficulty == 'hard':
		filename = 'hard_hangman_words.txt'
	else:
		print("That's not a valid input!\n")
		continue

	word_bank = create_word_bank(filename)

	current_word = choice(word_bank).upper()
	empty_slots_left = len(current_word)

	# Create empty letter slots according to the current word.
	for i in range(0, len(current_word)):
		slots.append('')
		displayed_slots += '_  '
	
	while True:
		if tries_left == 0:
			print("\nGAME OVER    GAME OVER    GAME OVER")
			print("YOU LOSE")
			print(f"The word was {current_word}.")
			break
		
		print("_______________________________________________________________________________________")
		print(f"\n\t{displayed_slots}\n")

		# Display letters you have already guessed.
		if guessed_letters:
			print(f"Letters you have already guessed: {guessed_letters}")

		# Display how many tries you have left, and prompts you to guess a letter.
		if tries_left == 1:
			guess = input(f"You currently have {tries_left} try left. Guess a letter: ")
		else:
			guess = input(f"You currently have {tries_left} tries left. Guess a letter: ")

		guess = guess.upper()

		# Check if the guess is a valid input, a single letter in the alphabet.
		valid_input = check_if_a_in_b(guess, alphabet)

		if valid_input:
			# Check if guessed letter is in the word.
			positions = get_positions(guess, current_word)
			
			# If the guessed letter is in the word
			# aka if the guessed letter has a position in the word
			if positions:

				# Check if guessed already
				guessed_already = check_if_a_in_b(guess, slots)
				
				# If the letter was guessed already
				if guessed_already:
					print(f"You guessed '{guess}' already!")
					continue

				# For every position, assign the guessed letter to its slot
				for position in positions:
					slots[position] = guess
				empty_slots_left -= len(positions)

				# Display how many times the guessed letter appears in the word.
				if len(positions) == 1:
					print(f"Nice! '{guess}' appears {len(positions)} time.")
				else:
					print(f"Nice! '{guess}' appears {len(positions)} times.")
					
				# Append the guessed letter to the list of the guessed letters.
				guessed_letters.append(guess)

				# Update displayed slots to be displayed when the while loop begins again.
				displayed_slots = get_updated_displayed_slots(slots, displayed_slots)
				
				# If you have guessed all the letters, the you win.
				# aka all the empty slots are filled
				if empty_slots_left == 0:
					print("\nCongratulations! You win!")
					print(f"\n\t{displayed_slots}\n")
					break
			
				
			# If the guessed letter is not in the word
			else:
				tries_left -= 1
				print(f"Sorry, '{guess}' is not in the word!")
				guessed_letters.append(guess)
				continue
				

		# If the input is not valid, if it is not a single letter in the alphabet
		else:
			print("That's not a valid guess!")
			continue
	

	play_again = input("\nDo you want to play again? Enter 'yes' or 'no': ")
	if play_again == 'no':
		break
	if play_again == 'yes':
		continue



print("\nThanks for playing.")

# How come it reduces the tries if you guessed already?