def not_hesap(i):
    i=i[:-1]
    liste=i.split(':')
    ögrenciad=liste[0]
    notlar=liste[1].split(",")
    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])
    ortalama=(not1+not2+not3)/3
    if ortalama>90 and ortalama<=100:
        harf="AA"
    elif ortalama >=80 and ortalama<=89:
        harf="BA"
    elif ortalama >=75 and ortalama<=80:
        harf="BB"
    elif ortalama >=70 and ortalama<=75:
        harf="CB"
    elif ortalama >=60 and ortalama<=69:
        harf="CC"
    elif ortalama >=50 and ortalama<=59:
        harf="DC"
    elif ortalama >=40 and ortalama<=49:
        harf="DD"
    elif ortalama >=30 and ortalama<=39:
        harf="FD"
    else:
        harf="FF"
    
    return ögrenciad+": " +str(ortalama)+ "   " + harf+ "\n"




def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8")as file:
        for i in file:
            
            print(not_hesap(i))


def notGir():
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    not1= input("Not-1: ")
    not2 = input("Not-2: ")
    not3= input("Not-3: ")

    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad+ " "+ soyad+ ":"+ not1+","+not2+","+not3+"\n")


def notKayit():
    with open("sinav_notlari.txt","r",encoding="utf-8")as file:
        liste=[]
        for i in file:
            liste.append(not_hesap(i))

        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)

while True:
    islem = input("1-Notları oku\n2-Not Gir: \n3-Notları Kaydet: \n4-Çıkış\n")

    if islem=="1":
        ortalamalari_oku()
    elif islem=="2":
        notGir()
    elif islem=="3":
        notKayit()
    else:
        break
