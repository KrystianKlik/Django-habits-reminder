# Generated by Django 2.2.10 on 2020-02-24 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200224_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='current_strike_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='habits_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='longest_strike',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
