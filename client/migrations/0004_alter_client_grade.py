# Generated by Django 3.2.6 on 2021-08-14 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_alter_client_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='grade',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, verbose_name='Nota'),
        ),
    ]
