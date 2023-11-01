import json
import requests


ex_api="https://v6.exchangerate-api.com/v6/ab9beaeab69ecb36ac0815e6/latest/"  #internetten alınan api verisi
   
    

bozulandvz=input("bozulan döviz türü: ")
alınandvz=input("alınan döviz türü: ")
miktar=int(input(f"Ne kadar {bozulandvz} bozdurmak istersiniz"))

result=requests.get(ex_api+bozulandvz)  #verilen apinin sonuna istenen kur eklenerek özel olarak kur verileri izlendi
result=result.text  #alınan api verisi metinsel ifadeye çevirildi
result=json.loads(result)   #gelen str ifade dictionary listeye döndü
print("1 {0} = {1} {2}".format(bozulandvz,result["conversion_rates"][alınandvz],alınandvz))
print("{0} {1} = {2} {3}".format(miktar,bozulandvz,miktar*result["conversion_rates"][alınandvz],alınandvz))
