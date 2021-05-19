import datetime

valoare_cnp = input("Introdu cnp-ul:\n")
if valoare_cnp.isdigit() is False:
    print("CNP-ul trebuie sa fie format doar din cifre.")
elif len(valoare_cnp) == 13:
    an = valoare_cnp[1:3]
    luna = int(valoare_cnp[3:5])
    zi = int(valoare_cnp[5:7])
    sex = int(valoare_cnp[0])
    judet = valoare_cnp[7:9]
    numar_ordine = valoare_cnp[9:12]

    if sex == 9:
        print("Persoana straina")
    else:
        try:
            if sex == 1 or sex == 2:
                if not datetime.datetime(int(f"19{an}"), luna, zi):
                    print("CNP gresit. Introduceti o data de nastere valida")
                if sex == 1:
                    print("Sex barbatesc nascut in intervalul 1900 - 1999")
                else:
                    print("Sex femeiesc nascut in intervalul 1900 - 1999")
            elif sex == 3 or sex == 4:
                if not datetime.datetime(int(f"18{an}"), luna, zi):
                    print("CNP gresit. Introduceti o data de nastere valida")
                if sex == 3:
                    print("Sex barbatesc nascut in intervalul 1800 - 1899")
                else:
                    print("Sex femeiesc nascut in intervalul 1800 - 1899")
            elif sex == 5 or sex == 6:
                if not datetime.datetime(int(f"20{an}"), luna, zi):
                    print("CNP gresit. Introduceti o data de nastere valida")
                if sex == 5:
                    print("Sex barbatesc nascut in intervalul 2000 - 2099")
                else:
                    print("Sex femeiesc nascut in intervalul 2000 - 2099")

            elif sex == 7 and datetime.datetime(int(f"1900"), 1, 1) < datetime.datetime(int(f"2000"), 12, 31):  # rescriem
                print("Sex barbatesc, strain rezident si nascut intre 1900 si 2000")
            elif sex == 8 and datetime.datetime(int(f"1900"), 1, 1) < datetime.datetime(int(f"2000"), 12, 31):
                print("Sex femeiesc, strain rezident si nascut intre 1900 si 2000")

        except ValueError:
            print("Data nasterii nu este valida")

else:
    print("CNP incomplet")

pob = {'01': 'Alba', '02': 'Arad', '03': 'Arges', '04': 'Bacau', '05': 'Bihor', '06': 'Bistrita Nasaud',
       '07': 'Botosani', '08': 'Brasov', '09': 'Braila', '10': 'Buzau', '11': 'Caras Severin', '12': 'Cluj',
       '13': 'Constanta', '14': 'Covasna', '15': 'Dambovita', '16': 'Dolj', '17': 'Galati', '18': 'Gorj',
       '19': 'Hargita', '20': 'Hunedoara', '21': 'Ialomnia', '22': 'Iasi', '23': 'Ilfov', '24': 'Maramures',
       '25': 'Mehedinti', '26': 'Mures', '27': 'Neamt', '28': 'Olt', '29': 'Prahova', '30': 'Satu Mare',
       '31': 'Salaj', '32': 'Sibiu', '33': 'Suceava', '34': 'Teleorman', '35': 'Timis', '36': 'Tulcea',
       '37': 'Vaslui', '38': 'Valcea', '39': 'Vrancea', '40': 'Bucuresti', '41': 'Bucuresti - Sector 1',
       '42': 'Bucuresti - Sector 2', '43': 'Bucuresti - Sector 3', '44': 'Bucuresti - Sector 4',
       '45': 'Bucuresti - Sector 5', '46': 'Bucuresti - Sector 6', '51': 'Calarasi', '52': 'Giurgiu', }

for key, value in pob.items(): #reformulam?
    if key == judet:
        print(value)

if int(numar_ordine) == 0:
    print("Eroare CNP. Nu te-ai nascut!")

numar_control = "279146358279"
suma_list = []

for i, v in enumerate(numar_control):
    suma_numere_cnp = int(numar_control[i]) * int(valoare_cnp[i])
    suma_list.append(suma_numere_cnp)
    total = int(sum(suma_list))

if total % 11 == 10:
    print("Numarul de control este: 1")
else:
    print(f"Numarul de control este {total % 11}")




