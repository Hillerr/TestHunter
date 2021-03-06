# Generated by Django 3.2.7 on 2021-09-19 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='segment',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=20, verbose_name='Segmento'),
        ),
        migrations.AddField(
            model_name='account',
            name='unit',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default='A', max_length=20, verbose_name='Unidade'),
        ),
    ]
