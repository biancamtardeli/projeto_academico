# Generated by Django 5.1.3 on 2024-11-26 17:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_uf_remove_cidade_uf'),
    ]

    operations = [
        migrations.AddField(
            model_name='cidade',
            name='UF',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.uf'),
        ),
        migrations.AlterField(
            model_name='cidade',
            name='nome',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='uf',
            name='sigla',
            field=models.CharField(default='', max_length=2),
        ),
    ]
