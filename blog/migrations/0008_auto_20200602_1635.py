# Generated by Django 2.2.6 on 2020-06-02 11:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200602_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription_form',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 2, 11, 5, 12, 180217, tzinfo=utc)),
        ),
    ]