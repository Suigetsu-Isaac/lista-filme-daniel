# Generated by Django 5.0.4 on 2024-08-03 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0044_remove_avaliacao_postagem_avaliacao_filme_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plataformastreaming',
            name='logo',
            field=models.ImageField(blank=True, default='/images/filme-default.png', null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='plataformastreamingfilme',
            name='urlFilme',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
