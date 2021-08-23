# Generated by Django 3.2.6 on 2021-08-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_auto_20210820_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='fb_comments',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Comentário sobre o feedback que o cliente forneceu'),
        ),
        migrations.AlterField(
            model_name='test',
            name='tk_comments',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Comentário sobre conhecimento técnico'),
        ),
        migrations.AlterField(
            model_name='test',
            name='tr_comments',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Comentário sobre o tempo de resposta'),
        ),
    ]