# Generated by Django 2.2.6 on 2020-05-26 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200502_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription_form',
            name='increased_hunger',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='prescription_form',
            name='increased_thirst',
            field=models.BooleanField(default=False),
        ),
    ]
