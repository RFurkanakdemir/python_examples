# sayilar=[1,3,5,7,9,12,19,21]
# toplam=0
# for x in sayilar:

#     toplam=toplam+x

# print(toplam)

# for x in sayilar:
#     if (x%2==1):
#         karesi=x**2
#         print(karesi)
   
# sehirler=['kocaeli','istanbul','ankara','izmir','rize']

# for x in sehirler:
#     if (len(x)<=5):
#         print(f"{x} sehri 5 karakterden kısadır")
#     else:
#         print(f"{x} sehri 5 karakterden uzundur")

from traceback import print_exc


urunler=[
    {'name':'samsung s6', 'price':'3000'},
    {'name':'samsung s7', 'price':'4000'},
    {'name':'samsung s8', 'price':'5000'},
    {'name':'samsung s9', 'price':'6000'},
    {'name':'samsung s10', 'price':'7000'},
]
# toplam=0
# for urun in urunler:
#     price=int(urun['price'])
#     toplam+=price
#     print(toplam)

# print(toplam)

for urun in urunler:
    if (int(urun['price'])<=5000):
        print(urun['name'])








