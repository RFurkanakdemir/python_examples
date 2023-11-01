


# themoviedb.org => dizi arşivi ve bir api VERIr 
# anahtar kelimeye göre arama 
# en popüler film listesi 
# vizyondaki film listesi 


import requests
import json
import os



class Movie:
    def __init__(self,token):
        self.api_url="https://api.themoviedb.org"
        self.token=token
        self.header={"content-type": "application/json; charset=UTF-8",'Authorization':'Bearer {}'.format(self.token)}
    
    def populermovies(self):
        response=requests.get(self.api_url+ "/3/movie/popular?api_key=" + self.token)

        return response.json()

    def vizyonMovies(self):
        response=requests.get(self.api_url+ "/3/movie/now_playing?api_key=" + self.token)
        return response.json()


    def findMovies(self,key):
        self.key=key
        response=requests.get(self.api_url+ "/3/search/movie?api_key=" + self.token +"&query="+self.key)
        return response.json()


print("Merhaba".center(50,"*"))
token=input("Token Bilgisi giriniz: ")
while True:
    
    movie=Movie(token)
    print("Seçim Bölümü".center(50,"*"))
    i=int(input("1-Popüler Film listesi\n2-Vizyondaki film listesi\n3-Anahtar kelime ile Arama\n4-Exit\nSeçiminiz: "))
    if i==1:
        result=movie.populermovies()
        for i in result["results"]:
            print(i["title"])
    elif i==2:
        result=movie.vizyonMovies()
        for i in result["results"]:
            print(i["title"])
    elif i==3:
        key=input("Anahtar Kelime Giriniz: ")
        result=movie.findMovies(key)
        
        for i in result["results"]:
            print(i["title"])
    else:
        break
    
    
    # result=requests.get("https://api.themoviedb.org/3/movie/popular?api_key=d23da6b57074ed83ae93dada17debf26")
    # print(result)