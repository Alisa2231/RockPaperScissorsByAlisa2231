import random

print("Let's play Rock Paper Scissors!")
play = "y"
while play == "y":
    player_move = input("Choose your weapon - type 'r' for rock, 'p' for paper or 's' for scissors: ")

    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"

    while (player_move not in ["r", "p", "s"]):
        player_move = input("This is not a valid input, please type 'r', 'p' or 's':")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors

    computer_random_number = random.randint(1, 3)
    computer_move = ""
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    result = ""
    draw = "draw"
    player_wins = "player wins"
    computer_wins = "computer wins"

    if player_move == computer_move:
        result = draw
    else:
        if (computer_move == paper and player_move == scissors) or \
                (computer_move == rock and player_move == paper) or \
                (computer_move == scissors and player_move == rock):
            result = player_wins
        else:
            result = computer_wins

    print(f"You chose {player_move} and computer chose {computer_move}!")

    if result == draw:
        print("It's a draw!")
    elif result == player_wins:
        print("Congratulation! You win!")
    elif result == computer_wins:
        print("I am sorry, you lose!")

    print()
    play = input("Wanna play again? y/n ")

    while (play not in ["y", "n"]):
        play = input("This is not a valid input, please type 'y' or 'n'")

    if play == "n":
        print("Thank you for playing!")
        break
