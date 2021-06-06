from pprint import pprint
from statistics import mean

description = ('Country', ['2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ', '2019 '])
dataset = [('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
           ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
           ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
           ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
           ('BG', ['45 ', '51 ', '54 ', '57', '59 ', '64 ', '67 ', '72 ', '75 ']),
           ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 b', ': ', '96 ']),
           ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
           ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
           ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
           ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
           ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
           ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
           ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
           ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
           ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
           ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
           ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
           ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
           ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
           ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99 ', '98 ']),
           ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
           ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
           ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93 b', '95 ']),
           ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 b', '79 ', '82 ', '85 ']),
           ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
           ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79 ', '82 ']),
           ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
           ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
           ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
           ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
           ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
           ('RO', ['47 ', '54 ', '58 ', '61 b', '68 ', '72 ', '76 ', '81 ', '84 ']),
           ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
           ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 b', '95 ', '93 ', '96 ']),
           ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
           ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
           ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84 ', '88 ']),
           ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
           ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']), ]


countries_list = {"AL": "Albania", "AT": "Austria", "BA": "Bosnia and Herzegovina", "BE": "Belgium", "BG": "Bulgaria",
                  "CH": "Switzerland", "CY": "Cyprus", "CZ": "Czech Republic", "DE": "Germany", "DK": "Denmark",
                  "EA": "Unknown", "EE": "Estonia", "EL": "Greece", "ES": "Spain", "FI": "Finland",
                  "FR": "France", "HR": "Croatia", "HU": "Hungary", "IE": "Ireland", "IS": "Iceland",
                  "IT": "Italy", "LT": "Lithuania", "LU": "Luxembourg", "LV": "Latvia", "ME": "Montenegro",
                  "MK": "North Macedonia", "MT": "Malta", "NL": "Netherlands", "NO": "Norway", "PL": "Poland",
                  "PT": "Portugal", "RO": "Romania", "RS": "Serbia", "SE": "Sweden", "SI": "Slovenia",
                  "SK": "Slovakia", "TR": "Turkey", "UK": "United Kingdom", "XK": "Kosovo"}


def get_year_data(year: str, data_list: list = None) -> dict:
    if data_list is None:
        data_list = dataset

    clean_description = [x.strip() for x in description[1]]
    selected_year_index = clean_description.index(year)
    country_code = []
    year_data = []
    for index, items in enumerate(data_list):
        country_code.append(items[0])
        year_data.append(items[1][selected_year_index])

    country_name = []
    country_conversion = [country_name.append(countries_list[c]) for c in country_code if c in countries_list]

    a = zip(country_name, year_data)
    result = {year: list(a)}
    return result


def get_country_data(country: str, data_list: list = None) -> dict:
    if data_list is None:
        data_list = dataset

    clean_description_2 = [y.strip() for y in description[1]]
    clean_description_2.reverse()
    e = []  # if I don't assign empty list here I will get a soft warning on line 88 (it works either way)
    for item in data_list:
        if item[0] == country.upper():
            e = list(item)
            e[1].reverse()

    f = zip(clean_description_2, e[1])
    result = {countries_list[country.upper()].title(): list(f)}
    return result


def perform_average(country4avg: list) -> dict:
    new_list = []
    updated_dict = []
    for item in dataset:
        if item[0] == "".join(country4avg):
            for i in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
                for sub_item in item[1][:i]:
                    a = "".join(x for x in sub_item if x.isdigit())
                    if a.isdigit():
                        sub_item = map(int, item[1][:i]) # not really needed here? maybe use a = int(a)...
                        new_list.append(a)
                    else:
                        sub_item = 0
                mean_list = list(map(int, new_list))
                z = (round(mean(mean_list), 2))
                data_dict = {"coverage": z, "year": description[1][i-1]}
                updated_dict.append(data_dict)
                new_list = []
            result = {countries_list[str("".join(country4avg))]: updated_dict}
            return result


def perform_average_set(data_list: list) -> dict:   # will try to do
    pass


while True:
    menu = [print(x) for x in ["1 - Get YEAR", "2 - Get COUNTRY", "3 - Perform AVERAGE", "0 - EXIT"]]
    select_function = int(input("\nSelect function from the menu (0 - EXIT): \n |>>> "))
    try:
        if select_function == 0:
            print("See you later!")
            break
        elif select_function == 1:
            print(f"\n\t\t>>> You selected [ Get YEAR ] <<<\n")
            insert_year = input(f"Please type the year: \n |>>> ")
            print(f"\n The results for year < {insert_year} > are:\n")
            pprint(get_year_data(insert_year), indent=3, width=50)
            print ("\n")
        elif select_function == 2:
            print(f"\n\t\t>>> You selected [ Get COUNTRY ] <<<\n")
            insert_country = input(f"Please type the country: \n |>>> ")
            for key, value in countries_list.items():
                if insert_country.title() == value.title():
                    insert_country = key
            print(f"\n The results for country < {insert_country.upper()} > are:\n")
            pprint(get_country_data(insert_country), indent=3, width=50)
            print("\n")
        elif select_function == 3:
            print(f"\n\t\t>>> You selected [ Perform AVERAGE ] <<<\n")
            insert_country = input(f"Please type the country: \n |>>> ")
            print(f"\n The results for country < {insert_country.upper()} > are:\n")
            for key, value in countries_list.items():
                if insert_country.title() == value.title():
                    insert_country = key
            pprint(perform_average(list(insert_country.upper())), indent=3, width=100)
            print("\n")
        else:
            continue
    except ValueError:
        print("\nAn error has occurred. Please try again!\n")
        continue
    except IndexError:
        print ("\nAn error has occurred. Please try again!\n")
        continue
