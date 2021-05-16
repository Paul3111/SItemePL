import sys
from tictactoe_functions import *
import tictactoe_game

# Tic Tac Toe game

try:
    games_run = 1
    while True:     # This is where each game starts. Will run until player chooses to stop
        empty_board()     # prints the empty board

        tictactoe_game.game()   # runs the game from the other module

        player_selection = input("\nDo you wish to continue? Press Y/N: \n>>> ")
        if player_selection.lower() == "n":
            print(f"You played {games_run} games!\n")
            print("Game over!")
            sys.exit()

        games_run += 1

except ValueError:
    print("Some error occurred. Please restart!")