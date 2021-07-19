import requests
from bs4 import BeautifulSoup

for covid_days in range(14, 21):
    covid_link = (f"https://www.mai.gov.ro/informare-covid-19-grupul-de"
                  f"-comunicare-strategica-{covid_days}-ianuarie-ora-13-00/")

    r = requests.get(covid_link)
    s1 = BeautifulSoup(r.text, "html.parser")

    file = open(f"covid_data_{covid_days}.csv", "w", encoding="utf-8")

    for tr in s1.table.select("tr"):
        for value in tr.select("td"):
            if "," in value.text:
                a = value.text.replace(",", ".")
                file.write(f"{a},")
            else:
                file.write(f"{value.text},")
        file.write("\n")
