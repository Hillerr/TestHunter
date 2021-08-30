# Generated by Django 3.2.6 on 2021-08-25 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0006_auto_20210824_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='status',
            field=models.CharField(blank=True, choices=[('Finalizado', 'Finalizado'), ('Em andamento', 'Em andamento')], default='Em andamento', max_length=20, verbose_name='Status'),
        ),
    ]