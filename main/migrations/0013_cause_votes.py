# Generated by Django 3.2.9 on 2021-12-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20211211_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='cause',
            name='votes',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
