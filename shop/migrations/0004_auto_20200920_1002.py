# Generated by Django 3.1.1 on 2020-09-20 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.CharField(default=0, max_length=800),
        ),
    ]
