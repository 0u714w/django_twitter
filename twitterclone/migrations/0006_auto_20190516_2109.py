# Generated by Django 2.2 on 2019-05-16 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0005_auto_20190516_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='datetime',
            field=models.DateTimeField(default='2019-05-16 17:09:27 EDT-0400'),
        ),
    ]
