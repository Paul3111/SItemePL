

def empty_board() -> bool:  # prints the empty board when the games starts
    print("\n\n")
    print("--|--|--")
    print("--|--|--")
    print("--|--|--")
    print("\n\n\n\n")
    return True


def print_board_after_move(board) -> bool:  # this function updates the board after each move
    print("\n")
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print("\n")
    return True


def find_winner(list1, list2) -> bool:
    """
    this function checks if the winning combination is found in the player's moves list
    @param list1:
    @param list2:
    @return:
    """
    if len(list(set(list1) & set(list2))) == 3:
        return True
    else:
        return False
