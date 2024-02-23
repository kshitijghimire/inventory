# Generated by Django 5.0.2 on 2024-02-22 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated',
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default='uncategorized', max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='added',
            field=models.DateField(default=datetime.datetime.now, null=True),
        ),
    ]
