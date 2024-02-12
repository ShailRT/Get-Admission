# Generated by Django 4.1.7 on 2024-02-12 15:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0015_course_duration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="course_fees",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="course",
            name="description",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="course",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="header"),
        ),
        migrations.AlterField(
            model_name="course",
            name="intro",
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]
