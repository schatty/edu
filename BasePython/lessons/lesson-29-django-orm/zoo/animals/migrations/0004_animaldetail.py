# Generated by Django 3.2 on 2022-04-03 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_animal_kind'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalDetail',
            fields=[
                ('animal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='animals.animal')),
                ('biography', models.TextField()),
            ],
        ),
    ]
