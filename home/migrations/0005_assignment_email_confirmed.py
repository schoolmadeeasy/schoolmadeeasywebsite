# Generated by Django 2.1.3 on 2018-12-08 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20181130_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
