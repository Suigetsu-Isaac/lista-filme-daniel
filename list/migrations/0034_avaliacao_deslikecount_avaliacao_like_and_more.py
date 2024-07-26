# Generated by Django 5.0.4 on 2024-06-14 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0033_delete_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='deslikeCount',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='like',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='likeCount',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]