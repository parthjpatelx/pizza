# Generated by Django 3.1.4 on 2020-12-25 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20201225_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='quantity',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
