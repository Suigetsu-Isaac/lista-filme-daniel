# Generated by Django 5.0.4 on 2024-06-14 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0031_avaliacao_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacao',
            name='like',
        ),
    ]
