from random import choice

# Rock, Paper, Scissors: you make a move, and the computer makes a move.
possible_moves = ['r', 'p', 's']

# score = [wins, losses, draws]
score = [0, 0, 0]

outcome = ''


print("Welcome to this Rock, Paper, Scissors simulation.")
# print("Input 'rock', 'paper', or 'scissors'.")
print("To choose rock, enter 'r'. To choose paper, enter 'p'. To choose scissors, enter 's'.")
print("Enter 'q' to end the simulation.")

while True:
    your_move = input("\nMake your move: ")
    if your_move == 'q':
        break
    elif your_move != possible_moves[0] and your_move != possible_moves[1] and your_move != possible_moves[2]:
        print("That's not a valid move!")
        continue

    comp_move = choice(possible_moves)

    if your_move == comp_move:
        outcome = 'draw'

    elif your_move == 'r' and comp_move == 'p':
        outcome = 'loss'

    elif your_move == 'r' and comp_move == 's':
        outcome = 'win'
    
    elif your_move == 'p' and comp_move == 'r':
        outcome = 'win'

    elif your_move == 'p' and comp_move == 's':
        outcome = 'loss'
    
    elif your_move == 's' and comp_move == 'r':
        outcome = 'loss'

    elif your_move == 's' and comp_move == 'p':
        outcome = 'win'



    # Turn the abbreviations back into words...?
    if your_move == 'r':
        your_move = 'rock'
    if your_move == 'p':
        your_move = 'paper'
    if your_move == 's':
        your_move = 'scissors'

    if comp_move == 'r':
        comp_move = 'rock'
    if comp_move == 'p':
        comp_move = 'paper'
    if comp_move == 's':
        comp_move = 'scissors'



    if outcome == 'win':
        print(f"You chose {your_move} and the computer chose {comp_move}. You win!")
        score[0] += 1
    elif outcome == 'loss':
        print(f"You chose {your_move} and the computer chose {comp_move}. You lose...")
        score[1] += 1
    else:
        print(f"Both you and the computer chose {your_move}! It's a draw.")
        score[2] += 1

    print(f"Current score: {score[0]} wins, {score[1]} losses, and {score[2]} draws")


print(f"Your final score was {score[0]} wins, {score[1]} losses, and {score[2]} draws.")
print("Thanks for playing.")