# Generated by Django 2.1.1 on 2018-10-21 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181020_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='crisis',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
