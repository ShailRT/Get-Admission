# Generated by Django 4.1.7 on 2023-04-12 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='institute_type',
            field=models.CharField(choices=[('University', 'university'), ('College', 'college')], default='college', max_length=120),
        ),
    ]
