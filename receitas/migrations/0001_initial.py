# Generated by Django 4.1.2 on 2022-10-29 16:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_receita', models.CharField(max_length=50)),
                ('ingredientes', models.TextField()),
                ('modo_preparo', models.TextField()),
                ('tempo_preparo', models.IntegerField()),
                ('rendimetno', models.TextField(max_length=40)),
                ('categoria', models.CharField(max_length=40)),
                ('data', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
