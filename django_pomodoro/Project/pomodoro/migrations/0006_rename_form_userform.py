# Generated by Django 5.1.2 on 2024-11-25 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pomodoro', '0005_form'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='form',
            new_name='UserForm',
        ),
    ]
