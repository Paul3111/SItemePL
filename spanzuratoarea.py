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