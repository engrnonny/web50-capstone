# Generated by Django 3.2.9 on 2021-11-30 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20211126_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cause',
            name='lga',
        ),
    ]
