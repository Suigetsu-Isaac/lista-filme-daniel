# Generated by Django 5.0.4 on 2024-06-04 01:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("list", "0015_skinuser"),
    ]

    operations = [
        migrations.AlterField(
            model_name="skin",
            name="img",
            field=models.ImageField(upload_to="static/"),
        ),
    ]
