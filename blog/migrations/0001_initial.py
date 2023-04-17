# Generated by Django 4.1.7 on 2023-04-17 00:58

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('intro', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='blog')),
                ('category', models.TextField()),
                ('tags', models.TextField()),
                ('body', ckeditor.fields.RichTextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.author')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
