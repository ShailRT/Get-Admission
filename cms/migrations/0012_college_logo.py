# Generated by Django 4.1.7 on 2024-02-08 16:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0011_course_meta_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="college",
            name="logo",
            field=models.ImageField(blank=True, null=True, upload_to="logo"),
        ),
    ]