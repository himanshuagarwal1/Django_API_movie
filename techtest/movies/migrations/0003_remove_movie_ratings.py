# Generated by Django 3.2.7 on 2022-05-14 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20220514_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='Ratings',
        ),
    ]
