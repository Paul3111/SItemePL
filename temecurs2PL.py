import time

#Exercise 1
your_name = input(f"\n\tExercise 1. Please type your name to start: ")

mesaj1 = input("Please type your string here (metoda 1): ") #celelalte metode interpreteaza 0.2 ca fiind string, nu float...
if mesaj1.isdigit():
    print(f"{your_name}, you typed a number (metoda 1)")
elif not mesaj1.isdigit():
    print(f"{your_name}, you typed a text or a float number (metoda 1)")
else:
    print(f"some other error occurred")


mesaj2 = input("Please type your string here (method 2) : ") #Metoda 2 nu functioneaza si nu stiu de ce
# mesaj2check = isinstance(mesaj2, str)
if isinstance(mesaj2,str):
    print(f"{your_name}, you typed a text (metoda 2) - incorrect result")
else:
    print(f"{your_name}, you typed a number (metoda 2) - incorrect result")


mesaj3 = input("Please type your string here (method 3): ") #nu functioneaza corect pt ca input returneaza str?
if type(mesaj3) == "str":
    print(f"{your_name}, you typed a number (metoda 3) - incorrect result")
else:
    print(f"{your_name}, you typed a text (metoda 3) - incorrect result")

#Exercise 2
your_number = input(f"\n\tExercise 2. Please type a number: ")

if your_number.isdigit():
    if int(your_number) % 2 == 0:
        print (f"Your number:{your_number} is an even number!")
    else:
        print (f"Your number: {your_number} is an odd number!")
else:
    print ("You did not type an integer number")

#Exercise 3
your_year = input(f"\n\tExercise 3. Please insert a year: ")
if int(your_year) % 4 == 0:
    print(f"Year {your_year} is a leap year!")
else:
    print("Year {} is not a leap year!".format(your_year))

#Exercise 4
try:
    your_number2 = int(input(f"\n\tExercise 4.  Please insert another number: "))
    if int(your_number2) > 0:
        if int(your_number2) >= 10:
            print("Number ({}) is a positive number and it is larger or equal to 10!\n".format(your_number2))
        else:
            print("Number ({}) is positive number and it is lower than 10!\n".format(your_number2))
    elif int(your_number2) < 0:
        converted_to_positive = abs(your_number2)
        print(f"Think positive. Your number is now ({converted_to_positive})\n")
    elif int(your_number2) == 0:
        print("Your number is zero!\n")
except ValueError:
    print("Please type a number, not a letter!\n")

time.sleep(2)

#Exercise 5:
print("Exercise 5:")
menu_item = ["Menu","Afisare lista de cumparaturi","Adaugare element","Stergere element","Stergere lista de cumparaturi"
    ,"Cautare in lista de cumparaturi"]
for item in enumerate(menu_item):
    print(item)
selected_item = int(input("\n\tPlease select an option (type a number between 1 and 5): "))

try:
    if selected_item in range(1,5):
        print(f"{selected_item} - ", menu_item[selected_item])
except IndexError:
    print("\nOption not available. Please make sure you only select a number between 1 and 5!")


#Exercise 5 - Version 2
# print("Exercise 5:")
# menu_item = ["1 - Afisare lista de cumparaturi","2 - Adaugare element","3 - Stergere element","4 - Stergere lista de cumparaturi"
#     ,"5 - Cautare in lista de cumparaturi"]
# for item in menu_item:
#     print(item)
#
# selected_item = int(input("Please select an option (type a number between 1 and 5): "))
#
# if selected_item == 1:
#     print("Afisare lista de cumparaturi")
# elif selected_item == 2:
#     print("Adaugare element")
# elif selected_item == 3:
#     print("Stergere element")
# elif selected_item == 4:
#     print("Stergere lista de cumparaturi")
# elif selected_item == 5:
#     print("Cautare in lista de cumparaturi")
# else:
#     print("Option not available. Please select a number between 1 and 5.")