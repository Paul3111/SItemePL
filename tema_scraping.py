import requests
from bs4 import BeautifulSoup
# import xlsxwriter


############################# VERSION 1 - Main #################################

# for covid_days in range(14, 21):
#     covid_link = (f"https://www.mai.gov.ro/informare-covid-19-grupul-de"
#                   f"-comunicare-strategica-{covid_days}-ianuarie-ora-13-00/")
#
#     r = requests.get(covid_link)
#     s1 = BeautifulSoup(r.text, "html.parser")
#
#     file = open(f"covid_data_{covid_days}.csv", "w", encoding="utf-8")
#
#     for tr in s1.table.select("tr"):
#         for value in tr.select("td"):
#             if "," in value.text:
#                 a = value.text.replace(",", ".")
#                 file.write(f"{a},")
#             else:
#                 file.write(f"{value.text},")
#         file.write("\n")


############################# VERSION 2 - Functions (access any link) #################################

# def get_covid_data(day_covid: int, month_covid: str) -> str:
#     covid_link = (f"https://www.mai.gov.ro/informare-covid-19-grupul-de"
#                   f"-comunicare-strategica-{day_covid}-{month_covid.lower ()}-ora-13-00/")
#     # print(covid_link)
#     r = requests.get (covid_link)
#     s1 = BeautifulSoup (r.text, "html.parser")
#
#     file = open (f"covid_data_{month_covid}.{day_covid}.csv", "w", encoding="utf-8")
#
#     for tr in s1.table.select("tr"):
#         for value in tr.select ("td"):
#             if "," in value.text:
#                 a = value.text.replace (",", ".")
#                 file.write(f"{a},")
#             else:
#                 file.write (f"{value.text},")
#         file.write ("\n")
#     return f"Report generated for {day_covid}-{month_covid}!"
#
#
# get_covid_data(15, "februarie")


######################## VERSION 3 - Multiple dates on one file #################################

start_date = 14
end_date = 21
month = "ianuarie"

for covid_days in range(start_date, end_date):
    covid_link = (f"https://www.mai.gov.ro/informare-covid-19-grupul-de"
                  f"-comunicare-strategica-{covid_days}-{month}-ora-13-00/")

    r = requests.get(covid_link)
    s1 = BeautifulSoup(r.text, "html.parser")

    file = open(f"covid_data_multiple_days.csv", "a+", encoding="utf-8")

    file.write("\n")
    file.write(f"Valori pentru {covid_days} {month}")
    file.write("\n")

    for tr in s1.table.select("tr"):
        for value in tr.select("td"):
            if "," in value.text:
                a = value.text.replace(",", ".")
                file.write(f"{a},")
            else:
                file.write(f"{value.text},")
        file.write("\n")


############################# VERSION 4 (NOT WORKING) #################################

# for covid_days in range(14, 21):
#     covid_link = (f"https://www.mai.gov.ro/informare-covid-19-grupul-de"
#                   f"-comunicare-strategica-{covid_days}-ianuarie-ora-13-00/")
#
#     r = requests.get(covid_link)
#     s1 = BeautifulSoup(r.text, "html.parser")
#
#     workbook = xlsxwriter.Workbook(f"covid_data_{covid_days}.xls")
#     worksheet = workbook.add_worksheet()
#
#     for tr in s1.table.select("tr"):
#         for value in tr.select("td"):
#             if "," in value.text:
#                 a = value.text.replace(",", ".")
#                 worksheet.write(str(a))
#             else:
#                 worksheet.write(str(value))
#         worksheet.write("\n")


