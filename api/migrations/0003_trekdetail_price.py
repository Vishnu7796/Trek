# Generated by Django 4.2.4 on 2023-08-03 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_rename_trekdetails_trekdetail"),
    ]

    operations = [
        migrations.AddField(
            model_name="trekdetail",
            name="price",
            field=models.IntegerField(default=1299),
        ),
    ]