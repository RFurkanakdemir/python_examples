import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE','kitap_docs.settings')

import django
django.setup()

from django.contrib.auth.models import User
from faker import Faker
# from faker.providers.person.en_US import Provider




def set_user():
    fakegen = Faker(['tr_TR'])
    
    f_name = fakegen.first_name()
    l_name = fakegen.last_name()
    u_name = f'{f_name.lower()}_{l_name.lower()}'
    email = f'{u_name}@{fakegen.domain_name()}'

    user_check = User.objects.filter(username=u_name)
    
    while user_check.exists():
        u_name = u_name + str(random.randrange(1,99))  
        user_check = User.objects.filter(username=u_name)
 

    user = User(
        username = u_name,
        first_name = f_name,
        last_name = l_name,
        email= email,
        # password = 'test321'
    )

    user.set_password('test321.')
    user.save()




import requests
from kitaplar.api.serializers import KitapSerializer
import pprint

def kitap_ara(konu):
    fake = Faker(['tr_TR'])
    url = 'http://openlibrary.org/search.json'
    payload = {'q':konu}
    response = requests.get(url,params=payload)
    
    
    if response.status_code!=200:
        print('yanlis istek',response.status_code)
        return

    jsn = response.json()
    
    kitaplar = jsn.get('docs')
    
    for kitap in kitaplar:
        x=kitap.get('has_fulltext')
        if x == True:
            ack='-'.join(kitap.get('ia'))
        else:
            ack = 'aciklama bulunmamaktadir'

        data = dict(
            isim=kitap.get('title'),
            yazar = kitap.get('author_name')[0],
            aciklama = ack ,
            yayin_tarihi = fake.date_time_between(start_date='-10y',end_date='now',tzinfo=None)
            )
        serializer = KitapSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            continue
        