class Calculator:
    def __init__(self):
        self.nr1 = 0
        self.operation = ""
        self.nr2 = 0
        self.rez = 0

    def adunare(self, nr1, operation, nr2):
        if operation == "+":
            rez = nr1 + nr2
            return rez

    def scadere(self, nr1, operation, nr2):
        if operation == "-":
            rez = nr1 - nr2
            return rez

    def inmultire(self, nr1, operation, nr2):
        if operation == "*":
            rez = nr1 * nr2
            return rez

    def impartire(self, nr1, operation, nr2):
        if operation == "/":
            if nr2 == 0:
                pass
            else:
                rez = nr1 / nr2
                return rez


calcul_1 = Calculator()
print(calcul_1.adunare(1, "+", 2))
print(calcul_1.scadere(9,"-",2))
print(calcul_1.inmultire(5,"*",2))
print(calcul_1.impartire(4,"/",2))
print(calcul_1.scadere(4,"+",2)) # eroare
