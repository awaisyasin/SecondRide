# Generated by Django 4.2.3 on 2023-08-08 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Ads", "0004_alter_ad_published_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ad",
            name="contact",
            field=models.IntegerField(),
        ),
    ]