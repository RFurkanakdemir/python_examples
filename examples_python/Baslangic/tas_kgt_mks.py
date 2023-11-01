import random
skorkullanici=0
skorpc=0
print("\nÇıkmak için 'q' tuşunu kullanabilirsiniz\n".center(100,"*"))

def sonuc(pc,kullanici,skorkullanici,skorpc):
    
    if pc==kullanici:
        print("Cevabınız aynı".center(40,'-'))
    elif pc==0 and kullanici==1:
        skorkullanici+=1
        print("Kazandınız".center(20,'*')+"\n")
    elif pc==0 and kullanici==2:
        skorpc+=1
        print("Kaybettiniz".center(20,'*')+"\n")
    elif pc==1 and kullanici==0:
        skorpc+=1
        print("Kaybettiniz".center(20,'*')+"\n")
    elif pc==1 and kullanici==2:
        skorkullanici+=1
        print("Kazandınız".center(20,'*')+"\n")
    elif pc==2 and kullanici==0:
        skorkullanici+=1
        print("Kazandınız".center(20,'*')+"\n")
    elif pc==2 and kullanici==1:
        skorpc+=1
        print("Kaybettiniz".center(20,'*')+"\n")
    else:
        print("Girilen Değer hatalıdır.")

    return skorkullanici,skorpc




while True:
    
    pc=random.randint(0,2)
    grs=input("'0': Taş\n'1': Kağıt\n'2': Makas\nCevabınızı giriniz:  ")
    if grs=="q":
        skorkullanici=0
        skorpc=0
        break
    kullanici=int(grs)
    skr=sonuc(pc,kullanici,skr[2],skr[3])
    print(f"Bilgisayar cevabı: {pc}\nSizin cevabınız: {kullanici}\nAnlık Skor: {skr}\n")


