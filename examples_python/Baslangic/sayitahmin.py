import random


rast=random.randint(0,100)

hak=5
eksipuan=100/hak
tpuan=100
while(hak>0):
    hak-=1
    tahmin=int(input("tahmin giriniz: "))
    if(tahmin>rast):
        print("daha küçük değer giriniz")
        tpuan=tpuan-eksipuan
    else:
        print("daha yüksek değer giriniz")
        tpuan=tpuan-eksipuan


    if(tahmin ==rast):
        print(f"tebrikler doğru bildiniz puanınız: {tpuan}")

        break
    
   

print("hakkınız bitmiştir tekrar deneyiniz")