import random

choices = ["rock", "paper", "scissor"]


def play():
    enemy_choice = random.choice(choices)
    player_choice = input(str.lower("Pick either rock, paper, or scissor: "))

    if player_choice == "rock" and enemy_choice == "rock":
        print(f"You picked {player_choice} and The Computer picked {enemy_choice}, its a tie")
    elif player_choice == "rock" and enemy_choice == "paper":
        print(f"You picked {player_choice} and The Computer picked {enemy_choice}, you lose")
    elif player_choice == "rock" and enemy_choice == "sc==sor":
        print(f"You picked {player_choice} and The Computer picked {enemy_choice}, you win")
    elif player_choice == "paper" and enemy_choice == "rock":
        print(f"You picked {player_choice} and The Computer picked {enemy_choice}, you win")
    elif player_choice == "paper" and enemy_choice == "paper":
        print(f"You picked {player_choice} and The Computer picked {enemy_choice}, its a tie")
    elif player_choice == "paper" and enemy_choice == "scissor":
        print(f"You picked {player_choice} and The Computer picked {enemy_choice}, you lose")
    elif player_choice == "scissor" and enemy_choice == "rock":
        print(f"You picked {player_choice} and The Computer picked {enemy_choice}, you lose")
    elif player_choice == "scissor" and enemy_choice == "paper":
        print(f"You picked {player_choice} and The Computer picked {enemy_choice}, you win")
    elif player_choice == "scissor" and enemy_choice == "scissor":
        print(f"You picked {player_choice} and The Computer picked {enemy_choice}, its a tie")
    else:
        quit()


while True:
    play()