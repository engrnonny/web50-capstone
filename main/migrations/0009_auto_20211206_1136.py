# Generated by Django 3.2.9 on 2021-12-06 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20211206_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cause_file',
            old_name='description',
            new_name='file_description',
        ),
        migrations.RenameField(
            model_name='cause_file',
            old_name='purpose',
            new_name='file_purpose',
        ),
    ]
