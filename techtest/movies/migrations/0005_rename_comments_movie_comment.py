# Generated by Django 3.2.7 on 2022-05-15 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='comments',
            new_name='Comment',
        ),
    ]