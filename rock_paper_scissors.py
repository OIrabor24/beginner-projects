import random 

def play():
    user = input("Choose 'r' for rock, 'p' for paper, or 's' for scissors: ")
    computer = random.choice(['r', 'p', 's']) 

    if not is_win(user, computer):
        return F"{user} not allowed!"

    if user == computer:
        return f"You tied! your opponent selected {computer}!"

    if is_win(user, computer):
        return f"You won {user} beats {computer}!"

    if is_win(user, computer) != True:
        return f"You lost! {computer} wins!"

def is_win(player, opponent):
    # r > s s > p p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True 

print(play()) 
