# Generated by Django 4.0.5 on 2022-08-16 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='details',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='user',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='order',
        ),
        migrations.DeleteModel(
            name='orderdetails',
        ),
        migrations.DeleteModel(
            name='orders',
        ),
        migrations.DeleteModel(
            name='payment',
        ),
    ]