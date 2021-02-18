from random import choice


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



alphabet = [
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

filename = 'hard_hangman_words.txt'

# Create a word bank from file, though it has whitespaces.
with open(filename) as f:
	word_bank = f.readlines()

# Recreate word bank without whitespaces.
for i in range(0,len(word_bank)):
	word_bank[i] = word_bank[i].strip()

# Initiate Hangman game.
while True:
	slots = []
	displayed_slots = ''
	tries = 15
	guessed_letters = []
	
	print("Welcome to Hangman.")

	current_word = choice(word_bank).upper()
	current_letters = split_word(current_word)
	empty_slots_left = len(current_word)

	for i in range(0, len(current_word)):
		slots.append('')
		displayed_slots += '_  '
	
	while True:
		if tries == 0:
			print("\nGAME OVER    GAME OVER    GAME OVER")
			print("YOU LOSE")
			print(f"The word was {current_word}.")
			break
		
		print("_______________________________________________________________________________________")
		print(f"\n\t{displayed_slots}\n")

		if guessed_letters:
			print(f"Letters you have already guessed: {guessed_letters}")

		if tries == 1:
			guess = input(f"You currently have {tries} try left. Guess a letter: ")
		else:
			guess = input(f"You currently have {tries} tries left. Guess a letter: ")

		guess = guess.upper()

		valid_input = check_if_a_in_b(guess, alphabet)

		if valid_input:
			# Check if guessed letter is in the word.
			positions = get_positions(guess, current_word)
			
			# If the guessed letter is in the word
			# If the guessed letter has a position in the word
			if positions:
				guessed_already = check_if_a_in_b(guess, slots)
				
				# If the letter was guessed already
				if guessed_already:
					print(f"You guessed '{guess}' already!")
					continue

				else:
					# For every position, assign the guessed letter to its slot
					for position in positions:
						slots[position] = guess
					empty_slots_left -= len(positions)

					if len(positions) == 1:
						print(f"Nice! '{guess}' appears {len(positions)} time.")
					else:
						print(f"Nice! '{guess}' appears {len(positions)} times.")
					
				guessed_letters.append(guess)

				displayed_slots = ''

				for i in range(0, len(slots)):
					if slots[i] == '':
						displayed_slots += '_  '
					else:
						displayed_slots += f'{slots[i]}  '
					
				if empty_slots_left == 0:
					print("\nCongratulations! You win!")
					break

			else:
				tries -= 1
				print(f"Sorry, '{guess}' is not in the word!")
				guessed_letters.append(guess)
				continue

		else:
			print("That's not a valid guess!")
			continue
	

	play_again = input("\nDo you want to play again? (yes/no) ")
	if play_again == 'no':
		break
	if play_again == 'yes':
		continue



print("\nThanks for playing.")