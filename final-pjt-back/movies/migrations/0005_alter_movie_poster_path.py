# Generated by Django 3.2.6 on 2022-11-23 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_likemovielist_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster_path',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
