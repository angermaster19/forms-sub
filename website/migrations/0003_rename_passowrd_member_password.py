# Generated by Django 4.2.7 on 2023-11-11 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_members_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='passowrd',
            new_name='password',
        ),
    ]
