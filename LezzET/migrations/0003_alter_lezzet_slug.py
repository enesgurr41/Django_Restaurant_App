# Generated by Django 3.2.9 on 2021-12-16 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LezzET', '0002_lezzet_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lezzet',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
