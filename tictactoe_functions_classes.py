class Board:
    # def __init__(self):
    #     self.x = 0

    def empty_board(self):  # prints the empty board when the games starts
        print("\n\n")
        print("--|--|--")
        print("--|--|--")
        print("--|--|--")
        print("\n\n\n\n")
        return "\n"

    def print_board_after_move(self, board):  #this function updates the board after each move
        print("\n")
        print(f"{board[1]} | {board[2]} | {board[3]}")
        print(f"{board[4]} | {board[5]} | {board[6]}")
        print(f"{board[7]} | {board[8]} | {board[9]}")
        print("\n")
        return "\n"

    def find_winner(self, list1, list2):  # this function checks if the winning combination is found in the player's moves list
        if len(list(set(list1) & set(list2))) == 3:
            return True
        else:
            return False

    @staticmethod
    def draw_man(wrong_letter: int) -> str:
        dict_parts = {1: "@", 2: "/", 3: "\\", 4: "|"}
        a = dict_parts[1] if wrong_letter >= 1 else ""
        b = dict_parts[2] if wrong_letter >= 2 else ""
        c = dict_parts[4] if wrong_letter >= 3 else ""
        d = dict_parts[3] if wrong_letter >= 4 else ""
        e = dict_parts[4] if wrong_letter >= 5 else ""
        f = dict_parts[2] if wrong_letter >= 6 else ""
        g = dict_parts[3] if wrong_letter >= 7 else ""

        draw = f"""
                ---------
                |       ^
                |       {a}
                |     {b} {c} {d}
                |       {e}
                |      {f} {g}
              << >>"""
        return draw

# board_1 = Board()
# print(board_1.empty_board())
