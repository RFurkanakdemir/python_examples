import requests
from bs4 import BeautifulSoup

# url="https://www.n11.com/bilgisayar/dizustu-bilgisayar"
# htmlData=requests.get(url).content
# soup=BeautifulSoup(htmlData,"html.parser")

# liste=soup.find("ul",{"class":"list-ul"}).find_all("li")
i=int(input("aranacak sayfa sayısı"))
for i in range(1,i+1):
    if i ==1:
        url="https://www.n11.com/bilgisayar/dizustu-bilgisayar"
    else:
        url="https://www.n11.com/bilgisayar/dizustu-bilgisayar"+"?pg="+str(i)
    
    htmlData=requests.get(url).content
    soup=BeautifulSoup(htmlData,"html.parser")

    liste=soup.find("ul",{"class":"list-ul"}).find_all("li")
    
    
    for tr in liste:
        title=tr.find("div",{"class":"pro"}).find("a").find("h3",{"class":"productName"}).text
        price=tr.find("div",{"class":"priceContainer"}).find("ins").text
        print(f"Ürün İsmi: {title}\nÜrün Fiyatı: {price}")
