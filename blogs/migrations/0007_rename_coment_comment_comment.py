# Generated by Django 5.1.2 on 2024-11-03 23:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0006_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="coment",
            new_name="comment",
        ),
    ]
