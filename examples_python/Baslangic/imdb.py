from urllib import response
import requests
from bs4 import BeautifulSoup


url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
htmlData=requests.get(url).content
soup=BeautifulSoup(htmlData,"html.parser")

liste=soup.find("tbody",{"class":"lister-list"}).find_all("tr")
count=0
for tr in liste:
    title= tr.find("td",{"class":"titleColumn"}).find("a").text
    year=tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
    rated=tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    count+=1
    print(f"{count}-- Film: {title.ljust(40)} Yıl: {year} Puan: {rated}")

