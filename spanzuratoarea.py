import random

secret_word = ["london", "secret", "alaska", "teamwork", "happiness", "homework", "guess", "banana"]
selected_word = list(random.choice(secret_word))
players_tried_letters = []
start_word = []
dict_parts = {1: "@", 2: "/", 3: "\\", 4: "|"}


def draw_man(wrong_letter: int) -> str:
    a = dict_parts[1] if wrong_letter >= 1 else ""
    b = dict_parts[2] if wrong_letter >= 2 else ""
    c = dict_parts[4] if wrong_letter >= 3 else ""
    d = dict_parts[3] if wrong_letter >= 4 else ""
    e = dict_parts[4] if wrong_letter >= 5 else ""
    f = dict_parts[2] if wrong_letter >= 6 else ""
    g = dict_parts[3] if wrong_letter >= 7 else ""

    draw = f"""
            ---------
            |       Y
            |       {a}
            |     {b} {c} {d}
            |       {e}
            |      {f} {g}
          << >>"""
    return draw


def show_partial_word(word_to_be_guessed: list) -> list:
    for letter in word_to_be_guessed:
        if letter == word_to_be_guessed[0] or letter == word_to_be_guessed[-1]:
            start_word.append(letter.lower())
        else:
            start_word.append("_")
    return start_word


def updated_word(word_to_be_guessed: list, letter_chosen: str = "") -> list:
    for index, letter in enumerate(word_to_be_guessed):
        if letter_chosen[:1] == letter:
            start_word[index] = letter_chosen[:1].lower()
    players_tried_letters.append(letter_chosen[:1])
    return start_word


def run_game() -> None:
    player_name = input("Please type your name: ")
    print(f"\nWelcome, {player_name.capitalize()}!\n")
    print("".join(show_partial_word(selected_word)))
    runs = 0
    fails = 0
    while runs < 8:
        if updated_word(selected_word) != selected_word and runs == 7:
            print(f"\nSorry {player_name.capitalize()}, you lost! The word was: {selected_word}!")
            break
        elif updated_word(selected_word) != selected_word:
            guess = input("\nPick a letter: \n |>>> ")
            if guess[:1] not in players_tried_letters and guess[:1] not in start_word:
                print("\n")
                [print(x, end="") for x in updated_word(selected_word, guess)]
                if guess[:1] not in selected_word:
                    print("\n")
                    fails += 1
                    print(draw_man(fails))
                else:
                    print("\n")
                    print(draw_man(fails))
                runs += 1
            else:
                print("\nYou have already tried this letter! Please try another one!")
                continue
        elif updated_word(selected_word) == selected_word:
            print(f"\nCongratulations {player_name.capitalize()}! You won!\n")
            break

    return None


while True:
    selected_word = list(random.choice(secret_word))    # this IS needed here as it refreshes the random word!
    start_word.clear()
    players_tried_letters.clear()
    run_game()
    ask = input('Do you WISH to play another game ("y" for YES or any key for NO)? \n |>>> ')
    if ask.lower() != "y":
        break
