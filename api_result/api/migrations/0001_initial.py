# Generated by Django 2.0.6 on 2018-06-10 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=1)),
                ('course', models.CharField(max_length=5)),
                ('roll_no', models.IntegerField()),
                ('year', models.IntegerField()),
                ('result_type', models.CharField(max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
