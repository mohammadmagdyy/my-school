# Generated by Django 3.2.13 on 2022-05-26 11:31

import creditcards.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipmentaddress', models.CharField(default='', max_length=200)),
                ('shipmentphone', models.CharField(default='', max_length=200)),
                ('cardnumber', creditcards.models.CardNumberField(max_length=25)),
                ('expiredate', creditcards.models.CardExpiryField()),
                ('securitycode', creditcards.models.SecurityCodeField(max_length=4)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orders')),
            ],
        ),
    ]
