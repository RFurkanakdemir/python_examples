# isim = input("isim giriniz: ")
# yas= int(input("yas giriniz: "))
# egitim=input("eğitim seviyeniz: ")

# if(yas>18)and ((egitim=="üniversite")or (egitim=="lise")):
#     print(f"sayın {isim} ehliyet almaya uygunsunuz")
# else:
#     print(f"sayın {isim} ehliyet almaya uygun değilsiniz")

# yazili1=int(input("1. yazılı notu: "))
# yazili2=int(input("2. yazılı notu: "))
# sözlü=int(input("sözlü notu: "))
# ortalama=(yazili1+yazili2+sözlü)/3

# if ortalama>=0 and ortalama<25:
#     print("notunuz 0 dır")
# elif ortalama>=25 and ortalama<45:
#     print("notunuz 1 dir")
# elif ortalama >=45 and ortalama<55:
#     print("notunuz 2 dir")
# elif ortalama>=55 and ortalama<70:
#     print("notunuz 3 dür")
# elif ortalama>=70 and ortalama<85:
#     print("notunuz 4 tür")
# elif ortalama >=85 and ortalama<=100:
#     print("notunuz 5")
# else:
#     print("not aralığı yanlıştır")


import datetime

bugün=datetime.datetime.today()
tarih=input("trafiğe çıkış tarihinizi giriniz yıl/ay/gün")
tarih=tarih.split(".")
yıl=int(tarih[0])
ay=int(tarih[1])
gün=int(tarih[2])
trafik=datetime.datetime(yıl,ay,gün)
fark=bugün-trafik
gecenzaman=fark.days
print(f"aracınız {gecenzaman} gündür trafikte------\n")
if gecenzaman>=365 and gecenzaman<365*2:
    print("1.bakıma gidiniz")
elif gecenzaman>=365*2 and gecenzaman<365*3:
    print("2. bakım zamanı")
elif gecenzaman >=365*3 and gecenzaman<365*4:
    print("3. bakım yılınız")
else:
    print(f"araç trafiğe çıkalı {gecenzaman} gün oldu")


print(f"\naracınız {gecenzaman} gündür trafikte------")