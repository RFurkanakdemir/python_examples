# Generated by Django 4.1.3 on 2022-11-14 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oncelik', models.CharField(choices=[('ÇÖ', 'çok önemli'), ('Ön', 'önemli'), ('NRML', 'normal'), ('grks', 'aciliyeti yok'), ('önmz', 'önemsiz')], default='NRML', max_length=5)),
                ('icerik', models.TextField(blank=True, default='görevi giriniz', max_length=500)),
                ('bas_tarih', models.DateTimeField(default=datetime.datetime(2022, 11, 14, 17, 13, 9, 431122))),
                ('bit_tarih', models.DateTimeField(default=datetime.datetime(2022, 11, 14, 17, 13, 9, 431122))),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
