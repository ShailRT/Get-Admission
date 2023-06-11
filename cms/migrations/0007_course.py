# Generated by Django 4.1.7 on 2023-06-11 12:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_college_course_fees_college_placement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='header')),
                ('description', ckeditor.fields.RichTextField()),
                ('course_fees', ckeditor.fields.RichTextField()),
                ('placement', ckeditor.fields.RichTextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]