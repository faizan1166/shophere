# Generated by Django 3.1.2 on 2020-10-18 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_buy_pin'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='product_name',
            field=models.CharField(default='', max_length=70),
        ),
    ]
