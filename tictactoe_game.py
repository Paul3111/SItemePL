import random
import time
from tictactoe_functions import print_board_after_move, find_winner


def game():
    board_structure = {1: "--", 2: "--", 3: "--", 4: "--", 5: "--", 6: "--", 7: "--", 8: "--", 9: "--", }

    # These are all possible (unique or sorted) winning combinations
    winning_combination1 = [1, 2, 3]  # if player fills 1 2 3 in any order (horizontal)
    winning_combination2 = [4, 5, 6]  # if player fills 4 5 6 in any order (horizontal)
    winning_combination3 = [7, 8, 9]  # if player fills 7 8 9 in any order (horizontal)
    winning_combination4 = [1, 4, 7]  # if player fills 1 4 7 in any order (vertical)
    winning_combination5 = [2, 5, 8]  # if player fills 2 5 8 in any order (vertical)
    winning_combination6 = [3, 6, 9]  # if player fills 3 6 9 in any order (vertical)
    winning_combination7 = [1, 5, 9]  # if player fills 1 5 9 in any order (diagonal)
    winning_combination8 = [3, 5, 7]  # if player fills 3 5 7 in any order (diagonal)
    winning_combinations = [winning_combination1, winning_combination2, winning_combination3, winning_combination4,
                            winning_combination5, winning_combination6, winning_combination7, winning_combination8]

    preferred_positions1 = [1, 3, 5, 7, 9]  # used to select from this list first (robot)
    preferred_positions2 = [2, 4, 6, 8]     # used to select from this list last (robot)
    all_positions = preferred_positions1 + preferred_positions2
    player_moves_list = []
    robot_moves_list = []

    player_name = input("\nPlease type your name (press Q to exit): ")
    while player_name == "":  # loop that makes sure that the player's name is not Q and not a space char
        if player_name.lower() == "q":
            break
        else:
            print("\tYou must enter a name!")
            player_name = input("\nPlease type your name (press Q to exit): ")

    if player_name.lower() != "q":  # only runs if Q is not pressed
        print("\n\n\t\t*** TIC-TAC-TOE GAME ***\n\n")
        print(f"Welcome, {player_name.title()}!\n")
        print("Starting game in 3 seconds. Deciding who moves first...\n")
        time.sleep(3)

        global who_moves
        who_moves = random.choice([player_name, "Robo"])    # chooses randomly who will make the first move

        for rounds in range(1, 10):
            # checks if the player has won
            if find_winner(player_moves_list, winning_combination1)\
                    or find_winner(player_moves_list, winning_combination2)\
                    or find_winner(player_moves_list, winning_combination3)\
                    or find_winner(player_moves_list, winning_combination4)\
                    or find_winner(player_moves_list, winning_combination5)\
                    or find_winner(player_moves_list, winning_combination6)\
                    or find_winner(player_moves_list, winning_combination7)\
                    or find_winner(player_moves_list, winning_combination8):
                print(f"Congrats, {player_name.title()}, you won!")
                break
            # checks if the robot has won
            elif find_winner(robot_moves_list, winning_combination1)\
                    or find_winner(robot_moves_list, winning_combination2)\
                    or find_winner(robot_moves_list, winning_combination3)\
                    or find_winner(robot_moves_list, winning_combination4)\
                    or find_winner(robot_moves_list, winning_combination5)\
                    or find_winner(robot_moves_list, winning_combination6)\
                    or find_winner(robot_moves_list, winning_combination7)\
                    or find_winner(robot_moves_list, winning_combination8):
                print(f"Hey, {player_name.title()}, YOU LOST and Robo won!")
                break
            elif player_moves_list not in winning_combinations and robot_moves_list not in winning_combinations:
                if preferred_positions1:
                    robot_choice = random.choice(preferred_positions1)
                else:
                    robot_choice = random.choice(preferred_positions2)

                print(f"\n\t\tPlease make move {rounds} now!")

                if who_moves == "Robo":     # if the robot moves first, it will always choose 5
                    if 5 in preferred_positions1:
                        board_structure[5] = " O"   # fills the board[position 5] with zero
                        robot_moves_list.append(5)
                        preferred_positions1.remove(5)
                        all_positions.remove(5)
                        print_board_after_move(board_structure)
                        print("Robo made his move!\n")
                        print(f"Robot's moves are: " + str(robot_moves_list))
                        who_moves = player_name
                    else:
                        board_structure[robot_choice] = " O"
                        robot_moves_list.append(robot_choice)
                        if robot_choice in preferred_positions1:
                            preferred_positions1.remove(robot_choice)
                        if robot_choice in preferred_positions2:
                            preferred_positions2.remove(robot_choice)
                        all_positions.remove(robot_choice)
                        print_board_after_move(board_structure)
                        print("Robo made his move!\n")
                        print(f"Robot's moves are: " + str(robot_moves_list))
                        who_moves = player_name

                elif who_moves == player_name:
                    try:
                        move = int(input(f"\nWhere would you like to move, {player_name.title()}?\n>>> "))
                        board_structure[move] = " X"
                        player_moves_list.append(move)
                        if move in preferred_positions1:
                            preferred_positions1.remove(move)
                            all_positions.remove(move)
                        if move in preferred_positions2:
                            preferred_positions2.remove(move)
                            all_positions.remove(move)
                        print_board_after_move(board_structure)
                        print(f"{player_name.title()}'s moves are: {player_moves_list}")
                        who_moves = "Robo"
                    except IndexError:
                        print("Please try an available position on the board!")
                        pass
                        # continue
            else:
                print("It's a draw!")
                break

            print("Available positions ", all_positions)

    else:
        print("\nSee you later!")
        pass
