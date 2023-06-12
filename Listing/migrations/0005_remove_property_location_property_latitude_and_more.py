# Generated by Django 4.2.2 on 2023-06-12 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Listing", "0004_contactmessage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="property",
            name="location",
        ),
        migrations.AddField(
            model_name="property",
            name="latitude",
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name="property",
            name="longitude",
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
        ),
    ]
