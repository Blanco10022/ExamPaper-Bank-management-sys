# Generated by Django 4.0.4 on 2022-05-26 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateurs', '0002_alter_profile_photo_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='photo_profile',
            new_name='profile_pic',
        ),
    ]