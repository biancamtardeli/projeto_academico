# Generated by Django 5.1.3 on 2024-12-03 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_frequencia_pessoa_frequencia_aluno_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matricula',
            name='pessoa',
        ),
        migrations.AddField(
            model_name='matricula',
            name='aluno',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.aluno'),
        ),
    ]
