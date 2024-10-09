### For computer vs player ###

# import random

# # RPS choices listed

# rps = ["rock", "paper", "scissors"]

# # set computer and player

# player_score = 0
# computer_score = 0

# player_choice = ""
# game_on = True

# print("Let's play a game of rock-paper-scissors to 3 points.")

# while game_on:
#     # loop back to ask for correct choice
#     while player_choice not in rps:
#         player_choice = input("Pick rock, paper, or scissors: ")
#         if player_choice not in rps:
#             print("Please pick a valid option.")

#     computer_choice = random.choice(rps)

#     # game logic

#     if player_choice == computer_choice:
#         print(f"You picked {player_choice} and computer picked {computer_choice}, draw.")
#     elif (player_choice == "rock" and computer_choice == "paper") or (player_choice == "scissors" and computer_choice == "rock") or (player_choice == "paper" and computer_choice == "scissors"):
#         print(f"You picked {player_choice} and computer picked {computer_choice}, you lose.")
#         computer_score += 1
#     else:
#         print(f"Player picked {player_choice} and computer picked {computer_choice}, you win.")
#         player_score += 1

#     print(f"Your score: {player_score}. Computer's score: {computer_score}.")

#     # reset player_choice for the while loop
#     player_choice = ""

#     if player_score > 2 or computer_score > 2:
#         game_on = False
#         print("Game over, thank you for playing.")

################# For player vs player #####################

import random

# RPS choices listed

rps = ["rock", "paper", "scissors"]

# set computer and player

player1_score = 0
player2_score = 0

player1_choice = ""
player2_choice = ""
game_on = True

print("Let's play a game of rock-paper-scissors to 3 points.")

while game_on:
    # loop back to ask for correct choice
    while player1_choice not in rps or player2_choice not in rps:
        player1_choice = input("Player 1, please pick rock, paper, or scissors: ")
        player2_choice = input("Player 2, please pick rock, paper, or scissors: ")

        if player1_choice not in rps:
            print("Player 1, please pick a valid option.")
        if player2_choice not in rps:
            print("Player 2, please pick a valid option.")
    
    # game logic

    if player1_choice == player2_choice:
        print(f"Player 1 picked {player1_choice} and Player 2 picked {player2_choice}, draw.")
    elif (player1_choice == "rock" and player2_choice == "paper") or (player1_choice == "scissors" and player2_choice == "rock") or (player1_choice == "paper" and player2_choice == "scissors"):
        print(f"Player 1 picked {player1_choice} and Player 2 picked {player2_choice}, Player 1 loses.")
        player2_score += 1
    else:
        print(f"Player 1 picked {player1_choice} and Player 2 picked {player2_choice}, Player 1 wins.")
        player1_score += 1

    print(f"Player 1 score: {player1_score}. Player 2's score: {player2_score}.")
    
    # reset player_choice for the while loop
    # maybe a better way for this here?
    player1_choice = ""
    player2_choice = ""

    if player1_score > 2 or player2_score > 2:
        game_on = False
        print("Game over, thank you for playing.")


