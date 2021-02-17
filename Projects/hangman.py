from random import choice

def split_word(word):
    """Splits word into letters and stores them in a list"""
    letters_of_word = []
    for i in range(0,len(word)):
        letters_of_word.append(word[i])

    return letters_of_word

def check_guess(guess, word):
	"""
	Checks to see if the letter you guessed is in the word
	If the guess is correct, store the positions in which the guessed letter appears.
	"""
	positions_of_guessed_letter = []

	for i in range(0,len(word)):
		if guess == word[i]:
			positions_of_guessed_letter.append(i)

	return positions_of_guessed_letter



word_bank = ['cheese', 'muffin', 'iguana', 'dictionary', 'scissors', 'jello']
word_bank = ['cheese']
flag = True

print("Welcome to Hangman.")

while True:
	slots = []
	displayed_slots = ''
	tries = 10
	
	current_word = choice(word_bank)
	current_letters = split_word(current_word)

	for i in range(0, len(current_word)):
		slots.append('')
		displayed_slots += '_ '
	
	print(displayed_slots)


	while flag:
		guess = input(f"\nYou currently have {tries} tries left. Guess a letter: ")    

		if len(guess) != 1:
			print("That's not a valid guess!")

		else:
			positions = check_guess(guess, current_word)
			print(f"Your guess appears {len(positions)} times.")

			if positions == []:
				if tries == 0:
					print(f"GAME OVER   YOU LOSE")
				else:
					tries -= 1
					print(f"Sorry, '{guess}' is not in the word! You have {tries} tries left.")

			else:
				for position in positions:
					slots[position] = guess

			displayed_slots = ''
			for i in range(0, len(slots)):
				if slots[i] == '':
					displayed_slots += '_ '
				else:
					displayed_slots += f'{slots[i]} '

			# Check to see if you have won. Check if there are any blanks left.
			# The while loop is going to keep going, so I need to make it stop.]
			# I need to make it stop if blank is NOT found.
			print(slots)
			for i in range(0, len(slots)):
				if slots[i]:
					flag = True
				else:
					flag = False
			
			print(slots)

			print(displayed_slots)

			

	print("You win!")

	play_again = input("Do you want to play again? (yes/no) ")
	if play_again == 'no':
		break




				












    
print(slots)