from bs4 import BeautifulSoup
import requests
import pandas as pd

url="https://www.scrapethissite.com/pages/simple/"

html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")

countrys = []
capitals = []
populations =  []
areas = []

for link in soup.find_all("div", attrs={"class": "country"}):
    countrys.append(link.find('h3').text.strip())
    capitals.append(link.find('span', attrs={"class": "country-capital"} ).text)
    populations.append(link.find('span', attrs={"class": "country-population"} ).text)
    areas.append(link.find('span', attrs={"class": "country-area"} ).text)


data = {
    "nome": countrys,
    "capital": capitals,
    "populacao": populations,
    "area" : areas
}

df = pd.DataFrame(data)
df.to_csv("paises.csv", index=False)