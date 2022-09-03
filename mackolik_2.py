import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://arsiv.mackolik.com/Mac/3689402/Fenerbahce-Kayserispor"
response = requests.get(url)
html_input = response.content
soup=BeautifulSoup(html_input,"html.parser")
value_hometeam= soup.find_all("div",attrs={"class":"team-1-statistics-text"})
print(value_hometeam)
parametre = soup.find_all("div",attrs={"class":"statistics-title-text"})
print(parametre)
value_awayteam= soup.find_all("div",attrs={"class":"team-2-statistics-text"})
print(value_awayteam)

fenerbahce_matchdata= list()
kayseri_matchdata= list()

for i in range(len(parametre)):
    parametre[i] = (parametre[i].text).strip("\n").strip()
    value_hometeam[i] = (value_hometeam[i].text).strip("\n").strip()
    fenerbahce_matchdata.append([parametre[i],value_hometeam[i]])

fenerbahce_matchdata = pd.DataFrame(fenerbahce_matchdata , columns= ["Parametre","Deger"])
fenerbahce_matchdata["Takım"] = "Fenerbahçe"
#fenerbahce_matchdata.to_csv("fenerbahcematchdata.csv",index=False)

for i in range(len(parametre)):
    # parametre[i] = (parametre[i].text).strip("\n").strip()
    value_awayteam[i] = (value_awayteam[i].text).strip("\n").strip()
    kayseri_matchdata.append([parametre[i],value_awayteam[i]])

kayseri_matchdata = pd.DataFrame(kayseri_matchdata , columns= ["Parametre","Deger"])
kayseri_matchdata["Takım"] = "Kayseri"
kayseri_matchdata.to_csv("kayserimatchdata.csv",index=False)
