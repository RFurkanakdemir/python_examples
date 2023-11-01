from re import M


frknhesap={
    'ad':'furkan akdemir',
    'Hesapno':'415653',
    'bakiye':3000,
    'ekhesap':2000
}
alihesap={
    'ad':'ali akdemir',
    'Hesapno':'123456',
    'bakiye':3000,
    'ekhesap':1000
}

def paracekme(miktar,hesap):
    print(f"merhaba {hesap['bakiye']}")

    tplmBky=hesap['bakiye']+hesap['ekhesap']
    if(miktar>tplmBky):
        print("Bakiyeniz yetersizdir.")
    elif miktar>hesap['bakiye']:
        hesap['bakiye']=0
        hesap['ekbakiye']=hesap['ekbakiye']-(miktar-hesap['bakiye'])
        print(f"{miktar} tl çekme işleminiz tamamlanmıştır.")
    
    else:
        hesap['bakiye']=hesap['bakiye']-miktar
        print(f"{miktar} tl çekme işleminiz tamamlanmıştır.")
        


hesapismi=input("hesap ismi giriniz: ")
hesap=frknhesap
print(hesap)

howMuch=int(input(f"ne kadar çekmek istersiniz"))
paracekme(howMuch,hesap)