# Generated by Django 5.1.3 on 2024-11-26 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_avaliacao_pessoa_disciplina_curso_disciplina_pessoa_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='nome_da_mae',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='data_nasc',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='nome_do_pai',
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.pessoa')),
                ('nome_do_pai', models.CharField(default='', max_length=100, verbose_name='mãe')),
                ('nome_da_mae', models.CharField(default='', max_length=100, verbose_name='pai')),
                ('cpf', models.CharField(default=0, max_length=11)),
                ('data_nasc', models.DateField(default='2000-01-01', verbose_name='data de nascimento')),
            ],
            options={
                'verbose_name': 'Pessoa Física',
                'verbose_name_plural': 'Pessoas Físicas',
            },
            bases=('app.pessoa',),
        ),
    ]