import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

url="https://www.isro.gov.in/SpacecraftMissions.html#"
r=requests.get(url)

soup = BeautifulSoup(r.text,"lxml")

table = soup.find("table",class_="table table-info table-striped table-hover table-bordered border-info")

headers = table.find_all("th")

titles = []

for i in headers:
    title = i.text
    title_1 = " ".join(title.split())
    title_2 = title_1.replace("\n","")
    title_3= title_2.replace("⇅","")
    titles.append(title_3)

df = pd.DataFrame(columns=titles)

rows = table.find_all("tr")

f = open("table.csv","+a")
writer = csv.writer(f)
writer.writerow(titles)

for i in rows[1:]:
    index = []
    data = i.find_all("td")
    row = [tr.text for tr in data]
    for j in row:
        j_1 = " ".join(j.split())
        j_2 = j_1.replace("\n","")
        j_3= j_2.replace("⇅","")
        index.append(j_3)
    writer.writerow(index)

f.close()