# Generated by Django 2.1.1 on 2018-10-16 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crisis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Crisis_Id', models.IntegerField()),
                ('Crisis_Category', models.CharField(max_length=30)),
                ('Crisis_Description', models.TextField()),
                ('Crisis_Assitance', models.CharField(max_length=30)),
                ('Crisis_Status', models.CharField(max_length=30)),
                ('Crisis_Time', models.DateTimeField(auto_now_add=True)),
                ('Crisis_Location', models.TextField()),
            ],
            options={
                'ordering': ['-Crisis_Id'],
            },
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Operator_Id', models.IntegerField()),
                ('Operator_Password', models.CharField(max_length=20)),
                ('Operator_Name', models.CharField(max_length=30)),
                ('Is_Admin', models.BooleanField()),
                ('crisis', models.ManyToManyField(to='api.Crisis')),
            ],
            options={
                'ordering': ['-Operator_Id'],
            },
        ),
    ]
