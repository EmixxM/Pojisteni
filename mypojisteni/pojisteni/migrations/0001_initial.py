# Generated by Django 4.1.7 on 2023-05-08 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pojisteny',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=100)),
                ('prijmeni', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Pojisteni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=100)),
                ('popis', models.TextField()),
                ('pojisteny', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pojisteni', to='pojisteni.pojisteny')),
            ],
        ),
    ]
