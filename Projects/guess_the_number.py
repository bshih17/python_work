number_list = []

x = 1
while len(number_list) < 100:
	number_list.append(x)
	x += 1

print(number_list)

guess = input("Guess a number between 1 and 100: ")
guess = int(guess)


