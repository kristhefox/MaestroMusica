# Generated by Django 3.0.7 on 2022-01-17 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0002_auto_20220109_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='desctiption',
            new_name='description',
        ),
    ]