# Generated by Django 3.2.9 on 2021-12-23 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20211215_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cause',
            name='expiration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
