import random

secret_word = ["london", "secret", "teamwork","happiness", "homework", "guess"]
vowels = ["a", "e", "i", "o", "u"]
selected_word = random.choice(secret_word)
print(f"The word's length is: {len(selected_word)} letters!")
print(selected_word[:len(selected_word)])

chosen_letter = ""

for letter in selected_word:     # tests if chosen letter repeats within the word
    if selected_word[0].count(letter) > 0:
        print(selected_word.index(letter))
        print(f"The index is: {selected_word.index(letter)}")
        print(f"the first letter is: {selected_word[0].title()}")

    elif selected_word[-1].count(letter) > 0:
        rest_of_word = []
        print(f"The letter was found {selected_word.count(letter)} times.")
        print(f"The index is: {selected_word.index(letter)}")
        print(f"the last letter is: {selected_word[-1].title()}")
        if selected_word.find(selected_word[-1]):
            print(selected_word.replace(selected_word[-1], "_"))
            rest_of_word.append(selected_word[-1])
        # for hidden not in selected_word[1:-1]:

    else:
        rest_of_word = []
        for hidden in selected_word[1:-1]:
            rest_of_word += "_"


# print(f"The word that needs to be guessed is: {selected_word[0].upper() + rest_of_word + selected_word[-1].upper()}")
print(f"The word that needs to be guessed is: {selected_word[0].upper() + str(rest_of_word) + selected_word[-1].upper()}")


# print("guess".index("s"))
# print("guess".count("s"))


# letter = ""
letter_attempt = 0
# word_length = len()

#player_name = input("Please type your name: ")
# while letter_attempt < 7:
#     letter = input("Choose your letter: ")
#     if letter in selected_word:
#         letter_attempt += 1

#7 incercari

# intai afisare cuvant cu x___z - DONE
# check if letters repeat within word
# input letter from player (add to list of selections)
# if letter more than once, reveal all
# check number of lives left after each loop/input
# if _ in list while tries run out then you lost
# continuous loop
# draw the little man

# VERSION 2 ------VERSION 2 ---------- VERSION 2 ------------- VERSION 2 ------------- VERSION 2-----------------

# import random
#
# secret_word = ["london", "secret", "alaska", "teamwork", "happiness", "homework", "guess", "banana"]
# selected_word = random.choice(secret_word)
# players_word = []
# players_tried_letters = []
# print("This is the word that must be guessed ", list(selected_word))
#
# player_name = input("Please type your name: ")
# print(f"\nWelcome, {player_name}!")
#
# ##Show drawing
# ##two dimensional list? use coords to fill what you need to fill and only print those?
#
# print(selected_word[0] + "_" * (len(selected_word)-2) + selected_word[-1])
#
# first_letter = selected_word[0]
# last_letter = selected_word[-1]
# players_word.insert(0, first_letter)
# players_word.append(last_letter)
# players_tried_letters.insert(0, first_letter)
# players_tried_letters.append(last_letter)
#
# runs = 0
# while runs < 7:
#     guess = input("\nPick a letter: ")
#     if guess not in players_tried_letters:
#         players_tried_letters.insert(-1, guess)
#         ## print(players_word)
#         for checked_letter in selected_word:
#             if first_letter == checked_letter:
#                 print(first_letter, end="")
#             elif last_letter == checked_letter:
#                 print(last_letter, end="")
#             elif guess in checked_letter:
#                 position = selected_word.index(checked_letter)
#                 ## print(f"The char position is {position}")
#                 print(checked_letter, end="")
#                 players_word.insert(position, guess)
#                 ## print(f"\nplayer's word is: {players_word}")
#             else:
#                 print("_", end="")
#         runs += 1
#
#     else:
#         print("\nYou have already tried this letter. Please try another or press 9 to exit!")
#
#
# if selected_word == players_word:
#     print(f"Congrats {player_name}, you won!")
# else:
#     print(f"\nYou lost!")
#     print(f"Letters tried: ", players_tried_letters)

## letter IS in secret word ---> player guessed all letters and won
## letter IS NOT in secret word ---> player ran out of guesses and lost
## check if player won

## if loop is over game over and the drawing is finished
## ask player if he/she wishes to play again

##7 incercari - DONE

## intai afisare cuvant cu x___z - DONE
## check if letters repeat within word - DONE
## input letter from player (add to list of selections) - DONE
## if letter more than once, reveal all - DONE
## check number of lives left after each loop/input - DONE
## if _ in list while tries run out then you lost - DONE
## continuous loop - DONE
## draw the little man