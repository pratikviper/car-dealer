# Generated by Django 5.0.6 on 2024-05-13 07:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=16)),
                ('cardholder_name', models.CharField(max_length=255)),
                ('expiration_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('cvv', models.CharField(max_length=4)),
            ],
        ),
    ]
