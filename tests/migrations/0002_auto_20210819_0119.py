# Generated by Django 3.2.6 on 2021-08-19 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='fb_comments',
            field=models.TextField(blank=True, max_length=300, verbose_name='Comentário sobre o feedback que o cliente forneceu'),
        ),
        migrations.AlterField(
            model_name='test',
            name='final_comments',
            field=models.TextField(blank=True, max_length=300, verbose_name='Comentários finais'),
        ),
        migrations.AlterField(
            model_name='test',
            name='tk_comments',
            field=models.TextField(blank=True, max_length=300, verbose_name='Comentário sobre conhecimento técnico'),
        ),
        migrations.AlterField(
            model_name='test',
            name='tr_comments',
            field=models.TextField(blank=True, max_length=300, verbose_name='Comentário sobre o tempo de resposta'),
        ),
    ]
