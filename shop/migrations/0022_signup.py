# Generated by Django 3.1.2 on 2020-10-31 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_auto_20201026_0842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('Signup_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('password', models.CharField(default='', max_length=70)),
            ],
        ),
    ]