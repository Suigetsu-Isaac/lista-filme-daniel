# Generated by Django 5.0.4 on 2024-06-08 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0021_filmes_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmes',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
