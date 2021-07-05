class Calculator:
    def __init__(self):
        self.nr1 = int(input("a: \t"))
        self.operation = input("operatie: \t")
        self.nr2 = int(input("b: \t"))
        self.rez = 0

    def __str__(self):
        if self.operation == "+":
            return str(self.adunare())
        elif self.operation == "-":
            return str(self.scadere())
        elif self.operation == "*":
            return str(self.inmultire())
        elif self.operation == "/":
            return str(self.impartire())

    def adunare(self):
        return self.nr1 + self.nr2

    def scadere(self):
        return self.nr1 - self.nr2

    def inmultire(self):
            return self.nr1 * self.nr2

    def impartire(self):
        if self.operation == "/":
            if self.nr2 == 0:
                pass
            else:
                return self.nr1 / self.nr2



calcul_1 = Calculator()
# print(calcul_1.adunare(1, "+", 2))
print(calcul_1)

# print(calcul_1.inmultire(5,"*",2))
# print(calcul_1.impartire(4,"/",2))
# print(calcul_1.scadere(4,"+",2)) # eroare
