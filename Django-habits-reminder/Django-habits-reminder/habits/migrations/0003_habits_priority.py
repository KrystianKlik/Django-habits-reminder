# Generated by Django 2.2.10 on 2020-02-24 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_habits_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='habits',
            name='priority',
            field=models.SmallIntegerField(default=0, max_length=10),
        ),
    ]