# Generated by Django 4.2.4 on 2023-08-05 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_photo_remove_trekdetail_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="trekdetail",
            name="imageFK",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="api.photo",
            ),
        ),
    ]
