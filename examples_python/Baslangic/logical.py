# x=input("email giriniz: ")
# ipassword=input("parola giriniz: ")

# email="rfrknakdemir@gmail"
# password="f4156532"


# result= (x.strip().lower()==email) and (ipassword.strip()==password)
# print(f"email ve şifre girildi: {result}")

from typing import final


vize1=int(input("1.vize notu?: "))

vize2=int(input("2.vize notu?: "))

final=int(input("final notu?: "))

ortalama=(((vize1+vize2)/2)*0.6)+(final*0.4)


gecme=((ortalama>50) and (final>50)) or (final>70)

print(f"dersten kalma gecme durumunuz true geçti: {gecme}\nortalama: {ortalama}\nfinal: {final}")