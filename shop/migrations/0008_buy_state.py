# Generated by Django 3.1.2 on 2020-10-18 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_buy_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='state',
            field=models.CharField(default='', max_length=70),
        ),
    ]