# Generated by Django 4.1.2 on 2022-10-31 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='makale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metin', models.TextField()),
                ('yayinlanma_Tarihi', models.DateField()),
                ('aktif', models.BooleanField(default=True)),
            ],
        ),
    ]
