liste=["1","2","5a","10b","abc","@1","50"]

#-------------------1

# sayisal=[]
# for i in liste:
#     import re
#     if not re.search("[a-z]",i):
#         sayisal.append(i)

# print(sayisal)

# diger yontem
# for x in liste:
#     try:
#         result=int(x)
#         print(result)
#     except ValueError:
#         continue


#-------------------------2
# sayilar=[]
# while True:
     
#     sayi=input("veri giriniz")
#     if sayi=="q":
#         break
     
#     try:
#         sayi=int(sayi)
#         sayilar.append(sayi)
#     except:
#         print("sayi yanlis")


# print(sayilar)

#--------------------------------3
# from logging import exception
# import re
# def check_pass(psw):
#     if re.findall("[ğĞçÇşŞüÜöÖıİ]",psw):

#         raise exception("türkçe karakter kullanmayınız")


# psw=input("parola giriniz: ")
# check_pass(psw)

#diger yol
# def checkPassword(parola):
#     turkce_karakterler = 'şçğüöıİ'

#     for i in parola:
#         if i in turkce_karakterler:
#             raise TypeError('Parola türkçe karakter içeremez.')
#         else:
#             pass
#     print('geçerli parola')    

# parola = input('parola: ')

# try:
#     checkPassword(parola)    
# except TypeError as err:
#     print(err)

#-----------------------------4
def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError('Negatif değer')

    result = 1

    for i in range(1, x+1):
        result *= i

    return result

for x in [5, 10, 20, -3, '10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue 
    print(y)






# sayi=input("sayi giriniz")
