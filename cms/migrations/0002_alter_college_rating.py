# Generated by Django 4.1.7 on 2023-04-17 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]
