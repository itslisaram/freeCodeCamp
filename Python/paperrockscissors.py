import random

def get_choices():
    player_choice = input("Emter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice} # dictionaries -> key : value
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}.")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose." 
    elif player == "paper":
        if computer == "rock":
            return "Paper covers the rock! You won!!"
        else:
            return "Scissors cut the paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut the paper! You win!!"
        else:
            return "Rock smashes scissors! You lose."

choices = get_choices() # returns a dictionary
result = check_win(choices["player"], choices["computer"]) # takes the values from the dictionary that are assigned to the keys "player" and "computer"
print(result)