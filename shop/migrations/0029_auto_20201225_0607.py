# Generated by Django 3.1.2 on 2020-12-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_buy_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='product_detail',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='buy',
            name='product_detail1',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
