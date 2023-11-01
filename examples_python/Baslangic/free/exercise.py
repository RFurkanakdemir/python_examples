#-------------1
# Kullanıcıdan adını ve yaşını girmesini isteyen bir program oluşturun. 
# Onlara, 100 yaşına gireceklerini yılı bildiren bir mesaj yazdırın.

# yas=int(input("yasinizi giriniz: "))
# isim=input("isminiz: ")
# yas100=(2022-yas)+100
# print(f"sayın {isim} 100 yaşına gireceğiniz yıl : {yas100}")


#-------------2
metin = input("hangi kelimenin harflerini alt alta yazdırılmasını istiyorusunuz?: ")
sayac = 0

while sayac < len(metin):  # burda hata var
    print(metin[sayac])
    sayac += 1