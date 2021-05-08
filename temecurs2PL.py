your_name = input("Please type your name to start: ")

mesaj1 = input("Please type your string here (metoda 1): ") #celelalte metode interpreteaza 0.2 ca fiind string, nu float...
if mesaj1.isdigit() == True:
    print(f"{your_name}, you typed a number (metoda 1)")
elif mesaj1.isdigit == False:
    print(f"{your_name}, you typed a text (metoda 1)")
else:
    print(f"{your_name}, you typed a float (metoda 1)")


mesaj2 = input("Please type your string here (method 2) : ") #Metoda 2 nu functioneaza si nu stiu de ce
# mesaj2check = isinstance(mesaj2, str)
if isinstance(mesaj2,str):
    print(f"{your_name}, you typed a text (metoda 2)")
else:
    print(f"{your_name}, you typed a number (metoda 2)")


mesaj3 = input("Please type your string here (method 3): ")
if type(mesaj3) == "str":
    print(f"{your_name}, you typed a text (metoda 3)")
else:
    print(f"{your_name}, you typed a number (metoda 3)")
