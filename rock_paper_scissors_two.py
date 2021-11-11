"""Ask the user to choose between rock, paper or scissors, then check who has won the game! 
Next print out text letting the player know who has won the game!"""

import random 

def rock_paper_scissors():
    player = input("Please select 'r' for rock, 'p' for paper, or 's' for scissors: ")
    choices = ['r', 'p', 's']
    opponent = random.choice(choices) 

    if player == opponent:
        return print(f"You tied! you and your opponent both selected {opponent}.")

    if check_winner(player, opponent):
        return print(f"You win! You selected {player} and your opponent lost because they chose {opponent}.")

    if check_winner(player, opponent) != True:
        return print(f"You lose! your opponent selected {opponent}.")

def check_winner(user, cpu):
    if (user == 'r' and cpu == 's') or (user == 'p' and cpu == 'r') or (user == 's' and cpu == 'p'):
        return True 

rock_paper_scissors() 
