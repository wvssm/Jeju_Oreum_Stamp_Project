# Generated by Django 4.2.10 on 2024-03-09 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mymap", "0004_oreum_ocontent"),
    ]

    operations = [
        migrations.AddField(
            model_name="oreum",
            name="oparking",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="oreum",
            name="otoilet",
            field=models.CharField(max_length=10, null=True),
        ),
    ]