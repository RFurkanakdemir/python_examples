sayi=int(input("bir sayı giriniz: "))
bölüm=sayi
asalmi=True
if(sayi>0 and sayi!=1):
    while bölüm>1:
        bölüm=bölüm-1
        
        if(sayi%bölüm==0 and bölüm>1):
            asalmi=False
            print("girilen sayi asal değildir.")
            break
     
    
    if(asalmi==True):
        print(f"{sayi} sayisi asaldır")



#for i in range(2,sayi) ilede döngü kurulabilir