# Generated by Django 5.0.4 on 2024-06-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("list", "0019_alter_skinuser_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="skinuser",
            name="img",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]