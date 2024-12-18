# Generated by Django 5.0.1 on 2024-12-18 08:48

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "deleted",
                    models.BooleanField(
                        default=False, help_text="This is for soft delete"
                    ),
                ),
                (
                    "profile_photo",
                    models.FileField(
                        default="/profile.png",
                        upload_to="",
                        verbose_name="Profile Photo",
                    ),
                ),
            ],
            options={
                "ordering": ["-updated_at", "-created_at"],
                "abstract": False,
            },
            managers=[
                ("everything", django.db.models.manager.Manager()),
            ],
        ),
    ]
