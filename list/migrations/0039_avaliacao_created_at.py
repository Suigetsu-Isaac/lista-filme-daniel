# Generated by Django 5.0.4 on 2024-07-27 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0038_postagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
