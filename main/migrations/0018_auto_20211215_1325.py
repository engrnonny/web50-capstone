# Generated by Django 3.2.9 on 2021-12-15 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20211215_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='month',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='info',
            name='total_amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='info',
            name='year',
            field=models.IntegerField(),
        ),
    ]
