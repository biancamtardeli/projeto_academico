# Generated by Django 5.1.3 on 2024-12-03 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_pessoa_ocupacao_remove_pessoa_turma_aluno_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacao',
            name='pessoa',
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='aluno',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.aluno'),
        ),
    ]
