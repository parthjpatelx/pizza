# Generated by Django 3.1.4 on 2020-12-25 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_cart'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dinner_platter',
            options={'verbose_name': 'dinnerplatter'},
        ),
        migrations.AlterModelOptions(
            name='food',
            options={'verbose_name': 'NA for food class'},
        ),
        migrations.AlterModelOptions(
            name='pasta',
            options={'verbose_name': 'pasta'},
        ),
        migrations.AlterModelOptions(
            name='regular_pizza',
            options={'verbose_name': 'regularpizza'},
        ),
        migrations.AlterModelOptions(
            name='salad',
            options={'verbose_name': 'salad'},
        ),
        migrations.AlterModelOptions(
            name='sicilian_pizza',
            options={'verbose_name': 'sicilianpizza'},
        ),
    ]
