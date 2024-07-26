# Generated by Django 5.0.3 on 2024-04-24 16:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_genero'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneroFilme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.filmes')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.genero')),
            ],
        ),
    ]