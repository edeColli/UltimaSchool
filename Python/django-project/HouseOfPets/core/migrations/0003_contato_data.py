# Generated by Django 4.2 on 2023-05-10 22:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_contato"),
    ]

    operations = [
        migrations.AddField(
            model_name="contato",
            name="data",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
