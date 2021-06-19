import datetime


def id_check() -> None:
    cnp_value = input("Type identification number:\n")
    if cnp_value.isdigit() is False:
        print("The ID must contain numbers only.")
    elif len(cnp_value) == 13:
        an = cnp_value[1:3]
        luna = int(cnp_value[3:5])
        zi = int(cnp_value[5:7])
        sex = int(cnp_value[0])
        county = cnp_value[7:9]
        order_number = cnp_value[9:12]

        if sex == 9:
            print("Foreigner")
        else:
            try:
                if sex == 1 or sex == 2:
                    if not datetime.datetime(int(f"19{an}"), luna, zi):
                        print("Wrong ID number. Please make sure the ID contains a valid DOB")
                    if sex == 1:
                        print("Male born between 1900 - 1999")
                    else:
                        print("Female born between 1900 - 1999")
                elif sex == 3 or sex == 4:
                    if not datetime.datetime(int(f"18{an}"), luna, zi):
                        print("Wrong ID number. Please make sure the ID contains a valid DOB")
                    if sex == 3:
                        print("Male born between 1800 - 1899")
                    else:
                        print("Female born between 1800 - 1899")
                elif sex == 5 or sex == 6:
                    if not datetime.datetime(int(f"20{an}"), luna, zi):
                        print("Wrong ID number. Please make sure the ID contains a valid DOB")
                    if sex == 5:
                        print("Male born between 2000 - 2099")
                    else:
                        print("Female born between 2000 - 2099")

                elif sex == 7 and datetime.datetime(int(f"1900"), 1, 1) < datetime.datetime(int(f"2000"), 12, 31):
                    print("Male, foreign resident born between 1900 si 2000")
                elif sex == 8 and datetime.datetime(int(f"1900"), 1, 1) < datetime.datetime(int(f"2000"), 12, 31):
                    print("Female, foreign resident born between 1900 si 2000")

                pob = {'01': 'Alba', '02': 'Arad', '03': 'Arges', '04': 'Bacau', '05': 'Bihor', '06': 'Bistrita Nasaud',
                       '07': 'Botosani', '08': 'Brasov', '09': 'Braila', '10': 'Buzau', '11': 'Caras Severin', '12': 'Cluj',
                       '13': 'Constanta', '14': 'Covasna', '15': 'Dambovita', '16': 'Dolj', '17': 'Galati', '18': 'Gorj',
                       '19': 'Hargita', '20': 'Hunedoara', '21': 'Ialomita', '22': 'Iasi', '23': 'Ilfov', '24': 'Maramures',
                       '25': 'Mehedinti', '26': 'Mures', '27': 'Neamt', '28': 'Olt', '29': 'Prahova', '30': 'Satu Mare',
                       '31': 'Salaj', '32': 'Sibiu', '33': 'Suceava', '34': 'Teleorman', '35': 'Timis', '36': 'Tulcea',
                       '37': 'Vaslui', '38': 'Valcea', '39': 'Vrancea', '40': 'Bucuresti', '41': 'Bucuresti - Sector 1',
                       '42': 'Bucuresti - Sector 2', '43': 'Bucuresti - Sector 3', '44': 'Bucuresti - Sector 4',
                       '45': 'Bucuresti - Sector 5', '46': 'Bucuresti - Sector 6', '51': 'Calarasi', '52': 'Giurgiu', }

                for key, value in pob.items():
                    if key == county:
                        print(value)

                if int(order_number) == 0:
                    print("ID Error. You were never born ;) !")

                control_number = "279146358279"
                list_sum = []

                for i, v in enumerate(control_number):
                    number_sum = int(control_number[i]) * int(cnp_value[i])
                    list_sum.append(number_sum)

                total = int(sum(list_sum))

                if total % 11 == 10:
                    print("The control number is: 1")
                    if int(total % 11/10) == int(cnp_value[-1]):
                        print("ID verified. The control number is valid!")
                    else:
                        print("ID not verified. Reason: invalid control number!")
                else:
                    print(f"The control number is {total % 11}")

            except ValueError:
                print("Invalid date of birth")
    else:
        print("Incomplete ID number")

    return None


id_check()
