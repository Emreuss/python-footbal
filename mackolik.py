import requests
from bs4 import BeautifulSoup
import json 
import pandas as pd
from pandas import json_normalize
import re
import ast

url = "https://arsiv.mackolik.com/Mac/3689402/Fenerbahce-Kayserispor"

regex = r"(?<=homePlayerList\s\=\s)[\s\S]*?(?=\n.*?=|$)"
regex_2 = r"(?<=awayPlayerList\s\=\s)[\s\S]*?(?=\n.*?=|$)"

response = requests.get(url)
html_input = response.content
soup=BeautifulSoup(html_input,"html.parser")
#print(soup.title)
script = soup.find_all('script')[47]  
#print(script)
homeplayerlist = re.finditer(regex, str(script) , re.MULTILINE)
#print(homeplayerlist)

for matchNum, match in enumerate(homeplayerlist, start=1):
       #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
       homeplayerlst = str(match.group())
       homeplayerlst = homeplayerlst.replace(";", "") \
        .replace('id:','"id":') \
        .replace('name:','"name":') \
        .replace('country:','"country":') \
        .replace('pass:','"pass":') \
        .replace('sot:','"sot":') \
        .replace('ts:','"ts":') \
        .replace('x:','"x":') \
        .replace('y:','"y":') \
        .replace('shirt:','"shirt":') \
        .replace('side:','"side":')       


#print(homeplayerlst)
homeplayerlst_fenerbahce = json.loads(homeplayerlst)
fenerbahce_ilkonbir = pd.DataFrame.from_records(homeplayerlst_fenerbahce)
#fenerbahce_ilkonbir.to_csv('fenerbahce_ilkonbir.csv',index=False)
print(fenerbahce_ilkonbir)

awayplayerlist = re.finditer(regex_2, str(script) , re.MULTILINE)

for matchNum, match in enumerate(awayplayerlist, start=1):
       #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
       awayplayerlst = str(match.group())
       awayplayerlst = awayplayerlst.replace(";", "") \
        .replace('id:','"id":') \
        .replace('name:','"name":') \
        .replace('country:','"country":') \
        .replace('pass:','"pass":') \
        .replace('sot:','"sot":') \
        .replace('ts:','"ts":') \
        .replace('x:','"x":') \
        .replace('y:','"y":') \
        .replace('shirt:','"shirt":') \
        .replace('side:','"side":') 

#print(awayplayerlst)
awayplayerlst_kayseri = json.loads(awayplayerlst)
kayseri_ilkonbir = pd.DataFrame.from_records(awayplayerlst_kayseri)
#kayseri_ilkonbir.to_csv('kayseri_ilkonbir.csv',index=False)
print(kayseri_ilkonbir)