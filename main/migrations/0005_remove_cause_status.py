# Generated by Django 3.2.9 on 2021-12-04 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211204_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cause',
            name='status',
        ),
    ]
