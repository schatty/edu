# Generated by Django 3.2 on 2022-04-03 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0005_animalfood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalfood',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]