# Generated by Django 2.2.10 on 2020-02-24 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
