

def empty_board():  # prints the empty board when the games starts
    print("\n\n")
    print("--|--|--")
    print("--|--|--")
    print("--|--|--")
    print("\n\n\n\n")


def print_board_after_move(board):  #this function updates the board after each move
    print("\n")
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print("\n")


def find_winner(list1, list2):  # this function checks if the winning combination is found in the player's moves list
    if len(list(set(list1) & set(list2))) == 3:
        return True
    else:
        return False
