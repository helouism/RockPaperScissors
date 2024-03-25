import sys 
import random

# Dictionary of all of the possible outcome 
combinations = {
    11 : "Computer picks Rock too, It's a Draw",
    22 : "Computer picks Paper too, It's a Draw",
    33 : "Computer picks Scissors too, It's a Draw",
    12 : "Computer picks Paper, You Lose",
    13 : "Computer picks Scissors, You Win",
    21 : "Computer picks Rock, You Win",
    23 : "Computer picks Scissors, You Lose",
    31 : "Computer picks Rock, You Lose",
    32 : "Computer picks Paper, You Win"
}

games_result = []

# Takes user input and use random.randint for computer move
def user_input():
    user_move = input(("Enter a number :\n1.Rock\n2.Paper\n3.Scissors"))
    computer_move = random.randint(1,3)
    decide_winner(user_move, computer_move)
    
# Access combinations key to output the winner
def decide_winner(x, y):
    games_result.append(str(x))
    games_result.append(str(y))
    games_result_converted = "".join(games_result)
    print(combinations[int(games_result_converted)])
    


choice = int(input("Do you want to play\nEnter a number\n1. Yes\n2. No"))

if choice == 1:
    user_input()
else:
    sys.exit()
